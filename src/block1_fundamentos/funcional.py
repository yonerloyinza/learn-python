"""Funcional: map, filter, reduce y lambdas."""
from functools import reduce


def demo_funcional(datos):
    dobles = list(map(lambda x: x * 2, datos))
    pares = list(filter(lambda x: x % 2 == 0, datos))
    suma = reduce(lambda acc, x: acc + x, datos, 0)
    return dobles, pares, suma


if __name__ == "__main__":
    datos = [1, 2, 3, 4, 5]
    print(demo_funcional(datos))
