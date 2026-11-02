"""Programación dinámica: cambio mínimo de monedas con memoización."""


def cambio_minimo(monedas, monto, memo=None):
    if memo is None:
        memo = {}
    if monto == 0:
        return 0
    if monto in memo:
        return memo[monto]
    minimo = float("inf")
    for moneda in monedas:
        if moneda <= monto:
            res = 1 + cambio_minimo(monedas, monto - moneda, memo)
            if res < minimo:
                minimo = res
    memo[monto] = minimo
    return minimo


if __name__ == "__main__":
    print(cambio_minimo([1, 5, 10, 25], 30))  # 2 (25 + 5)
