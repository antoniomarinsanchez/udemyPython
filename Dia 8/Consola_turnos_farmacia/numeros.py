''' Modulo que define los generadores '''

def turnos_perfumeria():
    '''Generador turnos perfumeria'''
    for turno in range(1,10000):
        yield f'P - {turno}'

def turnos_farmacia():
    '''Generador turnos perfumeria'''
    for turno in range(1,10000):
        yield f'F - {turno}'

def turnos_cosmetica():
    '''Generador turnos perfumeria'''
    for turno in range(1,10000):
        yield f'C - {turno}'

cosmetica = turnos_cosmetica()
perfumeria = turnos_perfumeria()
farmacia = turnos_farmacia()

def mostrar_turno(opcion):
    '''Decorador del generador'''
    def turno():
        print('*'*20)
        print('Este es su turno:')
        if opcion == "P":
            print(next(perfumeria))
        elif opcion == "F":
            print(next(farmacia))
        elif opcion == "C":
            print(next(cosmetica))
        print("Gracias por todo")
        print('*'*20)
        print('\n')

    return turno
