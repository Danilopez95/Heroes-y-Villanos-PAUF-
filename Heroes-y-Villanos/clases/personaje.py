
from datetime import datetime, date
import logging

class Personaje:

    def __init__(self ,nombre ,apellidos ,fecha_nacimiento ,id):
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.id = id
        self.puntuacion_total = 0

    def __str__(self):
        return f"{self.nombre} {self.apellidos} - ID {self.id} - Puntuación {self.puntuacion_total}"


    def calcular_edad(self):

        try:
            nacimiento = datetime.strptime(self.fecha_nacimiento, "%d/%m/%Y").date()
            #Convierte la fecha guardada en texto, en ese formato
            hoy = date.today()

            edad = hoy.year - nacimiento.year

            if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):
                edad -= 1

            return edad

        except ValueError:
            print("La fecha de nacimiento no es válida")
            logging.exception("Error al calcular la edad")
            return None  #No tenemos un resultado válido



