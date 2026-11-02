"""Grafo: mapa de redes sociales o rutas de transporte."""


from collections import deque, defaultdict


class Grafo:
    def __init__(self, dirigido=False):
        self.adyacencia = defaultdict(list)
        self.dirigido = dirigido

    def agregar_arista(self, origen, destino):
        self.adyacencia[origen].append(destino)
        if not self.dirigido:
            self.adyacencia[destino].append(origen)

    def bfs(self, inicio):
        visitados = set()
        cola = deque([inicio])
        orden = []
        while cola:
            nodo = cola.popleft()
            if nodo not in visitados:
                visitados.add(nodo)
                orden.append(nodo)
                for vecino in self.adyacencia[nodo]:
                    if vecino not in visitados:
                        cola.append(vecino)
        return orden

    def dfs(self, inicio, visitados=None, orden=None):
        if visitados is None:
            visitados = set()
        if orden is None:
            orden = []
        visitados.add(inicio)
        orden.append(inicio)
        for vecino in self.adyacencia[inicio]:
            if vecino not in visitados:
                self.dfs(vecino, visitados, orden)
        return orden


if __name__ == "__main__":
    g = Grafo()
    for a, b in [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")]:
        g.agregar_arista(a, b)
    print(g.bfs("A"))   # ['A', 'B', 'C', 'D']
    print(g.dfs("A"))   # ['A', 'B', 'D', 'C']
