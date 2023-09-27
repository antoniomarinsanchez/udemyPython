# Ejercicio 1
def cantidad_atributos(**kwargs):
    return len(kwargs)


# Ejercicio 2
def lista_atributos(**kwargs):
    lista = []
    for kwarg in kwargs.values():
        lista.append(kwarg)

    return lista


# Ejercicio 3
def describir_persona(nombre, **kwargs):
    print(f'Características de {nombre}:')
    for item,value in kwargs.items():
        print(f'{item}:{value}')


describir_persona("tomás",color_ojos="azules",color_pelo="verde")