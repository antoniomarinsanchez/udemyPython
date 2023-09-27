# Devolver distintos
def devolver_distintos(num1, num2, num3):
    lista = [num1, num2, num3]
    lista.sort()
    suma = sum(lista)
    resultado = 0
    if suma > 15:
        resultado = lista[-1]
    elif suma < 10:
        resultado = lista[0]
    elif suma in range(10,16):
        resultado = lista[1]

    return resultado


# Ordenar letras
def ordenar_letras(palabra):
    lista_unica = list(set(palabra))
    lista_unica.sort()
    return lista_unica


# Ceros consecutivos
def ceros_consecutivos(*args):
    anterior = 1
    for actual in args:
        print(f'Valor anterior: {anterior} -- Valor actual: {actual}')
        if anterior == actual and anterior == 0:
            return True
        anterior = actual
    return False


# Primos
def contar_primos(numero):

    primos = [2]
    iteracion = 3

    # Compruebo si es mayor que 2
    if numero < 2:
        return 0

    while iteracion <= numero:

        for n in range(3, iteracion, 2):
            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion += 2
    return primos

print(contar_primos(3))