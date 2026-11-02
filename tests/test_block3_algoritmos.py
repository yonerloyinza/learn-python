"""Tests Bloque 3: Algoritmia."""
import unittest
from src.block3_algoritmos.buscar import busqueda_lineal, busqueda_binaria
from src.block3_algoritmos.recursividad import factorial
from src.block3_algoritmos.ordenamiento import quicksort, mergesort, bubble_sort
from src.block3_algoritmos.recorridos import Grafo, ruta_mas_corta
from src.block3_algoritmos.dp import cambio_minimo


class TestBusqueda(unittest.TestCase):
    def setUp(self):
        self.datos = list(range(100))

    def test_lineal(self):
        self.assertEqual(busqueda_lineal(self.datos, 50), 50)
        self.assertEqual(busqueda_lineal(self.datos, 999), -1)

    def test_binaria(self):
        self.assertEqual(busqueda_binaria(self.datos, 50), 50)
        self.assertEqual(busqueda_binaria(self.datos, 999), -1)


class TestRecursividad(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)


class TestOrdenamiento(unittest.TestCase):
    def test_todos_ordenan(self):
        datos = [3, 1, 4, 1, 5, 9, 2, 6]
        esperado = sorted(datos)
        self.assertEqual(quicksort(datos), esperado)
        self.assertEqual(mergesort(datos), esperado)
        self.assertEqual(bubble_sort(datos), esperado)


class TestRecorridos(unittest.TestCase):
    def test_ruta_mas_corta(self):
        g = Grafo()
        for a, b in [("A", "B"), ("B", "D"), ("A", "C"), ("C", "D")]:
            g.agregar_arista(a, b)
        self.assertEqual(ruta_mas_corta(g, "A", "D"), ["A", "B", "D"])


class TestDP(unittest.TestCase):
    def test_cambio_minimo(self):
        self.assertEqual(cambio_minimo([1, 5, 10, 25], 30), 2)


if __name__ == "__main__":
    unittest.main()
