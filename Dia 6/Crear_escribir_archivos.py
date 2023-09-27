# Ejercicio 1
file = open("mi_archivo.txt", 'w')
file.write("Nuevo texto")
file.close()

file = open("mi_archivo.txt", 'r')
print(file.read())
file.close()

# Ejercicio 2
file = open('mi_archivo.txt', 'a')
file.write("Nuevo inicio de sesión")
file.close()

file = open('mi_archivo.txt','r')
print(file.read())
file.close()

# Ejercicio 3
registro_ultima_sesion = ["\nFederico", "\t20/12/2021", "\t08:17:32 hs", "\tSin errores de carga"]
file = open("registro.txt", 'a')
file.writelines(registro_ultima_sesion)
file.close()

file = open("registro.txt", 'r')
print(file.read())
file.close()