"""Tests Bloque 1: Fundamentos avanzados."""
import unittest
import sys
import gc
from src.block1_fundamentos.memoria import Objeto, demo_referencias, demo_gc_ciclico
from src.block1_fundamentos.closures import hacer_contador, multiplicador
from src.block1_fundamentos.decoradores import procesar
from src.block1_fundamentos.funcional import demo_funcional


class TestMemoria(unittest.TestCase):
    def test_objeto_liberado(self):
        obj = Objeto("X")
        self.assertEqual(obj.nombre, "X")


class TestClosures(unittest.TestCase):
    def test_contadores_independientes(self):
        c1 = hacer_contador()
        c2 = hacer_contador()
        self.assertEqual(c1(), 1)
        self.assertEqual(c1(), 2)
        self.assertEqual(c2(), 1)

    def test_multiplicador(self):
        triplicar = multiplicador(3)
        self.assertEqual(triplicar(5), 15)


class TestDecoradores(unittest.TestCase):
    def test_procesar_devuelve_suma(self):
        self.assertEqual(procesar(3), 3)  # 0+1+2


class TestFuncional(unittest.TestCase):
    def test_map_filter_reduce(self):
        dobles, pares, suma = demo_funcional([1, 2, 3, 4, 5])
        self.assertEqual(dobles, [2, 4, 6, 8, 10])
        self.assertEqual(pares, [2, 4])
        self.assertEqual(suma, 15)


if __name__ == "__main__":
    unittest.main()
