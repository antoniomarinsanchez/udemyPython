from random import randint
# Adivinar un número en 8 intentos

# Numero a adivinar
numero_secreto = randint(0,100)

# Inicio del programa
print("------- BIENVENIDO EL JUEGO DEL NÚMERO SECRETO -------\n")
nombre = input("Dime tu nombre: ")
print(f"Bueno {nombre} tienes que adivinar el número que estoy pensando en 8 intentos")

# Bucle del juego mientras intentos sea menor que 8
intentos = 0
numero = 0

while intentos < 8:
    # Introducir número
    numero = int(input("Introduce un número entre el 0 y el 100: "))
    intentos += 1
    # Si el número introducido es < 0 o > 100. Numero no permitido
    if numero not in range(1,101):
        print(f'{numero} no se encuentra en el rango\n')
    # Si el numero es menor que la respuesta, le dirá que es menor
    elif numero < numero_secreto:
        print(f'{numero} es menor que el número secreto\n')
    # Si el numero es mayor que la respuesta, le dirá que es mayor
    elif numero > numero_secreto:
        print(f'{numero} es mayor que el número secreto\n')
    # Si el numero es igual le dirá que ha acertado y cuantos intentos le ha llevado
    else:
        print(f'Enhorabuena {nombre}, {numero} es el número secreto y te costó {intentos} intentos\n')
        break
if numero != numero_secreto:
    print(f"Lo siento {nombre} se acabaron los intentos. El numero secreto es {numero_secreto}\n")






