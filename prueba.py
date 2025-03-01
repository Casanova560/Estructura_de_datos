import csv

archivo_csv = "primera_programada/results/ejemplo.csv"  # Cambia el nombre según tu dataset

with open(archivo_csv, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        print(row)
        if i == 5:  # Solo mostrar las primeras 5 filas
            break
