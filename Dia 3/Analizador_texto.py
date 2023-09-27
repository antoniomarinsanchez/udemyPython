print("------- Bienvenido al analizador de textos --------")
# Introducir un texto
texto = input("Introduce un texto: ").lower()

# Introducir tres letras
letras = []
letras.append(input("Introduce la primera letra: ").lower())
letras.append(input("Introduce la segunda letra: ").lower())
letras.append(input("Introduce la tercera letra: ").lower())
# Cuantas veces a parece cada letra (minusculas y mayusculas
print("\n------- Comprobación de la aparición de las letras ------")
print(f'La letra "{letras[0]}" aparece {texto.count(letras[0])} veces')
print(f'La letra "{letras[1]}" aparece {texto.count(letras[1])} veces')
print(f'La letra "{letras[2]}" aparece {texto.count(letras[2])} veces')

# Cuantas palabras hay en el texto
palabras = texto.lower().split(" ")
print("\n------- Contar el numero de palabras del texto ------")
print(f'Hay {len(palabras)} palabras en el texto')

# Primera letra del texto y la última
print("\n------- Comprobación primera y última letra --------")
print(f'La primera letra del texto es: "{texto[0]}"\nLa última letra del texto es: "{texto[-1]}"')

# Invertir palabras en orden inverso
palabras.reverse() # Este método no devuelve nada. Actua sobre la lista
texto_invertido = " ".join(palabras)
print("\n------- Inversión del orden de las palabras del texto ---------")
print(texto_invertido)

# Aparece python en el texto?
dic_salida = {True: "La palabra Python se encuentra en el texto",
              False: "La palabra Python no se encuentra en el texto"}
print("\n-------- Comprobación de la aparición de la palabra Python -------")
print(dic_salida["python" in palabras])