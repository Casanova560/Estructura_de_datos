from lector_data import LectorData
from ordenamiento import burbuja, insercion, merge_sort, quick_sort

def guardar_resultados(archivo, jugadas):
    with open(archivo, "w") as f:
        for jugada in jugadas:
            f.write(str(jugada) + "\n")

carpeta = "C:/Users/sebas/OneDrive/Escritorio/Tarea_programada/data/primeraprogramada"
lector = LectorData(carpeta)

# Procesar los archivos usando el lector
for archivo, jugadas in lector.procesar_todos_los_archivos():
    if len(jugadas) == 0:
        print(f" No se encontraron jugadas de punt sin fumble en {archivo}.")
        continue

    print(f"Se cargaron {len(jugadas)} jugadas del archivo {archivo}.")

    # Burbuja
    ordenadas, comps, intercambios = burbuja(jugadas)
    guardar_resultados(f"parte1-burbuja-{archivo}-resultado.csv", ordenadas)
    print(f"Burbuja completado.  # de comparaciones: {comps}, intercambios: {intercambios}")

    # Inserción
    ordenadas, comps, intercambios = insercion(jugadas)
    guardar_resultados(f"parte1-insercion-{archivo}-resultado.csv", ordenadas)
    print(f"Inserción completado. comparaciones: {comps}, intercambios: {intercambios}")

    # Merge Sort (recursivo)
    ordenadas, comps, intercambios = merge_sort(jugadas)
    guardar_resultados(f"parte1-merge_sort-{archivo}-resultado.csv", ordenadas)
    print(f"Merge Sort (recursivo) completado. comparaciones: {comps}, intercambios: {intercambios}")

    # Quick Sort (recursivo)
    ordenadas, comps, intercambios = quick_sort(jugadas)
    guardar_resultados(f"parte1-quicksort-{archivo}-resultado.csv", ordenadas)
    print(f"Quick Sort (recursivo) completado. comparaciones: {comps}, intercambios: {intercambios}")

print("\nTodos los archivos han sido procesados en orden cronologico.")
