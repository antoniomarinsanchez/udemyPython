print("Programa de calculo de comisiones")
nombre = input("Dime tu nombre: ")
ventas = int(input("¿Cuánto has vendido este mes?"))

comision = round(ventas*13/100,2)

print(f'{nombre}, este mes ganaste {comision}€ en comisiones')
