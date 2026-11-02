"""Proxy: carga perezosa de imágenes grandes."""


class Imagen:
    def mostrar(self):
        print("Mostrando imagen")


class ProxyImagen:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self._imagen = None

    def mostrar(self):
        if self._imagen is None:
            self._imagen = Imagen()
            print(f"Cargando {self.nombre_archivo}")
        self._imagen.mostrar()


if __name__ == "__main__":
    p = ProxyImagen("foto.jpg")
    p.mostrar()
