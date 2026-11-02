"""Type hints y docstrings: contratos claros entre módulos."""
from typing import List, Optional


def calcular_total(precios: List[float], descuento: Optional[float] = None) -> float:
    """Calcula el total de una lista de precios.

    Args:
        precios: Lista de valores numéricos positivos.
        descuento: Porcentaje de descuento entre 0 y 100, opcional.

    Returns:
        Total con descuento aplicado si se proporciona.
    """
    total = sum(precios)
    if descuento is not None:
        total *= (1 - descuento / 100)
    return round(total, 2)


if __name__ == "__main__":
    print(calcular_total([10.0, 20.0, 30.0], descuento=10))  # 54.0
