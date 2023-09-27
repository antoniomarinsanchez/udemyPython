# Ejercicio 1
palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

objetos = [palabra, lista, tupla]

for objeto in objetos:
    print(len(objeto))

# Ejercicio 2
class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")


mi_mago = Mago()
mi_arquero = Arquero()
mi_samurai = Samurai()

personajes = [mi_arquero, mi_mago, mi_samurai]

for personaje in personajes:
    personaje.atacar()


# Ejercicio 3
class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")


def personaje_defender(personaje):
    personaje.defender()
