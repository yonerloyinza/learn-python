"""Hash map: caché de resultados costosos."""


class Caché:
    def __init__(self, capacidad=128):
        self.capacidad = capacidad
        self.datos = {}
        self.orden = []

    def obtener(self, clave):
        return self.datos.get(clave)

    def guardar(self, clave, valor):
        if clave in self.datos:
            self.datos[clave] = valor
            return
        if len(self.datos) >= self.capacidad:
            antigua = self.orden.pop(0)
            del self.datos[antigua]
        self.datos[clave] = valor
        self.orden.append(clave)


if __name__ == "__main__":
    c = Caché(capacidad=2)
    c.guardar("a", 1)
    c.guardar("b", 2)
    print(c.obtener("a"))  # 1
    c.guardar("c", 3)      # expulsa 'a'
    print(c.obtener("a"))  # None
