import time
import os
from DataStructures.List import single_linked_list as sl
from DataStructures.Map import map_linear_probing as lp
from DataStructures.Tree import red_black_tree as rbt
from DataStructures.Tree import rbt_node as rn
import csv


data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/Challenge-3'

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    analyzer = {
        "flights": None,
        "flights_rbt": None
    }
    analyzer["flights"] = lp.new_map(304000, 0.7, None)
    analyzer["flights_rbt"] = rbt.new_map()
    return analyzer
    #TODO: Llama a las funciónes de creación de las estructuras de datos

# Funciones para la carga de datos
    
def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    pass

def load_flights(analyzer):
    
    inicio = get_time()
    flight_total = 0
    flights_map = analyzer["flights"]
    flights_rbt = analyzer["flights_rbt"]
    tree = rbt.new_map()
    
    flight_file = data_dir + "/flights_small.csv"
    input_file = csv.DictReader(open(flight_file, encoding="utf-8", delimeter=","))
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
        
    i2= 0
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
    # Falta eliminar las llaves que no estan pidiendo en el requerimiemnto            
        
def add_flights(analyzer, fligh):
    flight_map = analyzer["flights"]
    key = flight_map["id"]
    lp.put(flight_map, key, fligh)
    return analyzer    
    
    
# Funciones de consulta sobre el catálogo


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


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

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


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
