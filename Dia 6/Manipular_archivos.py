# Ejercicio 1
file = open("texto.txt", 'r')
print(file.read())
file.close()

# Ejercicio 2
file = open("texto.txt", 'r')
print(file.readline())
file.close()

# Ejercicio 2
file = open("texto.txt", 'r')
todas = file.readlines()
print(todas[1])
file.close()
