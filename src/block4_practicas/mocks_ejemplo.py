"""Mocks: simular llamada a API externa sin red."""
from unittest.mock import patch
import unittest


def obtener_precio_externo(producto):
    """Simula llamada a API externa."""
    import urllib.request
    with urllib.request.urlopen(f"https://api.ejemplo.com/precio/{producto}") as r:
        return int(r.read())


def calcular_con_impuesto(producto, impuesto=0.19):
    precio = obtener_precio_externo(producto)
    return precio * (1 + impuesto)


class TestConMock(unittest.TestCase):
    @patch("src.block4_practicas.mocks_ejemplo.obtener_precio_externo")
    def test_calculo(self, mock_obtener):
        mock_obtener.return_value = 100
        resultado = calcular_con_impuesto("libro")
        self.assertEqual(resultado, 119.0)


if __name__ == "__main__":
    unittest.main()
