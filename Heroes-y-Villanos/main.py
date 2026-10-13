
import logging

from clases.heroe import Heroe
from clases.villano import Villano
from logs.gestion import Gestion

logging.basicConfig(
    filename="actividad.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    force=True
)


def menu():
    print("\n========== HÉROES Y VILLANOS ==========")
    print("[1] Crear héroe")
    print("[2] Crear villano")
    print("[3] Buscar personaje por ID")
    print("[4] Buscar personaje por nombre")
    print("[5] Buscar personaje por atributo")
    print("[6] Listar personajes")
    print("[7] Calcular edad de un personaje")
    print("[8] Enfrentar héroe y villano")
    print("[9] Salir")
    print("=======================================")


def gestion_simulacion(opcion, gestion):
    salir = False

    try:
        match opcion:
            case 1:
                print("\n--- CREAR HÉROE ---")

                nombre = input("Nombre: ")
                apellidos = input("Apellidos: ")
                fecha = input("Fecha de nacimiento (DD/MM/AAAA): ")
                id = int(input("ID: "))

                heroe = Heroe(nombre, apellidos, fecha, id)
                gestion.agregar_personajes(heroe)

            case 2:
                print("\n--- CREAR VILLANO ---")

                nombre = input("Nombre: ")
                apellidos = input("Apellidos: ")
                fecha = input("Fecha de nacimiento (DD/MM/AAAA): ")
                id = int(input("ID: "))

                villano = Villano(nombre, apellidos, fecha, id)
                gestion.agregar_personajes(villano)

            case 3:
                print("\n--- BUSCAR POR ID ---")

                id = int(input("Introduce el ID: "))
                gestion.buscar_por_id(id)

            case 4:
                print("\n--- BUSCAR POR NOMBRE ---")

                nombre = input("Introduce el nombre: ")
                gestion.buscar_por_nombre(nombre)

            case 5:
                print("\n--- BUSCAR POR ATRIBUTO ---")

                atributo = input("Atributo: ")
                operador = input("Operador (==, >, <): ")
                valor = input("Valor: ")

                if atributo in ("nombre", "apellidos", "fecha_nacimiento"):
                    pass
                elif atributo in ("id", "gitgod", "ausencias",
                                  "codigo_limpio", "bien_documentado",
                                  "arquitecto", "detallista",
                                  "chagepeteador", "entregadorTardio",
                                  "hablador"):
                    valor = int(valor)
                elif atributo == "puntuacion_total":
                    valor = float(valor)

                gestion.buscar_por_atributo(atributo, operador, valor)

            case 6:
                print("\n--- LISTAR PERSONAJES ---")
                gestion.listar_personajes()

            case 7:
                print("\n--- CALCULAR EDAD ---")

                id = int(input("Introduce el ID: "))

                if id in gestion.personajes:
                    personaje = gestion.personajes[id]
                    print("Edad:", personaje.calcular_edad())
                    logging.info(f"Edad consultada del personaje ID {id}")
                else:
                    print("No existe ningún personaje con ese ID")
                    logging.warning(f"Edad consultada con ID inexistente: {id}")

            case 8:
                print("\n--- ENFRENTAMIENTO ---")
                gestion.pelea()

            case 9:
                print("Saliendo del programa...")
                logging.info("Programa finalizado")
                salir = True

            case _:
                print("Opción no válida")
                logging.warning(f"Opción no válida: {opcion}")

    except ValueError:
        print("Error: has introducido un valor incorrecto")
        logging.exception("Error de valor en el menú")

    except Exception:
        print("Ha ocurrido un error")
        logging.exception("Error al gestionar la opción")

    return salir


def main():
    gestion = Gestion()

    while True:
        menu()

        try:
            opcion = int(input("Elige una opción: "))

            if gestion_simulacion(opcion, gestion):
                break

        except ValueError:
            print("Debes introducir un número del 1 al 9")
            logging.exception("Opción del menú no numérica")


if __name__ == "__main__":
    main()
