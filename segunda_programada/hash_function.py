def compute_hash(fecha, cuarto, local):
    """
    Ejemplo: suma los ord() de la fecha (si existe) y el local,
    y multiplica por (cuarto+1).
    """
    total = 0
    for ch in str(fecha) + str(local):
        total += ord(ch)
    total *= (cuarto + 1)
    return total % 750




