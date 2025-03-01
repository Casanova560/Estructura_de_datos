import os
from punt_play import PuntPlay
from dataHandler import (
    initialize_info_dat, write_record, read_record,
    write_collision_record, read_collision_records
)
from hash_function import compute_hash

current_dir = os.path.dirname(__file__)           # .../primera_programada/segunda_programada
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))  # .../primera_programada
DATA_DIR = os.path.join(parent_dir, "primera_programada", "results")
# Esto genera: C:\Users\sebas\OneDrive\Escritorio\primera_programada\primera_programada\results

def cargar_datos():
    if not os.path.exists(DATA_DIR):
        print("No existe:", DATA_DIR)
        return
    archivos = [f for f in os.listdir(DATA_DIR) if f.endswith(".csv")]
    if not archivos:
        print("No hay archivos CSV en", DATA_DIR)
        return
    for archivo in archivos:
        ruta = os.path.join(DATA_DIR, archivo)
        with open(ruta, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                partes = linea.split(",")
                if len(partes) < 6:
                    continue
                game_id, equipos, yardas, cuarto, fecha, hora = partes
                jugada = PuntPlay(game_id, equipos, yardas, cuarto, fecha, hora)
                local = equipos.split("-")[0].strip()
                try:
                    c = int(cuarto)
                except:
                    c = 0
                pos = compute_hash(fecha, c, local)
                reg = read_record(pos)
                if reg is None:
                    write_record(jugada, pos)
                else:
                    write_collision_record(jugada, pos)
        print("Procesado:", archivo)

def buscar_datos():
    try:
        llave = int(input("Llave (0-749): "))
    except:
        print("Inválido.")
        return
    if llave < 0 or llave >= 750:
        print("Fuera de rango.")
        return
    reg = read_record(llave)
    if reg is None:
        print("Vacío.")
    else:
        print("Registro:", reg)
    col = read_collision_records(llave)
    if col:
        print("Colisiones:")
        for c in col:
            print(c)
    else:
        print("Sin colisiones.")

def main():
    initialize_info_dat()
    while True:
        print("\n1. Cargar datos\n2. Buscar datos\n3. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            cargar_datos()
        elif op == "2":
            buscar_datos()
        elif op == "3":
            break
        else:
            print("Inválido.")

if __name__ == "__main__":
    main()




