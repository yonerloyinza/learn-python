"""Singleton: configuración de aplicación."""


class Configuracion:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._ajustes = {}
        return cls._instancia

    def set(self, clave, valor):
        self._ajustes[clave] = valor

    def get(self, clave):
        return self._ajustes.get(clave)


if __name__ == "__main__":
    c1 = Configuracion()
    c2 = Configuracion()
    c1.set("modo", "produccion")
    print(c1 is c2, c2.get("modo"))  # True produccion
