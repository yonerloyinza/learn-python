"""Adapter: integrar librería de pago de terceros con interfaz distinta."""


class PagoTercero:
    def procesar_tarjeta(self, numero, monto):
        return {"ok": True, "transaccion": "T123"}


class AdaptadorPago:
    def __init__(self, servicio_tercero):
        self.servicio = servicio_tercero

    def pagar(self, tarjeta, monto):
        resultado = self.servicio.procesar_tarjeta(tarjeta, monto)
        return resultado["ok"], resultado["transaccion"]


if __name__ == "__main__":
    adap = AdaptadorPago(PagoTercero())
    print(adap.pagar("4111...", 100))
