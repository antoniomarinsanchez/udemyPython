# Ejercicio 1
texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
texto_strip = texto.lstrip(",:%_#")
print(texto_strip)

# Ejercicio 2
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3,"naranja")

# Ejercicio 3
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)