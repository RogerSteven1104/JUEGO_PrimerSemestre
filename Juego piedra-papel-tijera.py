import random  # Importamos la librería random para generar elecciones aleatorias

# Función que valida que el usuario ingrese una opción válida entre las permitidas
def obtener_opcion_valida(mensaje, opciones):
    while True:
        opcion = input(mensaje).strip().upper()
        if opcion in opciones:
            return opcion
        print("\nOpción no válida. Intenta de nuevo.")

# Función para mostrar estadísticas de la última partida
def mostrar_estadisticas(historial, nombres):
    if not historial:
        print("\nNo hay estadísticas recientes.")
        return

    print("\nResumen:")
    print(f"Numero de partidas realizadas: {len(historial)}")
    ganados = {nombres[0]: 0, nombres[1]: 0}
    empates = 0

    for i, resultado in enumerate(historial):
        print(f"Partida {i+1}: {resultado}")
        if "empató" in resultado:
            empates += 1
        elif nombres[0] in resultado and "ganó" in resultado:
            ganados[nombres[0]] += 1
        elif nombres[1] in resultado and "ganó" in resultado:
            ganados[nombres[1]] += 1

    print("\nEstadísticas:")
    print(f"{nombres[0]}: ganó {ganados[nombres[0]]}, perdió {ganados[nombres[1]]}, empató {empates}")
    print(f"{nombres[1]}: ganó {ganados[nombres[1]]}, perdió {ganados[nombres[0]]}, empató {empates}")

# Función que ejecuta una sola partida entre dos jugadores
def jugar_partida(j1, j2, modo):
    opciones = ["PIEDRA", "PAPEL", "TIJERA"]
    jugador1 = obtener_opcion_valida(f"{j1}, elige PIEDRA, PAPEL o TIJERA: ", opciones)
    if modo == "PC":
        jugador2 = random.choice(opciones)
        print(f"El PC escogió: {jugador2}")
    else:
        print("\nTurno del segundo jugador.")
        jugador2 = obtener_opcion_valida(f"{j2}, elige PIEDRA, PAPEL o TIJERA: ", opciones)

    if jugador1 == jugador2:
        print("\nEmpate!")
        return f"{j1} empató - {j2} empató"
    elif (jugador1 == "PIEDRA" and jugador2 == "TIJERA") or \
         (jugador1 == "PAPEL" and jugador2 == "PIEDRA") or \
         (jugador1 == "TIJERA" and jugador2 == "PAPEL"):
        print(f"\n¡{j1} ganó!")
        return f"{j1} ganó - {j2} perdió"
    else:
        print(f"\n¡{j2} ganó!")
        return f"{j1} perdió - {j2} ganó"
    
# Función que ejecuta varias partidas seguidas entre dos jugadores
def jugar_modo(nombre1, nombre2, modo):
    historial = []
    while True:
        try:
            n = int(input("¿Cuántas partidas desea jugar?: "))
            break
        except ValueError:
            print("Ingrese un número válido.")
    for _ in range(n):
        resultado = jugar_partida(nombre1, nombre2, modo)
        historial.append(resultado)
    return historial

historial_ultima = []
nombres_ultima = ["", ""]

# Bucle principal del programa
while True:
    print("\nMENÚ PRINCIPAL")
    print("1. Jugar")
    print("2. Ver estadísticas de la última partida")
    print("3. Reglas del juego")
    print("4. Salir")
    opcion_menu = input("Seleccione una opción: ")

    if opcion_menu == "1":
        print("\n1. Jugar contra la PC")
        print("2. Multijugador")
        sub_opcion = input("Seleccione el modo de juego: ")

        if sub_opcion == "1":
            nombre_jugador = input("Ingresa tu nombre: ").capitalize()
            historial_ultima = jugar_modo(nombre_jugador, "PC", "PC")
            nombres_ultima = [nombre_jugador, "PC"]
        elif sub_opcion == "2":
            nombre1 = input("Nombre del Jugador 1: ").capitalize()
            nombre2 = input("Nombre del Jugador 2: ").capitalize()
            historial_ultima = jugar_modo(nombre1, nombre2, "MULTI")
            nombres_ultima = [nombre1, nombre2]
        else:
            print("Opción inválida. Volviendo al menú principal.")

    elif opcion_menu == "2":
        if historial_ultima:
            mostrar_estadisticas(historial_ultima, nombres_ultima)
        else:
            print("\nNo hay estadísticas recientes para mostrar.")

    elif opcion_menu == "3":
        print("\nReglas del juego:")
        print("- Piedra: gana a Tijera, la piedra aplasta la tijera")
        print("- Papel: gana a Piedra, el papel envuelve la piedra")
        print("- Tijera: gana a Papel, la tijera corta el papel")
        print("- Si ambos jugadores eligen la misma opción, se repite la ronda hasta que haya un ganador.")

    elif opcion_menu == "4":
        print("\n¡Hasta la próxima!")
        break
    else:
        print("\nOpción no válida. Intente nuevamente.")


    
        

    
