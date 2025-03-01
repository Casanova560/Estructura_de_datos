# segunda_programada/mainMenu.py

import os
from segunda_programada.dataHandler import guardar_dato
from primera_programada.src.punt_play import obtener_datos_jugadas


def cargar_datos():
    """ Carga datos de results/ y los guarda en info.dat """
    archivos = os.listdir("primera_programada/results/")
    for archivo in archivos:
        if archivo.endswith(".csv"):
            datos = obtener_datos_jugadas(f"primera_programada/results/{archivo}")
            for dato in datos:
                fecha, cuarto, equipo, jugada = dato
                guardar_dato(fecha, cuarto, equipo, jugada)
            print(f"Procesado {archivo}")


def buscar_dato():
    """ Permite buscar una jugada en info.dat """
    llave = int(input("Ingrese la clave de búsqueda (0-749): "))
    offset = llave * 32  # Cada registro ocupa 32 bytes

    with open("info.dat", "rb") as f:
        f.seek(offset)
        contenido = f.read(32).strip(b"\x00")

        if contenido:
            print(f"Registro encontrado en {llave}: {contenido.decode()}")
            col_file = f"{llave}-col.dat"
            if os.path.exists(col_file):
                with open(col_file, "rb") as col:
                    print("Registros adicionales por colisión:")
                    for line in col:
                        print(line.decode().strip())
        else:
            print("No se encontró ningún dato en esa posición.")


def menu():
    """ Menú interactivo """
    while True:
        print("\nMenú:")
        print("1. Cargar Datos")
        print("2. Buscar Datos")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cargar_datos()
        elif opcion == "2":
            buscar_dato()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intente de nuevo.")


if __name__ == "__main__":
    menu()
