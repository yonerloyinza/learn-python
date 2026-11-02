"""Strategy: métodos de envío intercambiables."""
from abc import ABC, abstractmethod


class EnvioStrategy(ABC):
    @abstractmethod
    def enviar(self, paquete):
        pass


class Correo(EnvioStrategy):
    def enviar(self, paquete):
        return f"{paquete} por correo"


class Mensajeria(EnvioStrategy):
    def enviar(self, paquete):
        return f"{paquete} por mensajería"


class GestorEnvio:
    def __init__(self, strategy: EnvioStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: EnvioStrategy):
        self.strategy = strategy

    def despachar(self, paquete):
        return self.strategy.enviar(paquete)


if __name__ == "__main__":
    g = GestorEnvio(Correo())
    print(g.despachar("paquete A"))
    g.set_strategy(Mensajeria())
    print(g.despachar("paquete B"))
