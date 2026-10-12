
from clases.personaje import Personaje
import random

class Heroe(Personaje):
    def __init__(self,nombre,apellidos,fecha_nacimiento,id):
        super().__init__(nombre,apellidos,fecha_nacimiento,id)
        self.codigo_limpio = random.randint(0,100)
        self.bien_documentado = random.randint(0,100)
        self.gitgod = random.randint(0,100)
        self.arquitecto = random.randint(0,100)
        self.detallista = random.randint(0,100)
