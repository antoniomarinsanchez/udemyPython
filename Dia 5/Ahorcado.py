
# Imports
from random import choice
# ----- Funciones -----


# Funcion para pedir letra
def pedir_letra():
    '''devuelve la letra'''
    letra = input('Dime una letra: ')
    return letra


# Funcion para validar letra
def validar_letra(letra):
    '''devuelve verdadero o falso si es o no una letra '''
    abc = "abcdefghijklmnñopqrstuvwxyz"
    if letra.lower() not in abc or len(letra) > 1:
        return False
    else:
        return True


# Función para chequear si la letra esta en la palabra
def chequear_letra(letra, palabra, salida, vida, incorrectas):
    ''' devuelve verdadero o falso si esta la letra en la palabra
     también devuelve la salida_secreta actualizada'''
    lista_salida = list(salida)
    if letra in palabra:
        for n in range(0, len(palabra)):
            if letra == palabra[n]:
                lista_salida[n] = letra

    else:
        print(f'La letra {letra} no está en la palabra secreta')
        incorrectas.append(letra)
        # Perder una vida
        vida -= 1
        print(f'Te quedan {vida} vidas')

    salida = "".join(lista_salida)
    print(salida)
    return salida, vida, incorrectas


# Función para comprobar si gano
def fin_juego(salida, vida):
    if vida > 0:
        if '_' not in salida:
            print(f'ENHORABUENA! La palabra secreta era {salida}. Has ganado!')
            return True
        else:
            return False
    else:
        print(f'Lo siento te quedaste sin vidas. Has perdido')
        return True


# dibujo ahorcado
def dibujo_ahorcado(vida):
    match vida:
        case 6:
            print("______")
            print("|    ")
            print("|    ")
            print("|    ")
            print("_______")
        case 5:
            print("______")
            print("|    O")
            print("|    ")
            print("|    ")
            print("_______")
        case 4:
            print("______")
            print("|    O")
            print("|    |")
            print("|    ")
            print("_______")
        case 3:
            print("______")
            print("|    O")
            print("|   /|")
            print("|    ")
            print("_______")
        case 2:
            print("______")
            print("|    O")
            print("|   /|\\")
            print("|    ")
            print("_______")
        case 1:
            print("______")
            print("|    O")
            print("|   /|\\")
            print("|   / ")
            print("_______")
        case 0:
            print("______")
            print("|    O")
            print("|   /|\\")
            print("|   / \\")
            print("_______")
        case _:
            print("______")
            print("|    ")
            print("|    ")
            print("|    ")
            print("_______")


# escoger al azar
def escoger_palabra():
    lista_palabras = ['perro', 'gato', 'casa']
    print(f'Estoy pensando la palabra.... YA ESTA!')
    return choice(lista_palabras)


#  ------- Main del Juego -------
vida_user = 6
letras_incorrectas = []

# Bienvenida
print('------ BIENVENIDO AL JUEGO DEL AHORCADO -----')
nombre = input('Dime tu nombre: ')
print(f'Buenas {nombre}, vamos a comenzar')


# Escoger palabras al azar de una lista
palabra_secreta = escoger_palabra()

# Mostrar ahorcado inicial y salida secreta
dibujo_ahorcado(vida_user)
salida_secreta = len(palabra_secreta)*'_'
print(salida_secreta)

# Bucle principal juego
while not fin_juego(salida_secreta, vida_user):

    letra_user = pedir_letra()

    if validar_letra(letra_user):

        salida_secreta, vida_user, letras_incorrectas = chequear_letra(letra_user, palabra_secreta, salida_secreta,
                                                                       vida_user, letras_incorrectas)
        dibujo_ahorcado(vida_user)
    else:
        print(f'{letra_user} no es una letra')



