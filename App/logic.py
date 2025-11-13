import time
import os
import math
from DataStructures.List import array_list as al
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
        "Verificar que sea correcto y si el api de rbt lo permite si no volver a la version anterior"
        
    ordered = rbt.value_set(flights_rbt)
    total = ordered["size"]
    
    first5 = sl.new_list()
    last5 = sl.new_list()
    
    i = 0
    while i < total:
        if i < 5:
            flight = sl.get_element(ordered, i)
            clean_return = {
                "date": flight["date"],
                "dep_time": flight["dep_time"],
                "arr_time": flight["arr_time"],
                "airline_code": flight["carrier"],
                "airline_name": flight["airline"],
                "tailnum": flight["tailnum"],
                "origin": flight["origin"],
                "dest": flight["dest"],
                "air_time": flight["air_time"],
                "distance": flight["distance"]
            }
            sl.add_last(first5, clean_return)
        i += 1
    
    last_start = total -5
    if last_start < 0:
        last_start = 0
        
    i2= last_start
    while i2 < total:
        if i2 >= last_start:
            flight = sl.get_element(ordered, i2)
            clean_return = {
                "date": flight["date"],
                "dep_time": flight["dep_time"],
                "arr_time": flight["arr_time"],
                "airline_code": flight["carrier"],
                "airline_name": flight["airline"],
                "tailnum": flight["tailnum"],
                "origin": flight["origin"],
                "dest": flight["dest"],
                "air_time": flight["air_time"],
                "distance": flight["distance"]
            }
            sl.add_last(last5, clean_return)
        i2 +=1
    fin = get_time()
    
    return {
        "tiempo_ms": fin - inicio, 
        "total_vuelos": flight_total,
        "primeros5": first5,
        "ultimos5": last5
    }                        
        
def add_flights(analyzer, fligh):
    flight_map = analyzer["flights"]
    key = int(fligh["id"])
    lp.put(flight_map, key, fligh)
    return analyzer    
    
    
# Funciones de consulta sobre el catálogo
def req_1(catalog, airline_code, min_delay, max_delay):
    start=get_time()
    filtered_rbt=rbt.new_map()
    filtered_no=0
    table= catalog["flights"]["table"]
    for entry in table["elements"]:
        if entry["value"] is not None:
            flight= entry["value"]
            if flight["carrier"] != "" and flight["dep_time"]!= "" and flight["sched_dep_time"]!= "":
                dep_time= str(flight["dep_time"])
                sched_dep_time= str(flight["sched_dep_time"])
                dep_h,dep_m= dep_time.split(":")
                sched_h,sched_m= sched_dep_time.split(":")
                dep_minutes= int(dep_h)*60 + int(dep_m)
                sched_minutes= int(sched_h)*60 + int(sched_m)
                delay= dep_minutes-sched_minutes
                if delay<-720:
                    delay+= 1440
                elif delay> 720:
                    delay-= 1440
                if (flight["carrier"]== airline_code) and (min_delay <= delay <= max_delay):
                    filtered_no+= 1
                    flight_date= str(flight["date"])
                    y, m, d= flight_date.split("-")
                    date_int= int(y)*10000 + int(m)*100 + int(d)
                    dep_int= int(dep_h)*100 + int(dep_m)
                    key= delay*100000000 + date_int*10000 + dep_int
                    req_flight={
                        "id": flight["id"],
                        "flight": flight["flight"],
                        "date": flight["date"],
                        "airline_name": flight["name"],
                        "airline_code": flight["carrier"],
                        "origin": flight["origin"],
                        "dest": flight["dest"],
                        "delay_minutes": delay}
                    rbt.put(filtered_rbt, key, req_flight)
    ordered= rbt.value_set(filtered_rbt)
    total= ordered["size"]
    if total> 10:
        first5= sl.new_list()
        last5= sl.new_list()
        i= 0
        while i< total:
            if i<5:
                element = sl.get_element(ordered, i)
                sl.add_last(first5, element)
            i+= 1
        last_start= total - 5
        if last_start< 0:
            last_start= 0
        i2= last_start
        while i2< total:
            elem= sl.get_element(ordered, i2)
            sl.add_last(last5, elem)
            i2+= 1
        fin= get_time()
        return{
            "time_ms": fin - start,
            "filtered_number": filtered_no,
            "first5": first5,
            "last5": last5}
    fin= get_time()
    return{
        "time_ms": fin - start,
        "filtered_number": filtered_no,
        "filtered_flights": ordered}

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
    


def req_3(catalog, airline, code_airport , distance):
    """
    Retorna el resultado del requerimiento 3
    """
    result = {
        "time": get_time(),
        "total_flights": 0,
        "first": None,
        "last" : None
        
    }
    tree = rbt.new_map()
    
    map = catalog["flights"]
    table = map["table"]
    for each in table["elements"]:
        if each != None:
            single_flight = each["value"]
            if single_flight["carrier"] == airline and single_flight["dest"] == code_airport and distance[0] <=  int(single_flight["distance"]) <= distance[1]:
                result["total_flights"] += 1
                if rbt.contains(tree, single_flight["distance"]):
                    value_array = rbt.get(tree, single_flight["distance"])
                    al.add_last(value_array, single_flight)
                    rbt.put(tree, single_flight["distance"], value_array)
                else:
                    array = al.new_list()
                    dict_flight = {
                        "id": single_flight["id"],
                        "flight": single_flight["flight"],
                        "date": single_flight["date"],
                        "airline_name": single_flight["name"],
                        "airline_code": single_flight["carrier"],
                        "origin": single_flight["origin"],
                        "dest": single_flight["dest"],
                        "distance": float(single_flight["distance"])
                    }
                    al.add_last(array,dict_flight)
                    rbt.put(tree, single_flight["distance"],array)
    def default_criteria (flight1, flight2):
        if flight1["arr_time"] < flight2["arr_time"]:
            return True
        else:
            return False
        
    values = rbt.value_set(tree)
    if values["size"] > 0:
            last5 = al.new_list()
            i = 1
            while i <= values["size"]:
                element = sl.get_element(values, i)
                if element["size"] >= 2:
                    sort = al.merge_sort(element, default_criteria)
                    for each in sort:
                        al.add_last(last5, each)
                else:
                    al.add_last(last5, element["elements"][0])
                i += 1
            
            total = last5["size"]
            if total < 10:
                result["first"] = last5
                del result["last"]
            else:
                result["first"] = al.sublist(last5, 0, 5) 
                result["last"] = al.sublist(last5, last5["size"] -5, last5["size"])   
    else:
        result["first"] = al.new_list()
        result["last"] = al.new_list()
    final = get_time()
    result["time"] = final - result["time"]
    return result

    # TODO: Modificar el requerimiento 3



def req_4(catalog,date,time,n):
    """
    Retorna el resultado del requerimiento 4
    """
    result = {
        "time": get_time(),
        "total_airports": 0,
        "airports": sl.new_list()
    }
    airline = {}
    tree = rbt.new_map()
    map = catalog["flights"]
    table = map["table"]
    for each in table["elements"]:
        if each !=None:
            single_flight = each["value"]
            if date[0] <= single_flight["date"] <= date[1] and time[0] <= single_flight["sched_dep_time"] <= time[1]:
                result["total_airports"] += 1
                if single_flight["carrier"] in airline:
                    array =airline[single_flight["carrier"]["flights"]]
                    dict_flight = {
                        "id": single_flight["id"],
                        "flight": single_flight["flight"],
                        "date programmer":single_flight["date"]+ "-" + single_flight["sched_dep_time"],
                        "origin": single_flight["origin"],
                        "dest": single_flight["dest"],
                        "distance": single_flight["air_time"]
                    }
                    al.add_last(array, dict_flight)
                    airline[single_flight["carrier"]["flights"]] = array
                    airline[single_flight["carrier"]["duration"]] += int(single_flight["air_time"])
                    airline[single_flight["carrier"]["distance"]] += int(single_flight["distance"])
                else:
                    array = al.new_list()
                    dict_flight = {
                        "id": single_flight["id"],
                        "flight": single_flight["flight"],
                        "date programmer":single_flight["date"]+ "-" + single_flight["sched_dep_time"],
                        "origin": single_flight["origin"],
                        "dest": single_flight["dest"],
                        "duration": single_flight["air_time"]
                    }
                    airline[single_flight["carrier"]["duration"]] = int(single_flight["air_time"])
                    airline[single_flight["carrier"]["distance"]] = int(single_flight["distance"])
                    al.add_last(array, dict_flight)
                    airline[single_flight["carrier"]["flights"]] = array
    for key in airline:
        total_distance = airline[key]["distance"]/ airline[key]["flights"]["size"]
        total_duration = airline[key]["duration"]/ airline[key]["flights"]["size"]
        minor = airline[key]["flights"]["elements"][0]
        for flight in airline[key]["flights"]["elements"]:
            if flight["distance"] < minor["distance"]:
                minor = flight
            elif flight["distance"] == minor["distance"]:
                if flight["date programmer"] > minor["date programmer"]:
                    minor = flight
    
        
        dict_airline = {
            "airline_code": key,
            "total_flights": airline[key]["flights"]["size"],
            "total_distance": total_distance,
            "total_duration": total_duration,
            "minor" : minor
            }
        if rbt.contains (tree, airline[key]["flights"]["size"]):
            array = rbt.get (tree, airline[key]["flights"]["size"])
            al.add_last (array, dict_airline)
            rbt.put (tree, airline[key]["flights"]["size"], array)
        else:
            array= al.new_list()
            al.add_last (array, dict_airline)
            rbt.put(tree,airline[key]["flights"]["size"], array)
    
    values = rbt.value_set(tree)
    i = 0 
    array = al.new_list()
    while i < values["size"]:
        elements = sl.get_element(values,i)
        if elements["size"] > 1:
            if elements["elements"][0]["airline_code"][0] < elements["elements"][1]["airline_code"][0]:
                al.add_last(array,elements["elements"][0])
            else:
                al.add_last(array,elements["elements"][1])
        else:
            al.add_last(array,elements["elements"][0])
    al.sub_list(array, 0 ,n)
    result["airports"] = array
    return result
    "Falta terminar el ultimo filtro que es por letra y seleccionar los n primeros y sale"
    
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
