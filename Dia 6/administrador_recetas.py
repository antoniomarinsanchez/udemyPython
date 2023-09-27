import os
from pathlib import Path
from os import system


# Contar recetas
def contar_recetas(ruta):
    contador = len(list(ruta.glob("**/*txt")))
    return contador


# Imprimir menu
def imprimir_menu(ruta,err):

    print("\n ------ BIENVENIDO AL GESTOR DE RECETAS ------- \n")
    # Ubicación de las recetas

    print(f'Las recetas se encuentran en: {ruta}')
    print(f'Tienes {contar_recetas(ruta)} recetas\n')

    print("----- MENU PRINCIPAL ------")
    print("[1] Leer receta\n" +
          "[2] Crear receta\n" +
          "[3] Crear categoria\n" +
          "[4] Eliminar receta\n" +
          "[5] Eliminar categoria\n" +
          "[6] Salir del programa")
    print("---------------------------")
    print(err)


def mostrar_categorias(lista_categorias):
    system('cls')
    for n in range(0,len(lista_categorias)):
        print(f'[{n + 1}] {lista_categorias[n]}')


def mostrar_recetas(lista_recetas):
    system('cls')
    for n in range(0, len(lista_recetas)):
        print(f'[{n + 1}] {lista_recetas[n].stem}')


def escoger_categoria(ruta):
    lista_categorias = [x.stem for x in ruta.iterdir() if x.is_dir()]
    categoria = ""
    siguiente = True
    while siguiente:
        mostrar_categorias(lista_categorias)
        eleccion = input("Escoge la categoria: ")
        if eleccion.isnumeric():
            n = int(eleccion) - 1
            if n in range(0, len(lista_categorias)):
                categoria = lista_categorias[n]
                siguiente = False

    return categoria


def escoger_recetas(ruta):
    lista_recetas = [x for x in ruta.iterdir()]
    receta = ""
    siguiente = True
    while siguiente:
        if len(lista_recetas) == 0:
            print("No hay recetas en esta categoria")
            siguiente = False
        else:
            mostrar_recetas(lista_recetas)
            eleccion = input("Escoge la receta: ")
            if eleccion.isnumeric():
                n = int(eleccion) - 1
                if n in range(0,len(lista_recetas)):
                    receta = lista_recetas[n]
                    siguiente = False

    return receta


def leer_receta(ruta):

    categoria = escoger_categoria(ruta)
    ruta_recetas = Path(ruta, categoria)
    receta = escoger_recetas(ruta_recetas)
    if receta != "":
        file = Path(ruta_recetas, receta)
        print(file.read_text())
    while type(input("Pulsa cualquier tecla para volver al menu: ")) == 'str':
        pass


# crear receta()
def crear_receta(ruta):
    categoria = escoger_categoria(ruta)
    ruta_recetas = Path(ruta, categoria)
    nombre = input("Escribe el nombre de la receta: ")
    contenido = input("Escribe la receta: ")
    file = Path(ruta_recetas, f'{nombre}.txt')

    if not os.path.exists(file):
        file.write_text(contenido)
        print(f'Este es la ruta de la receta: {file}')
    else:
        print("Lo siento, esa receta ya existe")
    while type(input("Pulsa cualquier tecla para volver al menu: ")) == 'str':
        pass


# crear categoria()
def crear_categoria(ruta):
    nombre = input("Escribe el nombre de la categoria: ")
    categoria = Path(ruta, nombre)
    if not os.path.exists(categoria):
        categoria.mkdir()
        print(f'Este es la ruta de la categoria: {categoria}')
    else:
        print("Lo siento, esta categoría ya existe")
    while type(input("Pulsa cualquier tecla para volver al menu: ")) == 'str':
        pass


# eliminar_receta()
def eliminar_receta(ruta):
    categoria = escoger_categoria(ruta)
    ruta_recetas = Path(ruta, categoria)
    receta = escoger_recetas(ruta_recetas)
    if receta != "":
        ack = input("Seguro que quieres borrar esta receta? (s/n): ")
        if ack == 's':
            file = Path(ruta_recetas, receta)
            file.unlink()
            print("La receta ha sido borrada")
        elif ack != 's':
            print("La receta no será borrada")
    while type(input("Pulsa cualquier tecla para volver al menu: ")) == 'str':
        pass


# eliminar categoria()
# pregutnar nombre categoria / eliminar carpeta categoria
def eliminar_categoria(ruta):
    categoria = escoger_categoria(ruta)
    ack = input("¿Estas seguro de borrar esta categoria? (s/n): ")
    if ack == "s":
        categoria = Path(ruta, categoria)
        try:
            categoria.rmdir()
        except:
            print("No se puede borrar la categoria por que no está vacia")

        print(f'La categoria {categoria} ha sido borrada')
    elif ack != "s":
        print('No se borrara la categoria')

    while type(input("Pulsa cualquier tecla para volver al menu: ")) == 'str':
        pass


# Limpio la pantalla
system('cls')
ruta_main = Path(Path.home(), "Recetas")
opcion = ''
error = ''

# Bucle principal del programa
while opcion != '6':

    imprimir_menu(ruta_main, error)
    opcion = input("Escoge una opción del menu: ")
    match opcion:
        case '1':
            leer_receta(ruta_main)
            system('cls')

        case '2':
            crear_receta(ruta_main)
            system('cls')

        case '3':
            crear_categoria(ruta_main)
            system('cls')

        case '4':
            eliminar_receta(ruta_main)
            system('cls')

        case '5':
            eliminar_categoria(ruta_main)
            system('cls')

        case '6':
            print(" ------ FIN DEL PROGRAMA ------")
        case _:
            error = "La opción introducida no es válida"
            system('cls')












