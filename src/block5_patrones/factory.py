"""Factory: filtros de reporte según tipo de usuario."""
from abc import ABC, abstractmethod


class Filtro(ABC):
    @abstractmethod
    def aplicar(self, datos):
        pass


class FiltroAdmin(Filtro):
    def aplicar(self, datos):
        return datos


class FiltroUsuario(Filtro):
    def aplicar(self, datos):
        return {k: v for k, v in datos.items() if k != "salario"}


class FiltroFactory:
    @staticmethod
    def crear(tipo):
        if tipo == "admin":
            return FiltroAdmin()
        if tipo == "usuario":
            return FiltroUsuario()
        raise ValueError("Tipo desconocido")


if __name__ == "__main__":
    datos = {"nombre": "Ana", "salario": 5000}
    f = FiltroFactory.crear("usuario")
    print(f.aplicar(datos))
