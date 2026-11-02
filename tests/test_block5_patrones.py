"""Tests Bloque 5: Patrones de diseño y arquitectura."""
import unittest
from src.block5_patrones.singleton import Configuracion
from src.block5_patrones.factory import FiltroFactory
from src.block5_patrones.builder import ConsultaBuilder
from src.block5_patrones.adapter import AdaptadorPago, PagoTercero
from src.block5_patrones.decorator import Servicio
from src.block5_patrones.proxy import ProxyImagen
from src.block5_patrones.observer import Orden, EmailNotifier
from src.block5_patrones.strategy import GestorEnvio, Correo, Mensajeria
from src.block5_patrones.command import Editor, EscribirTexto
from src.block5_patrones.clean_architecture import ProcesarPedido, RepositorioEnMemoria
from src.block5_patrones.mvc import Controlador, Modelo, Vista


class TestSingleton(unittest.TestCase):
    def test_unica_instancia(self):
        c1 = Configuracion()
        c2 = Configuracion()
        self.assertIs(c1, c2)


class TestFactory(unittest.TestCase):
    def test_filtro_usuario(self):
        f = FiltroFactory.crear("usuario")
        datos = {"nombre": "Ana", "salario": 5000}
        self.assertNotIn("salario", f.aplicar(datos))


class TestBuilder(unittest.TestCase):
    def test_sql(self):
        sql = (ConsultaBuilder()
               .columnas("nombre")
               .tabla("usuarios")
               .donde("edad > 18")
               .construir())
        self.assertIn("WHERE", sql)


class TestAdapter(unittest.TestCase):
    def test_pagar(self):
        adap = AdaptadorPago(PagoTercero())
        ok, tx = adap.pagar("4111", 100)
        self.assertTrue(ok)


class TestDecorator(unittest.TestCase):
    def test_requiere_auth(self):
        s = Servicio()
        with self.assertRaises(PermissionError):
            s.dato_sensible()
        s.autenticado = True
        self.assertEqual(s.dato_sensible(), "secreto")


class TestProxy(unittest.TestCase):
    def test_mostrar(self):
        p = ProxyImagen("foto.jpg")
        self.assertIsNotNone(p)


class TestObserver(unittest.TestCase):
    def test_notificacion(self):
        orden = Orden()
        orden.suscribir(EmailNotifier())
        try:
            orden.cambiar_estado("enviado")
        except Exception:
            self.fail("Observer no debería fallar")


class TestStrategy(unittest.TestCase):
    def test_cambio_estrategia(self):
        g = GestorEnvio(Correo())
        self.assertEqual(g.despachar("p"), "p por correo")
        g.set_strategy(Mensajeria())
        self.assertEqual(g.despachar("p"), "p por mensajería")


class TestCommand(unittest.TestCase):
    def test_deshacer(self):
        editor = Editor()
        editor.ejecutar(EscribirTexto(editor, "hola"))
        self.assertEqual(editor.contenido, "hola")
        editor.deshacer()
        self.assertEqual(editor.contenido, "")


class TestCleanArchitecture(unittest.TestCase):
    def test_procesar(self):
        repo = RepositorioEnMemoria()
        caso = ProcesarPedido(repo)
        p = caso.ejecutar(1, 100.0)
        self.assertEqual(p.estado, "procesado")


class TestMVC(unittest.TestCase):
    def test_render(self):
        c = Controlador(Modelo(), Vista())
        html = c.manejar()
        self.assertIn("Hola MVC", html)


if __name__ == "__main__":
    unittest.main()
