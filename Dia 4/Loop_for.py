# Ejercicio 1
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
for alumno in alumnos_clase:
    print("Hola " + alumno)

# Ejercicio 2
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0
for numero in lista_numeros:
    suma_numeros += numero

# Ejercicio 3
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares,suma_impares = [0, 0]
for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero

