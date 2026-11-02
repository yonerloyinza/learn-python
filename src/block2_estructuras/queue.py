"""Cola (FIFO) con deque: cola de impresión."""


from collections import deque


class ColaImpresion:
    def __init__(self):
        self.cola = deque()

    def encolar(self, documento):
        self.cola.append(documento)

    def descolar(self):
        if self.esta_vacia():
            raise IndexError("Cola vacía")
        return self.cola.popleft()

    def esta_vacia(self):
        return len(self.cola) == 0


if __name__ == "__main__":
    c = ColaImpresion()
    for doc in ["doc1.pdf", "doc2.pdf", "doc3.pdf"]:
        c.encolar(doc)
    print(c.descolar())  # doc1.pdf
