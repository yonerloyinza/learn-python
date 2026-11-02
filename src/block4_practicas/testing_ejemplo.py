"""Testing unitario con unittest: funciones de cálculo financiero."""
import unittest
from src.block4_practicas.tipos import calcular_total


class TestCalculoFinanciero(unittest.TestCase):
    def test_sin_descuento(self):
        self.assertEqual(calcular_total([10.0, 20.0]), 30.0)

    def test_con_descuento(self):
        self.assertEqual(calcular_total([10.0, 20.0, 30.0], descuento=10), 54.0)

    def test_lista_vacia(self):
        self.assertEqual(calcular_total([]), 0.0)


if __name__ == "__main__":
    unittest.main()
