"""Tests Bloque 4: Buenas prácticas y calidad."""
import unittest
from src.block4_practicas.tipos import calcular_total
from src.block4_practicas.solid import GeneradorReportes, ReportePDF, ReporteCSV
from src.block4_practicas.dry_kiss import procesar_pago, formato_moneda
from src.block4_practicas.tdd_ejemplo import Carrito
from src.block4_practicas.errores import consultar_servicio


class TestTipos(unittest.TestCase):
    def test_sin_descuento(self):
        self.assertEqual(calcular_total([10.0, 20.0]), 30.0)

    def test_con_descuento(self):
        self.assertEqual(calcular_total([10.0, 20.0, 30.0], descuento=10), 54.0)


class TestSOLID(unittest.TestCase):
    def test_pdf(self):
        g = GeneradorReportes(ReportePDF())
        self.assertIn("PDF", g.ejecutar({"id": 1}))

    def test_csv(self):
        g = GeneradorReportes(ReporteCSV())
        self.assertIn("CSV", g.ejecutar({"id": 1}))


class TestDRYKISS(unittest.TestCase):
    def test_moneda(self):
        self.assertEqual(formato_moneda(1234.5), "$1,234.50")

    def test_pago_valido(self):
        self.assertEqual(procesar_pago(100), "$100.00")

    def test_pago_invalido(self):
        with self.assertRaises(ValueError):
            procesar_pago(-10)


class TestCarrito(unittest.TestCase):
    def test_total(self):
        c = Carrito()
        c.agregar("pan", 10)
        c.agregar("leche", 20)
        self.assertEqual(c.total(), 30)


class TestErrores(unittest.TestCase):
    def test_reintento(self):
        self.assertEqual(consultar_servicio(intento=1, maximo=3), "datos")


if __name__ == "__main__":
    unittest.main()
