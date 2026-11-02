"""Algoritmos de ordenamiento: Quicksort, Mergesort, Bubble sort."""


def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivote]
    medio = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    return quicksort(izquierda) + medio + quicksort(derecha)


def mergesort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = mergesort(lista[:medio])
    derecha = mergesort(lista[medio:])
    return _mezclar(izquierda, derecha)


def _mezclar(a, b):
    resultado = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            resultado.append(a[i])
            i += 1
        else:
            resultado.append(b[j])
            j += 1
    resultado.extend(a[i:])
    resultado.extend(b[j:])
    return resultado


def bubble_sort(lista):
    a = lista[:]
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


if __name__ == "__main__":
    datos = [3, 1, 4, 1, 5, 9, 2, 6]
    print(quicksort(datos))
    print(mergesort(datos))
    print(bubble_sort(datos))
