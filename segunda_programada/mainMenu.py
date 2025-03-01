import os
from dataHandler import (
    initialize_info_dat, write_record, read_record,
    write_collision_record, read_collision_records
)
from hash_function import compute_hash
from punt_play import PuntPlay

def cargar_datos():
    current_dir = os.path.dirname(__file__)
    csv_dir = os.path.join(current_dir, "..", "primera_programada", "results")

    if not os.path.exists(csv_dir):
        print("No existe la carpeta de resultados:", csv_dir)
        return

    archivos = [f for f in os.listdir(csv_dir) if f.endswith(".csv")]
    if not archivos:
        print("No hay archivos CSV en", csv_dir)
        return

    for archivo in archivos:
        ruta_csv = os.path.join(csv_dir, archivo)
        with open(ruta_csv, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                partes = linea.split(",")

                # Rellena hasta 6 columnas (fecha y hora quedan vacías si no existen)
                while len(partes) < 6:
                    partes.append("")

                game_id, equipos, yardas, cuarto, fecha, hora = partes[:6]
                jugada = PuntPlay(game_id, equipos, yardas, cuarto, fecha, hora)

                # Extrae equipo local (después de '@')
                if "@" in equipos:
                    local_team = equipos.split("@")[-1].strip()
                else:
                    local_team = equipos

                try:
                    c = int(cuarto)
                except ValueError:
                    c = 0

                pos = compute_hash(fecha, c, local_team)

                existente = read_record(pos)
                if existente is None:
                    write_record(jugada, pos)
                else:
                    write_collision_record(jugada, pos)
        print("Procesado:", archivo)

def buscar_datos():
    try:
        llave = int(input("Llave (0-749): "))
    except:
        print("Número inválido.")
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







