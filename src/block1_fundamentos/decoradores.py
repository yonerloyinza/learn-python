"""Decoradores: logger de ejecución y medición de tiempos."""
import functools
import time


def logger(func):
    @functools.wraps(func)
    def envoltura(*args, **kwargs):
        print(f"Llamando {func.__name__}")
        return func(*args, **kwargs)

    return envoltura


def medir_tiempo(func):
    @functools.wraps(func)
    def envoltura(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fin = time.perf_counter()
        print(f"{func.__name__} tardó {(fin - inicio) * 1000:.2f} ms")
        return resultado

    return envoltura


@logger
@medir_tiempo
def procesar(n):
    return sum(range(n))


if __name__ == "__main__":
    procesar(100000)
