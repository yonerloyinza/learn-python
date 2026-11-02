"""Clean Architecture: separación de dominio, infraestructura y presentación."""
from abc import ABC, abstractmethod


class Pedido:
    def __init__(self, id, monto, estado="pendiente"):
        self.id = id
        self.monto = monto
        self.estado = estado


class RepositorioPedidos(ABC):
    @abstractmethod
    def guardar(self, pedido: Pedido):
        pass


class RepositorioEnMemoria(RepositorioPedidos):
    def __init__(self):
        self.pedidos = {}

    def guardar(self, pedido: Pedido):
        self.pedidos[pedido.id] = pedido


class ProcesarPedido:
    def __init__(self, repo: RepositorioPedidos):
        self.repo = repo

    def ejecutar(self, id, monto):
        pedido = Pedido(id, monto)
        pedido.estado = "procesado"
        self.repo.guardar(pedido)
        return pedido


if __name__ == "__main__":
    repo = RepositorioEnMemoria()
    caso = ProcesarPedido(repo)
    p = caso.ejecutar(1, 100.0)
    print(p.id, p.estado)
