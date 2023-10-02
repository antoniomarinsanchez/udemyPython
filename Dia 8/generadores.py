''' Generadores '''
# Ejercicio 1
# def mi_generador():
#     '''Generador'''
#     i = 0
#     while True:
#         i +=1
#         yield i

# generador = mi_generador()

# print(next(generador))

# Ejercicio 2
def mi_generador():
    '''Generador'''
    i = 0
    while True:
        i +=7
        yield i

generador = mi_generador()

# Ejercicio 2

def mi_perder_vida(vida):
    '''Generador para perder vida'''
    while vida > 0:
        if vida == 1:
            yield f'Te queda {vida} vida'
        else:
            yield f'Te quedan {vida} vidas'
        vida -=1
    yield "Game Over"

perder_vida = mi_perder_vida(3)

print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
