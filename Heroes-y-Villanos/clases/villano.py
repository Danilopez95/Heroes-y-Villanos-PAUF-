
from clases.personaje import Personaje
import random

class Villano(Personaje):
    def __init__(self,nombre,apellidos,fecha_nacimiento,id):
        super().__init__(nombre,apellidos,fecha_nacimiento,id)
        self.chagepeteador = random.randint(0,100)
        self.entregadorTardio = random.randint(0,100)
        self.ausencias = random.randint(0,100)
        self.hablador = random.randint(0,100)

        self.puntuacion_total = (
            self.chagepeteador +
            self.entregadorTardio +
            self.ausencias +
            self.hablador
        ) / 4