"""Manejo de errores: servicio robusto ante fallos de red."""
import time


class ErrorRed(Exception):
    pass


def consultar_servicio(intento=1, maximo=3):
    try:
        if intento < maximo:
            raise ErrorRed("timeout")
        return "datos"
    except ErrorRed as e:
        if intento >= maximo:
            raise
        time.sleep(0.1)
        return consultar_servicio(intento + 1, maximo)


if __name__ == "__main__":
    print(consultar_servicio())  # datos tras reintentos
