# Ejercicio 1
def suma_cuadrados(*args):
    suma = 0
    for arg in args:
        suma += arg**2

    return suma


# Ejercicio 2
def suma_absolutos(*args):
    suma = 0
    for arg in args:
        suma += abs(arg)

    return suma

# Ejercicio 3
def numeros_persona(nombre, *args):
    mensaje = f'{nombre}, la suma de tus números es {sum(args)}'
    return mensaje
