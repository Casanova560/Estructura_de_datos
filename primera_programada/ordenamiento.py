from comparator import PlayComparator

def burbuja(lista):
    comparaciones = 0
    intercambios = 0
    comparator = PlayComparator()

    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            comparaciones += 1
            if comparator.compare(lista[j], lista[j+1]) > 0:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambios += 1

    return lista, comparaciones, intercambios

def insercion(lista):
    comparaciones = 0
    intercambios = 0

    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            comparaciones += 1
            lista[j + 1] = lista[j]
            intercambios += 1
            j -= 1
        lista[j + 1] = key

    return lista, comparaciones, intercambios

def merge_sort(lista):
    comparator = PlayComparator()
    comparaciones = 0

    def merge(left, right):
        nonlocal comparaciones
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            comparaciones += 1
            if comparator.compare(left[i], right[j]) <= 0:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    if len(lista) <= 1:
        return lista, comparaciones, 0

    mid = len(lista) // 2
    left, lc, _ = merge_sort(lista[:mid])
    right, rc, _ = merge_sort(lista[mid:])
    merged = merge(left, right)
    comparaciones += lc + rc

    return merged, comparaciones, 0


def quick_sort(lista):
    comparator = PlayComparator()
    comparaciones = 0
    intercambios = 0

    def partition(low, high):
        nonlocal comparaciones, intercambios
        pivot = lista[high]
        i = low - 1
        for j in range(low, high):
            comparaciones += 1
            if comparator.compare(lista[j], pivot) <= 0:
                i += 1
                if i != j:
                    lista[i], lista[j] = lista[j], lista[i]
                    intercambios += 1
        if i + 1 != high:
            lista[i+1], lista[high] = lista[high], lista[i+1]
            intercambios += 1
        return i + 1

    def quicksort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quicksort_recursive(low, pi - 1)
            quicksort_recursive(pi + 1, high)

    quicksort_recursive(0, len(lista) - 1)
    return lista, comparaciones, intercambios
