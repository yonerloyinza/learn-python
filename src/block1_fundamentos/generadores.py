"""Generadores e iteradores: lectura lazy de archivos grandes."""


def leer_lineas(ruta_archivo):
    """Generador que lee un archivo línea por línea sin cargarlo en memoria."""
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        for linea in f:
            yield linea.rstrip("\n")


def filtrar_lineas(lineas, palabra):
    """Generador que filtra líneas que contienen una palabra."""
    for linea in lineas:
        if palabra.lower() in linea.lower():
            yield linea


if __name__ == "__main__":
    ruta = "/tmp/datos.txt"
    with open(ruta, "w") as f:
        f.write("error: fallo de red\nok: todo bien\nerror: timeout\n")

    lineas = leer_lineas(ruta)
    errores = filtrar_lineas(lineas, "error")
    for e in errores:
        print(e)
