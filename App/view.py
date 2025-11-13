import sys
import tabulate
from App import logic as lg
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl

data_structure = None
def new_logic(data_structure):
    """
        Se crea una instancia del controlador
    """
    data = lg.new_logic(data_structure)
    return data 
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    pass

def print_menu():
    print("Bienvenido")
    print("0- Cargar información")
    print("1- Ejecutar Requerimiento 1")
    print("2- Ejecutar Requerimiento 2")
    print("3- Ejecutar Requerimiento 3")
    print("4- Ejecutar Requerimiento 4")
    print("5- Ejecutar Requerimiento 5")
    print("6- Ejecutar Requerimiento 6")
    print("7- Salir")

def load_data(control):
    """
    Carga los datos
    """
    answer = lg.load_data(control)
    print(answer)
    #TODO: Realizar la carga de datos
    pass


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    airline_code = input("Código de la aerolínea a analizar: ").upper()
    min_delay = int(input("Valor minimo de retraso en minutos: "))
    max_delay = int(input("Valor máximo de retraso en minutos: "))
    answer = lg.req_1(control, airline_code, min_delay, max_delay) # Corregir en la funcion en logic Sebastian
    
    print("\n=== RESULTADO REQ 1 ===")
    resumen = [
    ["Tiempo de ejecución (ms)", f"{answer['time_ms']}"],
    ["Número total de vuelos filtrados", answer["filtered_number"]],]
    print(tabulate(resumen,headers=["Descripción", "Valor"],tablefmt="grid"))
    
    first = []
    for i in range(answer["first5"]["size"]):
        flight = sl.get_element(answer["first5"], i)
        first.append([
            flight["id"],
            flight["flight"],
            flight["date"],
            flight["airline_name"],
            flight["airline_code"],
            flight["origin"],
            flight["dest"],
            flight["distance"],
        ])
    titulo = f"Primeros {len(first)} vuelos encontrados"
    print(f"\n============ {"titulo"} ============")
    print(tabulate(first,headers=["ID vuelo","Código vuelo","Fecha","Aerolínea","Carrier","Origen","Destino","Distancia (mi)",],tablefmt="grid",showindex=range(1, first["size"] + 1)))
    
    last = []
    for i in range(answer["last5"]["size"]):
        flight = sl.get_element(answer["last5"], i)
        last.append([
            flight["id"],
            flight["flight"],
            flight["date"],
            flight["airline_name"],
            flight["airline_code"],
            flight["origin"],
            flight["dest"],
            flight["distance"],
        ])
    titulo = f"Últimos {len(last)} vuelos encontrados"
    print(f"\n============ {"titulo"} ============")
    print(tabulate(last,headers=["ID vuelo","Código vuelo","Fecha","Aerolínea","Carrier","Origen","Destino","Distancia (mi)",],tablefmt="grid",showindex=range(1, last["size"] + 1)))
    print (answer)
    
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    airline_code = input("Código de la aerolínea a analizar: ").upper()
    min = int(input("Valor minimo en minutos de anticipo en la llegada: "))
    max =  int(input("Valor máximo en minutos de anticipo en la llegada: "))
    answer = lg.req_2(control, airline_code, min, max) # Corregir en la funcion en logic  
    print("\n=== RESULTADO REQ 2 ===")
    resumen = [
    ["Tiempo de ejecución (ms)", f"{answer['time_ms']}"],
    ["Número total de vuelos filtrados", answer["filtered_number"]],]
    print(tabulate(resumen,headers=["Descripción", "Valor"],tablefmt="grid"))
    
    first = []
    for i in range(answer["first5"]["size"]):
        flight = sl.get_element(answer["first5"], i)
        first.append([
            flight["id"],
            flight["flight"],
            flight["date"],
            flight["airline_name"],
            flight["airline_code"],
            flight["origin"],
            flight["dest"],
            flight["distance"],
        ])
    titulo = f"Primeros {len(first)} vuelos encontrados"
    print(f"\n============ {"titulo"} ============")
    print(tabulate(first,headers=["ID vuelo","Código vuelo","Fecha","Aerolínea","Carrier","Origen","Destino","Distancia (mi)",],tablefmt="grid",showindex=range(1, first["size"] + 1)))
    
    last = []
    for i in range(answer["last5"]["size"]):
        flight = sl.get_element(answer["last5"], i)
        last.append([
            flight["id"],
            flight["flight"],
            flight["date"],
            flight["airline_name"],
            flight["airline_code"],
            flight["origin"],
            flight["dest"],
            flight["distance"],
        ])
    titulo = f"Últimos {len(last)} vuelos encontrados"
    print(f"\n============ {"titulo"} ============")
    print(tabulate(last,headers=["ID vuelo","Código vuelo","Fecha","Aerolínea","Carrier","Origen","Destino","Distancia (mi)",],tablefmt="grid",showindex=range(1, last["size"] + 1)))
    
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    airline_code = input("Código de la aerolínea a analizar: ").upper()
    airline = input("Nombre de la aerolínea a analizar: ").upper()
    min_distance = int(input("Valor minimo de distancia en millas: "))
    max_distance = int(input("Valor máximo de distancia en millas: "))
    answer = lg.req_3(control, airline_code, airline, (min_distance,max_distance))
    
    print("\n=== RESULTADO REQ 3 ===")
    resumen = [
    ["Tiempo de ejecución (ms)", f"{answer['time']}"],
    ["Número total de vuelos filtrados", answer["total_flights"]],]
    print(tabulate(resumen,headers=["Descripción", "Valor"],tablefmt="grid"))
    
    first = []
    for i in range(answer["first"]["size"]):
        flight = al.get_element(answer["first"], i)
        first.append([
            flight["id"],
            flight["flight"],
            flight["date"],
            flight["airline_name"],
            flight["airline_code"],
            flight["origin"],
            flight["dest"],
            flight["distance"],
        ])
    titulo = f"Primeros {len(first)} vuelos encontrados"
    print(f"\n============ {"titulo"} ============")
    print(tabulate(first,headers=["ID vuelo","Código vuelo","Fecha","Aerolínea","Carrier","Origen","Destino","Distancia (mi)",],tablefmt="grid",showindex=range(1, first["size"] + 1)))
    
    last = []
    for i in range(answer["last"]["size"]):
        flight = al.get_element(answer["last"], i)
        last.append([
            flight["id"],
            flight["flight"],
            flight["date"],
            flight["airline_name"],
            flight["airline_code"],
            flight["origin"],
            flight["dest"],
            flight["distance"],
        ])
    titulo = f"Últimos {len(last)} vuelos encontrados"
    print(f"\n============ {"titulo"} ============")
    print(tabulate(last,headers=["ID vuelo","Código vuelo","Fecha","Aerolínea","Carrier","Origen","Destino","Distancia (mi)",],tablefmt="grid",showindex=range(1, last["size"] + 1)))
    
    
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    date_initial = input("Fecha inicial (YYYY-MM-DD): ")
    date_final = input("Fecha final (YYYY-MM-DD): ")
    time_initial = input("Hora minima de la salida programada (HH:MM): ")
    time_final = input("Hora maxima de la salida programada (HH:MM): ")
    n = int(input("Número de aerolineas con mayor vuelos: "))
    answer = lg.req_4(control, (date_initial,date_final), (time_initial, time_final), n)
    print("\n=== RESULTADO REQ 4 ===")
    resumen = [
    ["Tiempo de ejecución (ms)", f"{answer['time']}"],
    ["Número total de vuelos filtrados", answer["total_airports"]],]
    print(tabulate(resumen,headers=["Descripción", "Valor"],tablefmt="grid"))
    
    first = []
    for i in range(answer["airports"]["size"]):
        flight = al.get_element(answer["airports"], i)
        first.append([
            flight["id"],
            flight["flight"],
            flight["date_programmer"],
            flight["origin"],
            flight["dest"],
            flight["duration"],
        ])
    titulo = f"Primeros {len(first)} aeropuertos encontrados"
    print(f"\n============ {"titulo"} ============")
    print(tabulate(first,headers=["ID vuelo","Código vuelo","Fecha programada","Origen","Destino","Duracion (min)",],tablefmt="grid",showindex=range(1, first["size"] + 1)))
    
    
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    date_initial = input("Fecha inicial (YYYY-MM-DD): ")
    date_final = input("Fecha final (YYYY-MM-DD): ")
    airport_code = input("Codigo del aeropuerto de destino: ").upper()
    n = int(input("Número de aerolineas con mayor vuelos: "))
    answer = lg.req_5(control, (date_initial,date_final), airport_code, n)
    
    print("\n=== RESULTADO REQ 5 ===")
    resumen = [
    ["Tiempo de ejecución (ms)", f"{answer['time_ms']}"],
    ["Número total de vuelos filtrados", answer["total_airlines"]],]
    print(tabulate(resumen,headers=["Descripción", "Valor"],tablefmt="grid"))
    
    first = []
    for i in range(answer["most_punctual"]["size"]):
        flight = sl.get_element(answer["most_punctual"], i)
        first.append([
            flight["airline_code"],
            flight["avg_diff"],
            flight["avg_distance"],
            flight["avg_duration"],
            flight["total_flights"],
            flight["longest_flight"],
        ])
    titulo = f"Primeros {len(first)} aeropuertos encontrados"
    print(f"\n============ {"titulo"} ============")
    print(tabulate(first,headers=["ID vuelo","Código vuelo","Fecha programada","Origen","Destino","Duracion (min)",],tablefmt="grid",showindex=range(1, first["size"] + 1)))
    #Modifica los titulos de las columnas segun los datos a mostrar 
    
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    date_initial = input("Fecha inicial (YYYY-MM-DD): ")
    date_final = input("Fecha final (YYYY-MM-DD): ")
    min_distance = int(input("Valor minimo de distancia en millas: "))
    max_distance = int(input("Valor máximo de distancia en millas: "))
    m = int(input("Número de aerolineas con mayor vuelos: "))
    answer = lg.req_6(control, (date_initial,date_final), (min_distance, max_distance), m)
    print("\n=== RESULTADO REQ 6 ===")
    resumen = [
    ["Tiempo de ejecución (ms)", f"{answer['time_ms']}"],
    ["Número total de vuelos filtrados", answer["total_airlines"]],]
    print(tabulate(resumen,headers=["Descripción", "Valor"],tablefmt="grid"))
    
    first = []
    for i in range(answer["most_punctual"]["size"]):
        flight = sl.get_element(answer["most_punctual"], i)
        first.append([
            flight["airline"],
            flight["count"],
            flight["avg"],
            flight["dev"],
            flight["closest"],
        ])
        
    titulo = f"Primeros {len(first)} aeropuertos encontrados"
    print(f"\n============ {"titulo"} ============")
    print(tabulate(first,headers=["ID vuelo","Código vuelo","Fecha programada","Origen","Destino","Duracion (min)",],tablefmt="grid",showindex=range(1, first["size"] + 1)))
    #Modifica los titulos de las columnas segun los datos a mostrar 
    
    
    # TODO: Imprimir el resultado del requerimiento 6
    pass

# Se crea la lógica asociado a la vista
control = new_logic(data_structure)

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 0:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 1:
            print_req_1(control)

        elif int(inputs) == 2:
            print_req_2(control)

        elif int(inputs) == 3:
            print_req_3(control)

        elif int(inputs) == 4:
            print_req_4(control)

        elif int(inputs) == 5:
            print_req_5(control)

        elif int(inputs) == 5:
            print_req_6(control)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
