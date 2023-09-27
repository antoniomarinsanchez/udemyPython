# Ejercicio 1
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [valor ** 2 for valor in valores]
print(valores_cuadrado)

# Ejercicio 2
valores_pares = [valor for valor in valores if valor % 2 == 0]
print(valores_pares)

# Ejercicio 3
temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(grados_fahrenheit - 32)*5/9 for grados_fahrenheit in temperatura_fahrenheit]