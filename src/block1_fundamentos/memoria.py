"""Gestión de memoria: contado de referencias y GC."""
import gc
import sys


class Objeto:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def __del__(self):
        print(f"Liberado: {self.nombre}")


def demo_referencias():
    """Demuestra conteo de referencias y liberación por GC."""
    a = Objeto("A")
    b = a  # misma referencia, refcount = 2
    print(f"refcount A: {sys.getrefcount(a) - 1}")
    del b
    print(f"refcount tras del b: {sys.getrefcount(a) - 1}")
    del a  # refcount 0 -> __del__ se ejecuta


def demo_gc_ciclico():
    """Referencias cíclicas requieren del recolector de basura."""
    class Nodo:
        def __init__(self, valor):
            self.valor = valor
            self.ref = None

    x = Nodo(1)
    y = Nodo(2)
    x.ref = y
    y.ref = x  # ciclo
    del x, y
    gc.collect()


if __name__ == "__main__":
    demo_referencias()
    demo_gc_ciclico()
