# hash_function.py

def calcular_posicion(fecha, cuarto, equipo_local):
    """
    Función de hash que calcula la posición en info.dat
    Basado en fecha, cuarto y nombre del equipo local.
    """
    clave = hash((fecha, cuarto, equipo_local))
    return clave % 750  # Aseguramos que esté dentro del rango de 750 registros
