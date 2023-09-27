# Ejercicio 1
from random import randint


# Funcion lanzar dados
def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return dado1, dado2


# Funcion evaluar dados
def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    salida = ""
    if suma_dados <= 6:
        salida = f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados in range(6,10):
        salida = f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    elif suma_dados >= 10:
        salida = f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

    return salida


# Ejercicio 2
lista_numeros = [1,2,15,7,2]


# Reducir lista
def reducir_lista(lista):
    lista_unica = []
    for numero in lista:
        # Borrar duplicados
        if numero not in lista_unica:
            lista_unica.append(numero)
        else:
            pass
    lista_unica.remove(max(lista_unica))

    return lista_unica


# Promedio lista
def promedio(lista):
    suma = 0
    for numero in lista:
        suma += numero
    resultado = suma/len(lista)

    return resultado


# Ejercicio 3
from random import choice
lista_numeros = [1, 2, 3 ,4]


# Lanzar moneda
def lanzar_moneda():
    monedas = ["Cara", "Cruz"]
    eleccion = choice(monedas)
    return eleccion


# Probar suerte
def probar_suerte(eleccion, lista):
    salida = []
    if eleccion == "Cara":
        print("La lista se autodestruirá")
    elif eleccion == "Cruz":
        print("La lista fue salvada")
        salida = lista

    return salida


print(probar_suerte(lanzar_moneda(),lista_numeros))