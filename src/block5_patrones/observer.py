"""Observer: notificaciones al cambiar estado de orden."""


class Orden:
    def __init__(self):
        self._observadores = []
        self._estado = "pendiente"

    def suscribir(self, observador):
        self._observadores.append(observador)

    def cambiar_estado(self, nuevo):
        self._estado = nuevo
        for obs in self._observadores:
            obs.actualizar(nuevo)


class EmailNotifier:
    def actualizar(self, estado):
        print(f"Email: orden ahora {estado}")


class SmsNotifier:
    def actualizar(self, estado):
        print(f"SMS: orden ahora {estado}")


if __name__ == "__main__":
    orden = Orden()
    orden.suscribir(EmailNotifier())
    orden.suscribir(SmsNotifier())
    orden.cambiar_estado("enviado")
