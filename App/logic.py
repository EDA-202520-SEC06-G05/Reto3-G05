import time
import os
import math
from DataStructures.List import single_linked_list as sl
from DataStructures.Map import map_linear_probing as lp
from DataStructures.Tree import red_black_tree as rbt
from DataStructures.Tree import rbt_node as rn
from DataStructures.Priority_queue import priority_queue as pq
import csv


data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/Challenge-3'

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    analyzer = {
        "flights": None,
    }
    analyzer["flights"] = lp.new_map(304000, 0.7, None)
    return analyzer
    #TODO: Llama a las funciónes de creación de las estructuras de datos

# Funciones para la carga de datos
    
def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    flight = load_flights(catalog)
    return flight
    # TODO: Realizar la carga de datos

def load_flights(analyzer):
    
    inicio = get_time()
    flight_total = 0
    flights_rbt = rbt.new_map()
    
    flight_file = data_dir + "/flights_small.csv"
    input_file = csv.DictReader(open(flight_file, encoding="utf-8"), delimeter=",")
    for flight in input_file:
        add_flights(analyzer, flight)
        flight_total += 1
        
        date_str = flight["date"]              
        date_parts = date_str.split("-")    
        year = int(date_parts[0])
        month = int(date_parts[1])
        day = int(date_parts[2])
        date_int = year * 10000 + month * 100 + day
        
        time_str = flight["sched_dep_time"]
        partes = time_str.split(":")
        hh = int(partes[0])
        mm = int(partes[1])
        sched_int = hh * 100 + mm
        
        key_rbt = date_int * 10000 + sched_int
        rbt.put(flights_rbt, key_rbt, flight)
    
    ordered = rbt.value_set(flights_rbt)
    total = ordered["size"]
    
    first5 = sl.new_list()
    last5 = sl.new_list()
    
    i = 0
    while i < total:
        if i < 5:
            element = sl.get_element(ordered, i)
            sl.add_last(first5, element)
        i += 1
    
    last_start = total -5
    if last_start < 0:
        last_start = 0
        
    i2= last_start
    while i2 < total:
        if i2 >= last_start:
            elem = sl.get_element(ordered, i2)
            sl.add_last(last5, elem)
        i2 += 1
    fin = get_time()
    
    return {
        "tiempo_ms": fin - inicio, 
        "total_vuelos": flight_total,
        "primeros5": first5,
        "ultimos5": last5
    }                        
    # Falta eliminar las llaves que no estan pidiendo en el requerimiemnto #############################################################################           
        
def add_flights(analyzer, fligh):
    flight_map = analyzer["flights"]
    key = int(fligh["id"])
    lp.put(flight_map, key, fligh)
    return analyzer    
    
    
# Funciones de consulta sobre el catálogo


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog, code, min, max):
    
    start = get_time()
    filtered_rbt = rbt.new_map()
    filtered_no = 0
    table = catalog["flights"]["table"]
    for entry in table["elements"]:
        if entry["value"] is not None:
            flight = entry["value"]
            
            if flight["dest"] != "" and flight["arr_time"] != "" and flight["sched_arr_time"] != "":
                arr_time = str(flight["arr_time"])
                sched_arr_time = str(flight["sched_arr_time"])
               
                arr_time_h, arr_time_s = arr_time.split(":")
                sched_arr_time_h, sched_arr_time_s = sched_arr_time.split(":")
               
                arr_time_minutes = int(arr_time_h) *60 + int(arr_time_s)
                sched_arr_time_minutes = int(sched_arr_time_h) *60 + int(sched_arr_time_s)
               
                delay = arr_time_minutes - sched_arr_time_minutes
                if delay < -720:
                    delay += 1440
                elif delay > 720:
                    delay -= 1440
                    
                if (flight["dest"] == code) and (min <= delay <= max):
                    filtered_no += 1
                    flight_date = str(flight["date"])
                    y, m ,d = flight_date.split("-")
                    date_int = int(y) * 10000 + int(m)*100 + int(d)
                    arr_int = int(arr_time_h)* 100 + int(arr_time_s)
                    key = delay * 100000000 + date_int * 10000 + arr_int
                    req_flight = {
                        "id": flight["id"],
                        "flight": flight["flight"],
                        "date": flight["date"],
                        "airline_name": flight["name"],
                        "airline_code": flight["carrier"],
                        "origin": flight["origin"],
                        "dest": flight["dest"],
                        "early_minutes": delay
                    }
                    rbt.put(filtered_rbt, key, req_flight)
                    
    ordered = rbt.value_set(filtered_rbt)
    total = ordered["size"]
    
    if total > 10:
        first5 = sl.new_list()
        last5 = sl.new_list()
        i = 0
        while i < total:
            if i < 5:
                element = sl.get_element(ordered, i)
                sl.add_last(first5, element)
            i += 1
    
        last_start = total -5
        if last_start < 0:
            last_start = 0
        
        i2= last_start
        while i2 < total:
            if i2 >= last_start:
                elem = sl.get_element(ordered, i2)
                sl.add_last(last5, elem)
            i2 += 1
        fin = get_time()
        return {
            "time_ms": fin - start,
            "filtered_number": filtered_no,
            "first5": first5,
            "last5": last5 
        }
    fin = get_time()
    return {
        "time_ms": fin - start,
        "filtered_number": filtered_no,
        "filtered_flights": ordered
    }
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog, fech_min, fech_max, dist_min, dist_max, m):
    """
    Retorna el resultado del requerimiento 6
    """
    start = get_time()
    airline_rbt = rbt.new_map()
    
    table = catalog["flights"]["table"]
    for entry in table["elements"]:
        if entry["value"] is not None:
            flight = entry["value"]
            if (flight["dep_time"] != "") and (flight["sched_dep_time"] != "") and (flight["distance"] != "") and (flight["date"]!= ""):
                
                date = str(flight["date"])
                y, m, d = date.split("-")
                date_int = int(y) * 10000 + int(m)* 100 + int(d)
                distance = int(flight["distance"])
                
                date2 = str(fech_min)
                y2, m2, d2 = date2.split("-")
                fecha_min_int = int(y2) * 10000 + int(m2)*100 + int(d2)
                
                date3 = str(fech_max)
                y3, m3, d3 = date3.split("-")
                fecha_max_int = int(y3) * 10000 + int(m3)*100 + int(d3)

                if (fecha_min_int <= date_int <= fecha_max_int) and (dist_min <= distance <= dist_max):
                    
                    dep_time = str(flight["dep_time"])
                    sched_dep_time = str(flight["sched_dep_time"])
                
                    dep_time_h, dep_time_s = dep_time.split(":")
                    sched_dep_time_h, sched_dep_time_s = sched_dep_time.split(":")
                
                    dep_time_minutes = int(dep_time_h)*60 + int(dep_time_s)
                    sched_dep_time_minutes = int(sched_dep_time_h)*60 + int(sched_dep_time_s)
                
                    delay = dep_time_minutes - sched_dep_time_minutes
                    if delay < -720:
                        delay += 1440
                    elif delay > 720:
                        delay -= 1440
                    
                    airline = flight["airline"]
                    info = rbt.get(airline_rbt, airline)
                    if info is None:
                        info = {
                            "delays": sl.new_list(),
                            "sum": 0, 
                            "sum2": 0,
                            "count": 0
                        }
                    rbt.put(airline_rbt, airline, info)
                    
                    sl.add_last(info["delays"], {"delay": delay, "flight": flight})
                    info["sum"] += delay
                    info["sum2"] += delay * delay
                    info["count"] += 1
                    
    keys = rbt.key_set(airline_rbt)
    airline_total = keys["size"]
    
    pq_heap = pq.new_heap(is_min_pq=True)
    
    i = 0
    while i < airline_total:
        code = sl.get_element(keys, i)
        info = rbt.get(airline_rbt, code)
        
        if info["count"] > 0:
            averg = info["sum"] / info["count"]
            
            varian = (info["sum2"] / info["count"]) - (averg * averg)
            if varian < 0:
                varian = 0
            deviation = math.sqrt(varian)                      
            
            delays = info["delays"]
            size = delays["size"]
            best = None
            best_dif = 1440
            
            i2 = 0 
            while i2 < size:
                par = sl.get_element(delays, i2)
                diff = par["delay"] - averg
                if diff < 0:
                    diff = -diff
                if diff < best_dif:
                    best_dif = diff
                    best = par
                i2 += 1
                
            pq.insert(pq_heap, deviation, {
                "airline": code, 
                "count": info["count"],
                "avg": averg,
                "dev": deviation,
                "closest": best
            })
        i += 1
        
    result_list = sl.new_list()
    extracted = 0
    while extracted < m and not pq.is_empty(pq_heap):
        element = pq.remove(pq_heap)
        sl.add_last(result_list, element["value"])
        extracted +=1
    
    end = get_time()
    
    return {
        "time_ms": end - start,
        "total_airlines": extracted,
        "airlines": result_list
    }     
    
    # TODO: Modificar el requerimiento 6



# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
