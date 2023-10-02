''' Modulo que define los generadores '''

def perfumeria():
    '''Generador turnos perfumeria'''
    turno = 0
    while True:
        turno +=1
        yield f'P{turno}'

def farmacia():
    '''Generador turnos perfumeria'''
    turno = 0
    while True:
        turno +=1
        yield f'F{turno}'

def cosmetica():
    '''Generador turnos perfumeria'''
    turno = 0
    while True:
        turno +=1
        yield f'C{turno}'

c = cosmetica()
p = perfumeria()
f = farmacia()

def mostrar_turno(numero):
    '''Decorador del generador'''
    def turno():
        print('*'*20)
        print('Este es su turno:')
        if numero == 1:
            print(next(p))
        elif numero == 2:
            print(next(f))
        elif numero == 3:
            print(next(c))
        print("Gracias por todo")
        print('*'*20)
        print('\n')

    return turno
