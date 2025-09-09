#1. Generá un cartón 5x5 con números aleatorios entre 1 y 50, sin repetirse.
#2. Mostrá el cartón al jugador en forma de matriz.
#3. El programa debe sortear números al azar entre 1 y 50, uno por uno.
#4. Cada vez que salga un número:
#o Si está en el cartón, reemplazarlo por un 0.
#o Si no está, avisar que no aparece.
#o Mostrar el cartón actualizado después de cada sorteo.
#5. El juego termina cuando el cartón completo queda en 0 (¡Bingo!).
#Desafío extra: Validar cuando haya una línea completa (una fila llena de ceros) y mostrar el 
#mensaje "¡Línea!"

import random

numeros = random.sample(range(1, 51), 25)

carton = []
indice = 0
for i in range(5):
    fila = []
    for j in range(5):
        fila.append(numeros[indice])
        indice += 1
    carton.append(fila)

print("Bienvenido al Bingo")
print("Tu cartón es:")
for fila in carton:
    print(fila)

numeros_sorteo = list(range(1, 51))
random.shuffle(numeros_sorteo)

for numero in numeros_sorteo:
    print("Se sortea el número...", numero)
    encontrado = False

    for i in range(5):
        for j in range(5):
            if carton[i][j] == numero:
                carton[i][j] = 0
                encontrado = True

    if encontrado:
        print("¡Lo tenés!")
    else:
        print("No está en tu cartón.")

    for fila in carton:
        print(fila)

    for fila in carton:
        if fila.count(0) == 5:
            print("¡Línea!")

    bingo = True
    for fila in carton:
        for num in fila:
            if num != 0:
                bingo = False
    if bingo:
        print("¡Bingo!")
        break
