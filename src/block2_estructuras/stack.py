"""Pila (LIFO): validador de paréntesis balanceados."""


class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, valor):
        self.elementos.append(valor)

    def desapilar(self):
        if self.esta_vacia():
            raise IndexError("Pila vacía")
        return self.elementos.pop()

    def esta_vacia(self):
        return len(self.elementos) == 0


def parentesis_balanceados(cadena):
    pares = {")": "(", "]": "[", "}": "{"}
    pila = Pila()
    for char in cadena:
        if char in "([{":
            pila.apilar(char)
        elif char in ")]}":
            if pila.esta_vacia() or pila.desapilar() != pares[char]:
                return False
    return pila.esta_vacia()


if __name__ == "__main__":
    print(parentesis_balanceados("({[]})"))   # True
    print(parentesis_balanceados("({[})"))    # False
