"""Decorator: control de acceso (auth) en métodos."""


def requiere_auth(func):
    def envoltura(self, *args, **kwargs):
        if not getattr(self, "autenticado", False):
            raise PermissionError("No autenticado")
        return func(self, *args, **kwargs)
    return envoltura


class Servicio:
    def __init__(self):
        self.autenticado = False

    @requiere_auth
    def dato_sensible(self):
        return "secreto"


if __name__ == "__main__":
    s = Servicio()
    try:
        s.dato_sensible()
    except PermissionError as e:
        print(e)
    s.autenticado = True
    print(s.dato_sensible())
