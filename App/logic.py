import time
import os
import math
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl
from DataStructures.Map import map_linear_probing as lp
from DataStructures.Tree import red_black_tree as rbt
from DataStructures.Priority_queue import priority_queue as pq
import csv
from DataStructures.Tree import rbt_node as rb

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/Challenge-3'
# Funciones para la carga de datos
def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = {
        "flights": None,
    }
    
    catalog["flights"] = al.new_list()
    
    return catalog
    #TODO: Llama a las funciónes de creación de las estructuras de datos

def load_data(catalog):
    """
    Carga los datos del reto
    """
    flight = load_flights(catalog)
    return flight
    # TODO: Realizar la carga de datos

def load_flights(catalog):
    
    inicio = get_time()
    flight_total = 0
    
    flight_file = data_dir + "/flights_large.csv" # Aca luego de las pruebas cambiar por filename
    input_file = csv.DictReader(open(flight_file, encoding="utf-8"), delimiter=",")
    array = al.new_list()
    for flight in input_file:
        for each in flight:
            if flight[each] == "":
                flight[each] = "Unknown"
        add_flights(catalog, flight)
        flight_total += 1
        if flight["date"] != "Unknown" and flight["sched_dep_time"] != "Unknown":
            clean_return = {
                    "date": flight["date"],
                    "dep_time": flight["dep_time"],
                    "arr_time": flight["arr_time"],
                    "airline_code": flight["carrier"],
                    "airline_name": flight["name"],
                    "tailnum": flight["tailnum"],
                    "origin": flight["origin"],
                    "dest": flight["dest"],
                    "air_time": flight["air_time"],
                    "distance": flight["distance"]
                }
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
            flight_order = (key_rbt, clean_return)
            al.add_last(array, flight_order)
    def sort_criteria (a,b):
        if a[0] < b[0]:
            return False
        return True 
    array = al.merge_sort(array,sort_criteria)
    first5 = al.sub_list(array,0,4)
    last5 = al.sub_list(array, flight_total -5, flight_total -1)
    fin = get_time()
    
    return {
        "tiempo_ms": delta_time(inicio, fin),
        "total_vuelos": flight_total,
        "primeros5": first5,
        "ultimos5": last5
    }                        
def new_flight_info(id, flight, date, name, carrier, origin, dest, dep_time, arr_time, sched_dep_time, sched_arr_time, air_time, distance):
    flight_info = {
        "id": id,
        "flight": flight,
        "date": date,
        "name": name,
        "carrier": carrier,
        "origin": origin,
        "dest": dest,
        "dep_time": dep_time,
        "arr_time": arr_time,
        "sched_dep_time": sched_dep_time,
        "sched_arr_time": sched_arr_time,
        "air_time": air_time,
        "distance": distance
    }
    return flight_info

def add_flights(catalog, fligh):
    flight_map = catalog["flights"]
    t = new_flight_info(
        fligh["id"],
        fligh["flight"],
        fligh["date"],
        fligh["name"],
        fligh["carrier"],
        fligh["origin"],
        fligh["dest"],
        fligh["dep_time"],
        fligh["arr_time"],
        fligh["sched_dep_time"],
        fligh["sched_arr_time"],
        fligh["air_time"],
        fligh["distance"]
    )
    al.add_last(flight_map, t)
    return catalog 

# Funciones de consulta sobre el catálogo
def req_1(catalog, airline_code, min_delay, max_delay):
    start=get_time()
    filtered_rbt=rbt.new_map()
    filtered_no=0
    for flight in catalog["flights"]["elements"]:
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
                if rbt.contains(filtered_rbt, key):
                    value_array = rbt.get(filtered_rbt, key)
                    al.add_last(value_array, req_flight)
                    rbt.put(filtered_rbt, key, value_array)
                else:
                    array = al.new_list()
                    al.add_last(array, req_flight)
                    rbt.put(filtered_rbt, key, array)
    values = rbt.value_set(filtered_rbt)
    if values["size"] > 0:
            first = al.new_list()
            i = 0
            centinela = True
            while i < values["size"] and centinela:
                element = sl.get_element(values, i)
                if element["size"] >= 2:
                    for each in element["elements"]:
                        al.add_last(first, each)
                        if first["size"] == 5:
                            centinela = False
                else:
                    al.add_last(first, element["elements"][0])
                if first["size"] == 5:
                    centinela = False
                i += 1
            
            last = sl.sub_list(values, values["size"] -5, values["size"])
            last_cleaned = al.new_list()
            i2 = 0
            centinela = True
            while i2 < last["size"] and centinela:
                element = sl.get_element(last, i2)
                if element["size"] >= 2:
                    for each in element["elements"]:
                        al.add_last(last_cleaned, each)
                        if last_cleaned["size"] == 5:
                            centinela = False
                else:
                    al.add_last(last_cleaned, element["elements"][0])
                if last_cleaned["size"] == 5:
                    centinela = False
                i2 += 1
            fin= get_time()
            return{
                "time_ms": fin - start,
                "filtered_number": filtered_no,
                "first5": first,
            "   last5": last_cleaned}
    fin= get_time()
    return{
        "time_ms": fin - start,
        "filtered_number": filtered_no,
        "filtered_flights": al.new_list()}

def req_2(catalog, code, time):
    
    min = time[0]
    max = time[1]
    
    start = get_time()
    filtered_rbt = rbt.new_map()
    filtered_no = 0
    for i in range(catalog["flights"]["size"]):
        single_flight = catalog["flights"]["elements"][i]
        arr_time = str(single_flight["arr_time"])
        sched_arr_time = str(single_flight["sched_arr_time"])
                
        arr_time_h, arr_time_s = arr_time.split(":")
        sched_arr_time_h, sched_arr_time_s = sched_arr_time.split(":")
                
        arr_time_minutes = int(arr_time_h) *60 + int(arr_time_s)
        sched_arr_time_minutes = int(sched_arr_time_h) *60 + int(sched_arr_time_s)
                
        delay = arr_time_minutes - sched_arr_time_minutes
        if delay < -720:
            delay += 1440
        elif delay > 720:
            delay -= 1440
                    
        if (single_flight["dest"] == code) and (min <= delay <= max):   
            filtered_no += 1
            flight_date = str(single_flight["date"])
            y, m ,d = flight_date.split("-")
            date_int = int(y) * 10000 + int(m)*100 + int(d)
            arr_int = int(arr_time_h)* 100 + int(arr_time_s)
            key = delay * 10000000000000 + date_int * 100000000 + arr_int * 10000 + int(single_flight["id"])
            req_flight = {
                    "id": single_flight["id"],
                    "flight": single_flight["flight"],
                    "date": single_flight["date"],
                    "airline_name": single_flight["name"],
                    "airline_code": single_flight["carrier"],
                    "origin": single_flight["origin"],
                    "dest": single_flight["dest"],
                    "early_minutes": delay
                    }
            if rbt.contains(filtered_rbt, key):
                value_array = rbt.get(filtered_rbt, key)
                al.add_last(value_array, req_flight)
                rbt.put(filtered_rbt, key, value_array)
            else:
                array = al.new_list()
                al.add_last(array, req_flight)
                rbt.put(filtered_rbt, key, array)
                    
    values = rbt.value_set(filtered_rbt)
    if values["size"] > 0:
            first = al.new_list()
            i = 0
            centinela = True
            while i < values["size"] and centinela:
                element = sl.get_element(values, i)
                if element["size"] >= 2:
                    for each in element["elements"]:
                        al.add_last(first, each)
                        if first["size"] == 5:
                            centinela = False
                else:
                    al.add_last(first, element["elements"][0])
                if first["size"] == 5:
                    centinela = False
                i += 1
            
            last = sl.sub_list(values, values["size"] -5, values["size"])
            last_cleaned = al.new_list()
            i2 = 0
            centinela = True
            while i2 < last["size"] and centinela:
                element = sl.get_element(last, i2)
                if element["size"] >= 2:
                    for each in element["elements"]:
                        al.add_last(last_cleaned, each)
                        if last_cleaned["size"] == 5:
                            centinela = False
                else:
                    al.add_last(last_cleaned, element["elements"][0])
                if last_cleaned["size"] == 5:
                    centinela = False
                i2 += 1
            fin= get_time()
            return{
                "time_ms": fin - start,
                "filtered_number": filtered_no,
                "first5": first,
                "last5": last_cleaned}
    fin= get_time()
    return{
        "time_ms": fin - start,
        "filtered_number": filtered_no,
        "filtered_flights": al.new_list()}
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
    
    for i in range(0,al.size(catalog["flights"])):
        single_flight = al.get_element(catalog["flights"], i)
        if single_flight["carrier"].strip().upper() == airline and single_flight["dest"].strip().upper() == code_airport and distance[0] <=  int(single_flight["distance"]) <= distance[1]:
            result["total_flights"] += 1 
            if rbt.contains(tree, int(single_flight["distance"])):
                
                value_array = rbt.get(tree, int(single_flight["distance"]))
                dict_flight = {
                    "id": single_flight["id"],
                    "flight": single_flight["flight"],
                    "date": single_flight["date"],
                    "airline_name": single_flight["name"],
                    "airline_code": single_flight["carrier"],
                    "origin": single_flight["origin"],
                    "dest": single_flight["dest"],
                    "distance": int(single_flight["distance"])
                        }
                al.add_last(value_array, dict_flight)
                rbt.put(tree, int(single_flight["distance"]),value_array)
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
                    "distance": int(single_flight["distance"]),
                        }
                al.add_last(array,dict_flight)
                rbt.put(tree, int(single_flight["distance"]),array)
    
    def default_criteria (flight1, flight2):
        date_str = flight1["date"]              
        date_parts = date_str.split("-")    
        year = int(date_parts[0])
        month = int(date_parts[1])
        day = int(date_parts[2])
        date_int = year * 10000 + month * 100 + day
        arr = al.get_element(catalog["flights"], int(flight1["id"]))
        time_str = arr["arr_time"]
        partes = time_str.split(":")
        hh = int(partes[0])
        mm = int(partes[1])
        sched_int = hh * 100 + mm
        first = date_int * 10000 + sched_int
        date_str2 = flight2["date"]
        date_parts2 = date_str2.split("-")
        year2 = int(date_parts2[0])
        month2 = int(date_parts2[1])
        day2 = int(date_parts2[2])
        date_int2 = year2 * 10000 + month2 * 100 + day2
        arr2= al.get_element(catalog["flights"], int(flight2["id"]))
        time_str2 = arr2["arr_time"]
        partes2 = time_str2.split(":")
        hh2 = int(partes2[0])
        mm2 = int(partes2[1])
        sched_int2 = hh2 * 100 + mm2
        first2 = date_int2 * 10000 + sched_int2
        if first < first2:
            return True
        else:
            return False

    values = rbt.value_set(tree)

    if values["size"] > 0:
        first = al.new_list()
        i = 0
        centinela = True
        while i < values["size"] and first["size"] < 5 and centinela:
            element = sl.get_element(values, i)
            if element["size"] >= 2:
                for each in element["elements"]:
                    al.add_last(first, each)
                    if first["size"] == 5:
                        centinela = False
            else:
                al.add_last(first, element["elements"][0])
            i += 1


    last = sl.sub_list(values, values["size"] - 5, values["size"])
    last_cleaned = al.new_list()
    i2 = 0
    centinela = True
    while i2 < last["size"] and last_cleaned["size"] < 5 and centinela:
        element = sl.get_element(last, i2)
        if element["size"] >= 2:
            for each in element["elements"]:
                al.add_last(last_cleaned, each)
                if last_cleaned["size"] == 5:
                    centinela = False
        else:
            al.add_last(last_cleaned, element["elements"][0])
        i2 += 1

        result["first"] = first
        result["last"] = last_cleaned
    else:
        result["first"] = al.new_list()
        result["last"] = al.new_list()
    final = get_time()
    result["time"] = delta_time( result["time"], final)
    return result
    # TODO: Modificar el requerimiento 3

def req_4(catalog,date,time,n):
    """
    Retorna el resultado del requerimiento 4
    """
    result = {
        "time": get_time(),
        "total_airports": 0,
        "airports": al.new_list()
    }
    airline = {}
    tree = rbt.new_map()
    for single_flight in catalog["flights"]["elements"]:
            if single_flight["date"] != "Unknown" and single_flight["sched_dep_time"] != "Unknown":
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
                        airline[single_flight["carrier"]["distance"]] += float(single_flight["distance"])
                    else:
                        array = al.new_list()
                        dict_flight = {
                            "id": single_flight["id"],
                            "flight": single_flight["flight"],
                            "date_programmer":single_flight["date"]+ "-" + single_flight["sched_dep_time"],
                            "origin": single_flight["origin"],
                            "dest": single_flight["dest"],
                            "duration": single_flight["air_time"]
                        }
                        airline[single_flight["carrier"]["duration"]] = int(single_flight["air_time"])
                        airline[single_flight["carrier"]["distance"]] = float(single_flight["distance"])
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
                if flight["date_programmer"] > minor["date_programmer"]:
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
    # TODO: Modificar el requerimiento 4

def req_5(catalog,dest_code,date,N):
    start=get_time()
    airlines_info={}
    date_min = date[0] 
    date_max = date[1]
    for flight in catalog["flights"]["elements"]:
        if flight is not None:
            if (flight["dest"]!= "" and flight["arr_time"]!="" and flight["sched_arr_time"]!="" and 
                flight["date"]!= "" and flight["carrier"]!= ""):
                if flight["dest"]== dest_code:
                    flight_date= str(flight["date"])
                    y, m, d= flight_date.split("-")
                    date_int= int(y)* 10000 + int(m)* 100 + int(d)
                    y1, m1, d1= date_min.split("-")
                    y2, m2, d2= date_max.split("-")
                    date_min_int= int(y1)*10000+ int(m1)*100+ int(d1)
                    date_max_int= int(y2)*10000+ int(m2)*100+ int(d2)
                    if date_min_int<= date_int<= date_max_int:
                        arr_time= str(flight["arr_time"])
                        sched_arr_time=str(flight["sched_arr_time"])
                        arr_h, arr_m= arr_time.split(":")
                        sched_h, sched_m=sched_arr_time.split(":")
                        arr_minutes= int(arr_h)*60+ int(arr_m)
                        sched_minutes= int(sched_h)*60 + int(sched_m)
                        diff= arr_minutes- sched_minutes
                        if diff<-720:
                            diff+=1440
                        elif diff>720:
                            diff-=1440
                        carrier= flight["carrier"]
                        if carrier not in airlines_info:
                            airlines_info[carrier]={
                                "flights":sl.new_list(),
                                "total_diff":0,
                                "total_flights":0,
                                "total_distance":0,
                                "total_duration":0}
                        sl.add_last(airlines_info[carrier]["flights"],flight)
                        airlines_info[carrier]["total_diff"]+= diff
                        airlines_info[carrier]["total_distance"]+= int(flight["distance"]) if flight["distance"]!= "" else 0
                        airlines_info[carrier]["total_duration"]+= int(flight["air_time"]) if flight["air_time"]!= "" else 0
                        airlines_info[carrier]["total_flights"]+= 1
    punctual_rbt= rbt.new_map()
    carrier_list = sl.new_list()
    for carrier in airlines_info:
        pair = {
            "carrier": carrier,
            "info": airlines_info[carrier]
        }
        sl.add_last(carrier_list, pair)
    i = 0
    total_pairs = carrier_list["size"]
    while i < total_pairs:
        element = sl.get_element(carrier_list, i)
        carrier = element["carrier"]
        info = element["info"]
        total_f= info["total_flights"]
        if total_f>0:
            avg_diff=info["total_diff"] / total_f
            avg_distance=info["total_distance"]/ total_f
            avg_duration=info["total_duration"]/ total_f
            flights_list=info["flights"]
            max_dist=-1
            longest_flight= None
            j = 0
            size_f = flights_list["size"]
            while j < size_f:
                node = flights_list["elements"][j]
                if node is not None and node["value"]["distance"] != "":
                    dist = int(node["value"]["distance"])
                    if dist > max_dist:
                        max_dist = dist
                        longest_flight = node["value"]
                j +=1
            key = avg_diff* 1000+ord(carrier[0])*10+ord(carrier[-1])
            data={
                "airline_code":carrier,
                "avg_diff":avg_diff,
                "avg_distance":avg_distance,
                "avg_duration":avg_duration,
                "total_flights":total_f,
                "longest_flight":{
                    "id": longest_flight["id"],
                    "flight": longest_flight["flight"],
                    "date": longest_flight["date"],
                    "arr_time": longest_flight["arr_time"],
                    "origin": longest_flight["origin"],
                    "dest": longest_flight["dest"],
                    "duration": longest_flight["air_time"]
                }
            }
            rbt.put(punctual_rbt,key,data)
        i+=1
    ordered=rbt.value_set(punctual_rbt)
    total=ordered["size"]
    result_list=sl.new_list()
    i=0
    while i< total and i< N:
        element= sl.get_element(ordered, i)
        sl.add_last(result_list, element)
        i+= 1
    fin= get_time()
    return{
        "time_ms":fin-start,
        "total_airlines":N if N < total else total,
        "most_punctual":result_list}

def req_6(catalog, date, distance, m):
    """
    Retorna el resultado del requerimiento 6
    """
    start = get_time()
    airline_rbt = rbt.new_map()
    fech_min = date[0]
    fech_max = date[1]
    dist_min = distance[0]
    dist_max = distance[1]
    
    for flight in catalog["flights"]["elements"]:
        if flight is not None:
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
