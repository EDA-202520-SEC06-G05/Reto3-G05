import sys
from tabulate import tabulate
from App import logic as lg
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl


def new_logic():
    """
        Se crea una instancia del controlador
    """
    data = lg.new_logic()
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
    
    #TODO: Realizar la carga de datos
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    airline_code = input("Código de la aerolínea a analizar: ").upper()
    min_delay = int(input("Valor minimo de retraso en minutos: "))
    max_delay = int(input("Valor máximo de retraso en minutos: "))
    answer = lg.req_1(control, airline_code, min_delay, max_delay)
    print("\n=== RESULTADO REQ 1 ===")

    resumen = [
    ["Tiempo de ejecución (ms)", f"{answer['time_ms']}"],
    ["Número total de vuelos filtrados", answer["filtered_number"]],
]
    print(tabulate(resumen, headers=["Descripción", "Valor"], tablefmt="grid"))

    first = []
    first_list = answer["first5"]

    for i in range(al.size(first_list)):
        flight = al.get_element(first_list, i)
        first.append([
            flight["id"],
            flight["flight"],
            flight["date"],
            flight["airline_name"],
            flight["airline_code"],
            flight["origin"],
            flight["dest"],
            flight["delay_minutes"],
        ])

    titulo_first = f"Primeros {len(first)} vuelos encontrados"
    print(f"\n============ {titulo_first} ============\n")

    print(
        tabulate(
            first,
            headers=[
                "ID vuelo",
                "Código vuelo",
                "Fecha",
                "Aerolínea",
                "Carrier",
                "Origen",
                "Destino",
                "Retraso (min)"
        ],
            tablefmt="grid",
            showindex=range(1, len(first) + 1)
    )
)


    if "last5" in answer:
        last = []
        last_list = answer["last5"]

        for i in range(al.size(last_list)):
            flight = al.get_element(last_list, i)
            last.append([
                flight["id"],
                flight["flight"],
                flight["date"],
                flight["airline_name"],
                flight["airline_code"],
                flight["origin"],
                flight["dest"],
                flight["delay_minutes"],
        ])

    titulo_last = f"Últimos {len(last)} vuelos encontrados"
    print(f"\n============ {titulo_last} ============\n")

    print(
        tabulate(
            last,
            headers=[
                "ID vuelo",
                "Código vuelo",
                "Fecha",
                "Aerolínea",
                "Carrier",
                "Origen",
                "Destino",
                "Retraso (min)"
            ],
            tablefmt="grid",
            showindex=range(1, len(last) + 1)
        )
    )
    
    
    
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    airline_code = input("Código de la aerolínea a analizar: ").upper()
    min = int(input("Valor minimo en minutos de anticipo en la llegada: "))
    max =  int(input("Valor máximo en minutos de anticipo en la llegada: "))
    answer = lg.req_2(control, airline_code, (min, max))
    print("\n=== RESULTADO REQ 2 ===")
    resumen = [
    ["Tiempo de ejecución (ms)", f"{answer['time_ms']}"],
    ["Número total de vuelos filtrados", answer["filtered_number"]],]
    print(tabulate(resumen, headers=["Descripción", "Valor"], tablefmt="grid"))

    first = []
    for i in range(answer["first5"]["size"]):
        flight = al.get_element(answer["first5"], i)
        first.append([
        flight["id"],
        flight["flight"],
        flight["date"],
        flight["airline_name"],
        flight["airline_code"],
        flight["origin"],
        flight["dest"],
        flight["early_minutes"],
    ])

    titulo_first = f"Primeros {len(first)} vuelos encontrados"
    print(f"\n============ {titulo_first} ============")

    print(tabulate(
        first,
        headers=[
        "ID vuelo", "Código vuelo", "Fecha",
        "Aerolínea", "Carrier", "Origen",
        "Destino", "Distancia (mi)"
        ],
        tablefmt="grid",
        showindex=range(1, len(first) + 1)
))

    last = []
    for i in range(answer["last5"]["size"]):
        flight = al.get_element(answer["last5"], i)
        last.append([
        flight["id"],
        flight["flight"],
        flight["date"],
        flight["airline_name"],
        flight["airline_code"],
        flight["origin"],
        flight["dest"],
        flight["early_minutes"],
    ])

    titulo_last = f"Últimos {len(last)} vuelos encontrados"
    print(f"\n============ {titulo_last} ============")

    print(tabulate(
        last,
        headers=[
        "ID vuelo", "Código vuelo", "Fecha",
        "Aerolínea", "Carrier", "Origen",
        "Destino", "Distancia (mi)"
        ],
        tablefmt="grid",
        showindex=range(1, len(last) + 1)
))
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    airline_code = input("Código de la aerolínea a analizar: ").upper()
    airline = input("Codigo del areopuerto: ").upper()
    min_distance = int(input("Valor minimo de distancia en millas: "))
    max_distance = int(input("Valor máximo de distancia en millas: "))
    answer = lg.req_3(control, airline_code, airline, (min_distance, max_distance))
    print("\n=== RESULTADO REQ 3 ===")
    resumen = [
    ["Tiempo de ejecución (ms)", f"{answer['time']}"],
    ["Número total de vuelos filtrados", answer["total_flights"]],
]
    print(tabulate(resumen, headers=["Descripción", "Valor"], tablefmt="grid"))

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

    titulo_first = f"Primeros {len(first)} vuelos encontrados"
    print(f"\n============ {titulo_first} ============")
    print(
        tabulate(
        first,
        headers=[
            "ID vuelo",
            "Código vuelo",
            "Fecha",
            "Aerolínea",
            "Carrier",
            "Origen",
            "Destino",
            "Distancia (mi)",
        ],
        tablefmt="grid",
        showindex=range(1, len(first) + 1)
    )
)

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

    titulo_last = f"Últimos {len(last)} vuelos encontrados"
    print(f"\n============ {titulo_last} ============")
    print(
    tabulate(
        last,
        headers=[
            "ID vuelo",
            "Código vuelo",
            "Fecha",
            "Aerolínea",
            "Carrier",
            "Origen",
            "Destino",
            "Distancia (mi)",
        ],
        tablefmt="grid",
        showindex=range(1, len(last) + 1)
    )
)
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
    answer = lg.req_4(control, (date_initial, date_final), (time_initial, time_final), n)
    print("\n=== RESULTADO REQ 4 ===")

    resumen = [
    ["Tiempo de ejecución (ms)", f"{answer['time']}"],
    ["Número total de vuelos filtrados", answer["total_airports"]],
]
    print(tabulate(resumen, headers=["Descripción", "Valor"], tablefmt="grid"))

    first = []
    airports_list = answer["airports"]

    for i in range(al.size(airports_list)):
        flight = al.get_element(airports_list, i)
        first.append([
            flight["id"],
            flight["flight"],
            flight["date_programmer"],
            flight["origin"],
            flight["dest"],
            flight["duration"],
    ])

    titulo = f"Primeros {len(first)} aeropuertos encontrados"
    print(f"\n============ {titulo} ============")

    print(
        tabulate(
            first,
            headers=[
                "ID vuelo",
                "Código vuelo",
                "Fecha programada",
                "Origen",
                "Destino",
                "Duración (min)",
        ],
            tablefmt="grid",
            showindex=range(1, len(first) + 1),
    )
)
    
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
    ["Número total de aerolíneas filtradas", answer["total_airlines"]],
]
    print(tabulate(resumen, headers=["Descripción", "Valor"], tablefmt="grid"))

    first = []
    airlines_list = answer["most_punctual"]


    for i in range(sl.size(airlines_list)):
        airline = sl.get_element(airlines_list, i)
        first.append([
            airline["airline_code"],
            airline["avg_diff"],
            airline["avg_distance"],
            airline["avg_duration"],
            airline["total_flights"],
            airline["longest_flight"],
    ])

    titulo = f"Primeros {len(first)} aerolíneas más puntuales"
    print(f"\n============ {titulo} ============")

    print(
        tabulate(
            first,
            headers=[
                "Código aerolínea",
                "Retraso promedio (min)",
                "Distancia promedio (mi)",
                "Duración promedio (min)",
                "Total de vuelos",
                "Vuelo más largo (mi)",
        ],
        tablefmt="grid",
        showindex=range(1, len(first) + 1),
    )
)

    
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
    ["Número total de aerolíneas analizadas", answer["total_airlines"]],
    ]
    print(tabulate(resumen, headers=["Descripción", "Valor"], tablefmt="grid"))

    first = []
    airlines_list = answer["most_punctual"]


    for i in range(sl.size(airlines_list)):
        airline = sl.get_element(airlines_list, i)
        first.append([
            airline["airline"],   
            airline["count"],     
            airline["avg"],       
            airline["dev"],       
            airline["closest"],   
        ])

    titulo = f"Primeros {len(first)} aerolíneas encontradas"
    print(f"\n============ {titulo} ============")

    print(
        tabulate(
            first,
            headers=[
            "Aerolínea",
            "Cantidad de vuelos",
            "Promedio",
            "Desviación estándar",
            "Vuelo más cercano",
            ],
            tablefmt="grid",
            showindex=range(1, len(first) + 1),
    )
)
    
    
    # TODO: Imprimir el resultado del requerimiento 6
    pass

# Se crea la lógica asociado a la vista
control = new_logic()

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
