from clases.personaje import Personaje
from clases.heroe import Heroe
from clases.villano import Villano
import random
import logging


class Gestion:
    def __init__(self):
        self.personajes ={}  #Dicionario donde guardamos Heroes y villanos

    def agregar_personajes (self, personaje):
        if personaje.id in self.personajes:  #Mirar si existe el ID
            print("Ya existe un personaje con este ID")
            logging.warning(f"ID duplicado: {personaje.id}")
        else:
            self.personajes[personaje.id] = personaje
            print("Personaje agregado correctamente")
            logging.info(f"Personaje agregado: {personaje.nombre} - ID: {personaje.id}")


    def listar_personajes(self):
        if not self.personajes:  #Comprobar si el diccionario está vacio
            print("No hay personajes registrados")
        else:
            for personaje in self.personajes.values():  #Te da todos los objetos almacenados en el diccionario
                print(personaje)


    def buscar_por_id(self,id):
        if id in self.personajes:  #Mirar si existe el ID
            print(self.personajes[id])  #Recupera el personaje de ese ID
            logging.info(f"Personaje encontrado con ID: {id}")
        else:
            print("No existe ningun personaje con esa ID")
            logging.info(f"Búsqueda sin resultados para ID: {id}")

    def buscar_por_nombre(self, nombre):
        encontrado = False

        for personaje in self.personajes.values():
            if personaje.nombre == nombre:
                print(personaje)
                encontrado = True

        if not encontrado:
            print("No existe ningún personaje con ese nombre")

    def buscar_por_gitgod(self, puntuacion):
        encontrado = False

        for personaje in self.personajes.values():
            if isinstance(personaje, Heroe):  #Comprobar si el personaje es un objeto de la clase Heroe
                if personaje.gitgod > puntuacion:
                    print(personaje)
                    encontrado = True

        if not encontrado:
            print("No hay héroes con esa puntuacion de GITGod")


    def buscar_por_ausencias(self, puntuacion):
        encontrado = False

        for personaje in self.personajes.values():
            if isinstance(personaje, Villano):
                if personaje.ausencias > puntuacion:
                    print(personaje)
                    encontrado = True

        if not encontrado:
            print("No hay Villanos con esas ausencias")


    def buscar_por_atributo(self, atributo, operador, valor):
        encontrado = False

        try:
            if operador not in ("==",">","<"):
                print("Operador no válido")
                logging.error(f"Operador no válido: {operador}")
                return

            for personaje in self.personajes.values():
                if hasattr(personaje, atributo):
                    valor_personaje = getattr(personaje, atributo)  #Coge el atributo

                    if operador == "==":
                        cumple = valor_personaje == valor
                    elif operador == ">":
                        cumple = valor_personaje > valor
                    elif operador == "<":
                        cumple = valor_personaje < valor
                    else:
                        print("Operador no válido")
                        logging.info(f"Operador no válido: {operador}")
                        return

                    if cumple:
                        print(personaje)
                        logging.info(f"Personaje encontrado: {personaje.id}")
                        encontrado = True

            if not encontrado:
                print("No se encontraron personajes")
                logging.warning(f"Sin resultados: {atributo} {operador} {valor}")

        except (TypeError,ValueError):
            print("Error al comparar valores")
            logging.exception("Error en la búsqueda por atributo")

    def pelea(self):
        heroes = []
        villanos = []

        for personaje in self.personajes.values():
            if isinstance(personaje, Heroe):
                heroes.append(personaje)
            elif isinstance(personaje, Villano):
                villanos.append(personaje)

        if not heroes or not villanos:
            print("No hay suficientes personajes para realizar una pelea")
            logging.warning(f"No hay suficientes personajes para la pelea")
        else:
            heroe_elegido = random.choice(heroes) #Elije un heroe de forma aleatoria
            villano_elegido = random.choice(villanos)

            print("Héroe:", heroe_elegido)
            print("Villano:", villano_elegido)

            logging.info(
                f"Enfrentamiento: Heroe ID {heroe_elegido.id} "
                f"contra Villano ID {villano_elegido.id}"
            )

            diferencia = abs(heroe_elegido.puntuacion_total - villano_elegido.puntuacion_total)
            #el abs calcula la diferencias entre las puntuaciones de lo sdos

            if diferencia <= 10:
                print("El enfrentamiento está equilibrado")
                logging.info(f"Enfrentamiento equilibrado")
            else:
                print("El enfrentamiento está desequilibrado")
                logging.info("Enfrentamiento desequilibrado")

            print("Diferencia de puntuación:", diferencia)
            logging.info(f"Diferencia de puntuación: {diferencia}")























