# Ejercicio 1
def todos_positivos(lista):
    for numero in lista:
        if numero < 0:
            return False
        else:
            pass

    return True


lista_numeros = [1, 2, 4, -5, 66, -66]


# Ejercicio 2
def suma_menores(lista):
    suma = 0
    for numero in lista:
        if numero in range(0,1001):
            suma += numero
    return suma


# Ejercicio 3
def cantidad_pares(lista):
    pares = 0
    for numero in lista:
        if numero % 2 == 0:
            pares += 1
    return pares


print(cantidad_pares(lista_numeros))