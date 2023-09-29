''' Esto es un modulo para manejo de errores'''

# Ejercicio 1
def suma(num1, num2):
    '''Suma dos numeros'''
    try:
        print(num1 + num2)
    except Exception:
        print("Error inesperado")

# Ejercicio 2 
def cociente(num1, num2):
    '''Realiza la división de dos números'''
    try:
        print(num1/num2)
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")

# Ejercicio 3
def abrir_archivo(nombre_archivo):
    '''Abre un archivo'''
    try:
        archivo = open(nombre_archivo, encoding="utf-8")
    except FileNotFoundError:
        print("El archivo no fue encontrado")
        return None
    except Exception:
        print("Error desconocido")
        return None
    else:
        print("Abriendo exitosamente")
        return archivo
    finally:
        print("Finalizando ejecución")
        