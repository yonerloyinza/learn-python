"""Tests Bloque 2: Estructuras de datos."""
import unittest
from src.block2_estructuras.indice_invertido import IndiceInvertido
from src.block2_estructuras.linked_list import ListaEnlazada
from src.block2_estructuras.stack import Pila, parentesis_balanceados
from src.block2_estructuras.queue import ColaImpresion
from src.block2_estructuras.binary_tree import Directorio
from src.block2_estructuras.heap import Planificador
from src.block2_estructuras.grafo import Grafo
from src.block2_estructuras.hash_map import Caché


class TestIndiceInvertido(unittest.TestCase):
    def test_buscar(self):
        idx = IndiceInvertido()
        idx.indexar(1, "Python es genial")
        idx.indexar(2, "Java y Python")
        self.assertEqual(idx.buscar("python"), {1, 2})
        self.assertEqual(idx.buscar("ruby"), set())


class TestLinkedList(unittest.TestCase):
    def test_agregar_y_listar(self):
        l = ListaEnlazada()
        l.agregar("a")
        l.agregar("b")
        self.assertEqual(l.a_lista(), ["a", "b"])


class TestStack(unittest.TestCase):
    def test_parentesis_balanceados(self):
        self.assertTrue(parentesis_balanceados("({[]})"))
        self.assertFalse(parentesis_balanceados("({[})"))


class TestQueue(unittest.TestCase):
    def test_fifo(self):
        c = ColaImpresion()
        c.encolar("d1")
        c.encolar("d2")
        self.assertEqual(c.descolar(), "d1")


class TestBinaryTree(unittest.TestCase):
    def test_en_orden(self):
        d = Directorio()
        for n in ["b", "a", "c"]:
            d.insertar(n)
        self.assertEqual(d.en_orden(d.raiz), ["a", "b", "c"])


class TestHeap(unittest.TestCase):
    def test_prioridad(self):
        p = Planificador()
        p.agregar(3, "baja")
        p.agregar(1, "alta")
        self.assertEqual(p.siguiente(), (1, "alta"))


class TestGrafo(unittest.TestCase):
    def test_bfs_dfs(self):
        g = Grafo()
        for a, b in [("A", "B"), ("A", "C")]:
            g.agregar_arista(a, b)
        self.assertIn("A", g.bfs("A"))
        self.assertIn("A", g.dfs("A"))


class TestHashMap(unittest.TestCase):
    def test_capacidad(self):
        c = Caché(capacidad=2)
        c.guardar("a", 1)
        c.guardar("b", 2)
        c.guardar("c", 3)
        self.assertIsNone(c.obtener("a"))
        self.assertEqual(c.obtener("b"), 2)


if __name__ == "__main__":
    unittest.main()
