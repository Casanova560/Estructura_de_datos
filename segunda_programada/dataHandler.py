# segunda_programada/dataHandler.py

import os
from segunda_programada.hash_function import calcular_posicion

FILE_NAME = "info.dat"

def inicializar_archivo():
    """ Crea 'info.dat' si no existe con 750 registros vacíos """
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "wb") as f:
            f.write(b"\x00" * 750 * 32)  # 750 registros de 32 bytes cada uno
        print("Archivo info.dat creado.")

def guardar_dato(fecha, cuarto, equipo_local, dato):
    """ Guarda un dato en info.dat en la posición determinada por la función hash """
    pos = calcular_posicion(fecha, cuarto, equipo_local)
    offset = pos * 32  # Cada registro ocupa 32 bytes

    with open(FILE_NAME, "r+b") as f:
        f.seek(offset)
        contenido = f.read(32)

        if contenido.strip(b"\x00"):  # Si la posición ya está ocupada
            col_file = f"{pos}-col.dat"
            with open(col_file, "ab") as col:
                col.write(dato.ljust(32).encode())  # Guardar la colisión
            print(f"Colisión detectada, guardando en {col_file}")
        else:
            f.seek(offset)
            f.write(dato.ljust(32).encode())  # Guardar en info.dat
            print(f"Guardado en posición {pos}")

inicializar_archivo()  # Asegurar que el archivo exista antes de operar
