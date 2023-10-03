''' Codigo principal de la farmacia'''
import numeros as nm

def mostrar_menu():
    '''Función que muestra el menú por pantalla'''
    print('1. Pedir turno en la perfumería\n')
    print('2. Pedir turno en la farmacia\n')
    print('3. Pedir turno en la cosmética\n')
    print('4. Salir\n')

def leer_opcion():
    '''Función que lee la opción introducida por el usuario'''
    opcion = input("Escoga una opción del menú: ")
    print("\n")
    return opcion

def comprobar_opcion(opcion):
    '''Función que comprueba si es una entrada válida'''
    if not opcion.isnumeric() or int(opcion) not in range(1,5):
        return False
    else:
        return True

def ejecutar_opcion(opcion):
    '''Función que dada una opción del menu ejecuta el programa correspondiente'''
    match int(opcion):
        case 1:
            nm.mostrar_turno("P")()
            return True
        case 2:
            nm.mostrar_turno("F")()
            return True
        case 3:
            nm.mostrar_turno("C")()
            return True
        case 4:
            print("Saliendo....")
            return False
        case _:
            pass

def main():
    '''Función que ejecuta el programa principal'''
    finalizar = True
    while finalizar:
        mostrar_menu()
        opcion = leer_opcion()
        if comprobar_opcion(opcion):
            finalizar = ejecutar_opcion(opcion)
        else:
            print("Ejecuta una opcion válida\n")

main()
