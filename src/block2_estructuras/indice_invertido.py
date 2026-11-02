"""Índice invertido: buscador de documentos usando set y dict."""


class IndiceInvertido:
    def __init__(self):
        self.indice = {}  # palabra -> set de ids de documentos

    def indexar(self, doc_id, texto):
        for palabra in texto.lower().split():
            self.indice.setdefault(palabra, set()).add(doc_id)

    def buscar(self, palabra):
        return self.indice.get(palabra.lower(), set())


if __name__ == "__main__":
    idx = IndiceInvertido()
    idx.indexar(1, "Python es un lenguaje excelente")
    idx.indexar(2, "Java y Python son populares")
    print(idx.buscar("python"))  # {1, 2}
