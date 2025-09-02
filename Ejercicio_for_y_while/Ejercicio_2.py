# Juego Piedra, Papel o Tijera contra la computadora

import random

print("Bienvenido al juego Piedra, Papel o Tijera")
print("Opciones: piedra, papel, tijera o salir")

jugador_gana = 0
computadora_gana = 0

while True:
    jugador = input("Elige tu jugada: ").lower()

    if jugador == "salir":
        break

    if jugador not in ["piedra", "papel", "tijera"]:
        print("Opción no válida, intenta de nuevo.")
        continue

    opciones = ["piedra", "papel", "tijera"]
    computadora = random.choice(opciones)
    print(f"La computadora eligió: {computadora}")

    if jugador == computadora:
        print("¡Empate!")
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "tijera" and computadora == "papel") or \
         (jugador == "papel" and computadora == "piedra"):
        print("¡Ganaste esta ronda!")
        jugador_gana += 1
    else:
        print("La computadora ganó esta ronda.")
        computadora_gana += 1

print("\nJuego terminado.")
print(f"Marcador final: Jugador {jugador_gana} - {computadora_gana} Computadora")