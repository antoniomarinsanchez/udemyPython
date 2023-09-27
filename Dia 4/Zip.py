# Ejercicio 1
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinado = list(zip(paises,capitales))
for pais, capital in combinado:
    print(f'La capital de {pais} es {capital}')

# Ejercicio 2
marcas = ["Seat", "Nike", "CocaCola"]
productos = ["Coche", "Ropa", "Bebida"]
mi_zip = zip(marcas,productos)

# Ejercicio 3
num_espaniol = ["uno", "dos", "tres", "cuatro", "cinco"]
num_portugues = ["um", "dois", "três", "quatro", "cinco"]
num_ingles = ["one", "two", "three", "four", "five"]

numeros = list(zip(num_espaniol,num_portugues,num_ingles))
print(numeros)