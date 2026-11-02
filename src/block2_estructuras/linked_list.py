"""Lista enlazada simple: historial con nodos."""


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def a_lista(self):
        resultado = []
        actual = self.cabeza
        while actual:
            resultado.append(actual.valor)
            actual = actual.siguiente
        return resultado


if __name__ == "__main__":
    historial = ListaEnlazada()
    for pagina in ["inicio", "productos", "contacto"]:
        historial.agregar(pagina)
    print(historial.a_lista())
