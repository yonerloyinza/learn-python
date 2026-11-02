"""MVC: app web simple separando modelo, vista y controlador."""


class Modelo:
    def __init__(self):
        self.mensaje = "Hola MVC"


class Vista:
    def render(self, mensaje):
        return f"<html><body>{mensaje}</body></html>"


class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def manejar(self):
        return self.vista.render(self.modelo.mensaje)


if __name__ == "__main__":
    c = Controlador(Modelo(), Vista())
    print(c.manejar())
