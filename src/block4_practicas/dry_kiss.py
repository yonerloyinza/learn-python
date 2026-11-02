"""DRY / KISS / YAGNI: evitar duplicación y complejidad innecesaria."""


def formato_moneda(valor: float, simbolo: str = "$") -> str:
    """Función única para formatear moneda (DRY)."""
    return f"{simbolo}{valor:,.2f}"


def procesar_pago(monto: float) -> str:
    """Lógica simple sin funcionalidad anticipada (YAGNI + KISS)."""
    if monto <= 0:
        raise ValueError("Monto inválido")
    return formato_moneda(monto)


if __name__ == "__main__":
    print(procesar_pago(1234.5))
