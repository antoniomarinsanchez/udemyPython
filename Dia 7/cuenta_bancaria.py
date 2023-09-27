class Persona:

    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return (f'Cliente: {self.nombre} {self.apellido}\n '
                f'Numero de cuenta: {self.numero_cuenta}\n'
                f'Balance de cuenta: {self.balance}')

    def depositar(self, cantidad):
        self.balance += cantidad

    def retirar(self, cantidad):
        self.balance -= cantidad


# Codigo principal


def crear_cliente():
    nombre = input("Dime tu numbre: ")
    apellido = input("Dime tu apellido: ")
    cliente = Cliente(nombre, apellido, 1000, 0)

    return cliente


def imprimir_menu():
    print("[1] Depositar dinero")
    print("[2] Retirar dinero")
    print("[3] Salir del programa")


def inicio(cliente):
    opcion = ""
    while opcion != "3":
        print(mi_cliente)
        imprimir_menu()
        opcion = input("Escoja una opción: ")
        match opcion:
            case "1":
                mi_cliente.depositar(int(input("Qué cantidad quiere depositar?: ")))
            case "2":
                mi_cliente.retirar(int(input("Qué cantidad quiere retirar?: ")))
            case "3":
                print("Saliendo del programa...")
            case _:
                print("No es una opción valida")


# Creo el cliente
mi_cliente = crear_cliente()
inicio(mi_cliente)
