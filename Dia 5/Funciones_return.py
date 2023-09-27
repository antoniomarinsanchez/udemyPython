# Ejercicio 1
def potencia(base,exponente):
    '''Esta función realiza la potencia de dos numeros'''
    total = base**exponente
    return total


# Ejercicio 2
def usd_a_eur(usd):
    '''Esta función realiza la conversión de dolares a euros'''
    eur = usd * 0.90
    return eur


dolares = 200


# Ejercicio 3
def invertir_palabra(palabra):
    '''Invierte la palabra y la pone en mayuscula'''
    lista_palabra = list(palabra.upper())
    lista_palabra.reverse()
    inversion = "".join(lista_palabra)
    return inversion


palabra = "Python"
