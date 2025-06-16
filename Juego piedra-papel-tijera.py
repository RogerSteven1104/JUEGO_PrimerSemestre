import random                                          #Necesario para que la computadora elija las opciones / Consultar Ing.

nombre = (input("Ingresa tu nombre: ")).capitalize()
print("\nHola, " + nombre + "! Bienvenido al juego de piedra, papel o tijera.")

while True:                                            # Mostrar Menú / Empieza bucle principal
    print("\nMenú:")
    print("1. Jugar")
    print("2. Salir")
    menu = input("\nSelecciona una opción (1 o 2): ")  # Mostrar opciones para empezar el juego/salir

    if menu == "1":                                    # Si elige JUGAR  
        opciones = ["PIEDRA", "PAPEL", "TIJERA"]                                             
        print("\nElige una opción:")
        print("1. PIEDRA")
        print("2. PAPEL")
        print("3. TIJERA")
    
        while True:                                     # Bucle para jugar
            jugador = input("Elige: PIEDRA, PAPEL o TIJERA: ").upper()  
            if jugador not in opciones:                 # Validar opcion valida del jugador
                print("\nOpción no válida. Por favor escribe PIEDRA, PAPEL o TIJERA.")
                continue    
            else:
                break                                    # Si la opcion es valida, salir del bucle secundario                              

        computadora = random.choice(opciones)            #Necesario para que la computadora elija / Consultar Ing
        print("\nEscogiste:", jugador)
        print("El PC escogió:", computadora)

        if jugador == computadora:                       # Resultado de la partida  
            print("Empate!")
        elif (jugador == "PIEDRA" and computadora == "TIJERA") or \
             (jugador == "PAPEL" and computadora == "PIEDRA") or \
             (jugador == "TIJERA" and computadora == "PAPEL"):
            print("\n¡Ganaste!")    
        else:
            print("\n¡Perdiste!")


    elif menu == "2":                                     # Si elige SALIR, terminar el bucle principal
        print("¡Hasta la próxima!")
        break
    else:
        print("Opción no válida. Por favor selecciona 1 o 2.")

    
