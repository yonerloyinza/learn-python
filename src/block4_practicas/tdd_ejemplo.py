"""TDD: carrito de compras desarrollado por pruebas."""
import unittest


class Carrito:
    def __init__(self):
        self.items = []

    def agregar(self, producto, precio):
        self.items.append((producto, precio))

    def total(self):
        return sum(precio for _, precio in self.items)


class TestCarrito(unittest.TestCase):
    def test_total_vacio(self):
        c = Carrito()
        self.assertEqual(c.total(), 0)

    def test_agregar_items(self):
        c = Carrito()
        c.agregar("pan", 10)
        c.agregar("leche", 20)
        self.assertEqual(c.total(), 30)


if __name__ == "__main__":
    unittest.main()
