# Ejercicio 1
def abrir_leer(ruta):
    file = open(ruta, 'r')
    file_read = file.read()
    file.close()
    return file_read


# Ejercicio 2
def sobrescribir(ruta):
    file = open(ruta, 'w')
    file.write('contenido eliminado')
    file.close()


# Ejercicio 3
def registro_error(ruta):
    file = open(ruta, 'a')
    file.write("se ha registrado un error de ejecución")
    file.close()
