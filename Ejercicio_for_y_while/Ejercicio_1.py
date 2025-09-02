# Programa que encripta 5 mensajes con la cifra del César

# Primero pido al usuario el número de lugares que se van a correr
corrimiento = int(input("Ingrese el corrimiento: "))
alfabeto = "abcdefghijklmnñopqrstuvwxyz"

# Hago 5 repeticiones porque son 5 mensajes
for i in range(1, 6):
    mensaje = input(f"Ingrese el mensaje {i}: ")
    mensaje_encriptado = ""

    for letra in mensaje:
        if letra.lower() in alfabeto:  
            indice = alfabeto.index(letra.lower())
            nuevo_indice = (indice + corrimiento) % 27
            nueva_letra = alfabeto[nuevo_indice]

            if letra.isupper():
                mensaje_encriptado += nueva_letra.upper()
            else:
                mensaje_encriptado += nueva_letra
        else:
            mensaje_encriptado += letra

    print(f"Mensaje {i} encriptado: {mensaje_encriptado}")


    