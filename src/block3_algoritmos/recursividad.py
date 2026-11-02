"""Recursividad: factorial y recorrido de árbol de carpetas."""


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def listar_carpeta(ruta, nivel=0):
    import os
    print("  " * nivel + ruta)
    try:
        for entrada in os.listdir(ruta):
            camino = os.path.join(ruta, entrada)
            if os.path.isdir(camino):
                listar_carpeta(camino, nivel + 1)
    except PermissionError:
        pass


if __name__ == "__main__":
    print(factorial(5))  # 120
