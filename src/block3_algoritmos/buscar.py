"""Complejidad algorítmica: comparativa de búsqueda lineal vs binaria."""


def busqueda_lineal(lista, objetivo):
    for i, valor in enumerate(lista):
        if valor == objetivo:
            return i
    return -1


def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1


if __name__ == "__main__":
    datos = list(range(1_000_000))
    print(busqueda_binaria(datos, 999999))  # 999999
