"""Árbol binario: directorio de archivos jerárquico."""


class NodoArbol:
    def __init__(self, nombre, es_directorio=True):
        self.nombre = nombre
        self.es_directorio = es_directorio
        self.izquierda = None
        self.derecha = None


class Directorio:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, es_directorio=True):
        nuevo = NodoArbol(nombre, es_directorio)
        if not self.raiz:
            self.raiz = nuevo
        else:
            self._insertar_rec(self.raiz, nuevo)

    def _insertar_rec(self, actual, nuevo):
        if nuevo.nombre < actual.nombre:
            if actual.izquierda is None:
                actual.izquierda = nuevo
            else:
                self._insertar_rec(actual.izquierda, nuevo)
        else:
            if actual.derecha is None:
                actual.derecha = nuevo
            else:
                self._insertar_rec(actual.derecha, nuevo)

    def en_orden(self, nodo, resultado=None):
        if resultado is None:
            resultado = []
        if nodo:
            self.en_orden(nodo.izquierda, resultado)
            resultado.append(nodo.nombre)
            self.en_orden(nodo.derecha, resultado)
        return resultado


if __name__ == "__main__":
    d = Directorio()
    for nombre in ["documentos", "archivos", "imagenes", "descargas"]:
        d.insertar(nombre)
    print(d.en_orden(d.raiz))
