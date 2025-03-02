def compute_hash(fecha, cuarto, local):
    total = 0
    for ch in str(fecha) + str(local):
        total += ord(ch)
    total *= (cuarto + 1)
    return total % 750




