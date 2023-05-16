import random


def menu():
    print("------------------------------------------------------")
    print("¡LOTERIA!\n")
    print("1. Iniciar juego")
    print("2. Resumen de partidas")
    print("3. Salir")
    opcion = input("\nSeleccione una opción: ")
    return opcion


def iniciar_juego(cartas, i, cartas_tiradas):
    cartas = list(cartas)
    while True:
        carta = random.randint(1, i)
        print("----------------------------------")
        print("¡", cartas[carta - 1].upper(), "!")
        print("----------------------------------")
        cartas_tiradas.append(cartas[carta - 1])
        cartas.pop(carta - 1)
        i -= 1
        
        opcion = input("\n¿Desea seguir jugando? (s/n): ")
        while opcion.lower() != "s" and opcion.lower() != "n":
            opcion = input("Opción inválida, por favor seleccione una opción válida: ")

        if opcion.lower() == "n":
            break

    print("\nCartas tiradas:")
    for carta in cartas_tiradas:
        print(carta)

    opcion = input("\n¿Desea reanudar el juego? (s/n): ")
    while opcion.lower() != "s" and opcion.lower() != "n":
        opcion = input("Opción inválida, por favor seleccione una opción válida: ")
    
    if opcion.lower() == "s":
        return iniciar_juego(cartas, i, cartas_tiradas)
    else:
        ganador = input("\nIngrese el nombre del ganador: ")
        partida = {"Ganador": ganador, "Cartas tiradas": cartas_tiradas}
        return partida


def resumen_partidas(historial):
    print("\n\nResumen de partidas:")
    for partida in historial:
        i = 1
        print(f"Ganador {i}: ", partida["Ganador"])
        print("Cartas tiradas:")
        for carta in partida["Cartas tiradas"]:
            print(carta)
        print("")
        i += 1


cartas = ("El gallo","El diablito","La dama","El catrín","El paraguas","La sirena","La escalera","La botella","El barril",
        "El árbol","El melón","El valiente","El gorrito","La muerte","La pera","La bandera","El bandolón","El violoncello","La garza",
        "El pájaro","La mano","La bota","La luna","El cotorro","El borracho","El negrito","El corazón","La sandía","El tambor",
        "El camarón","Las jaras","El músico","La araña","El soldado","La estrella","El cazo","El mundo","El apache","El nopal",
        "El alacrán","La rosa","La calavera","La campana","El cantarito","El venado","El sol","La corona","La chalupa","El pino",
        "El pescado","La palma","La maceta","El arpa","La rana")


historial = []
while True:
    opcion = menu()
    if opcion == "1":
        partida = iniciar_juego(cartas=cartas, i=54, cartas_tiradas=[])
        historial.append(partida)
    elif opcion == "2":
        resumen_partidas(historial)
    elif opcion == "3":
        print("\n¡Hasta luego!\n")
        break
    else:
        print("Opción inválida, por favor seleccione una opción válida")
