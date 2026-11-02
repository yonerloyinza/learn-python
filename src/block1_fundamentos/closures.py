"""Closures y ámbito: funciones que capturan variables."""


def hacer_contador():
    """Retorna un contador independiente (closure)."""
    cuenta = 0

    def contador():
        nonlocal cuenta
        cuenta += 1
        return cuenta

    return contador


def multiplicador(factor):
    """Closure que multiplica por un factor dado."""

    def aplicar(valor):
        return valor * factor

    return aplicar


if __name__ == "__main__":
    c1 = hacer_contador()
    c2 = hacer_contador()
    print(c1(), c1(), c2())  # 1, 2, 1
    triplicar = multiplicador(3)
    print(triplicar(5))  # 15
