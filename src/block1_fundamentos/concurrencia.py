"""Concurrencia: hilos (I/O-bound) y multiprocessing (CPU-bound)."""
import threading
import time
from multiprocessing import Pool


def descargar(url):
    time.sleep(0.1)  # simula I/O
    return f"descargado {url}"


def demo_threading():
    urls = [f"http://ejemplo.com/{i}" for i in range(5)]
    resultados = []
    hilos = []

    def trabajo(url):
        resultados.append(descargar(url))

    for url in urls:
        h = threading.Thread(target=trabajo, args=(url,))
        hilos.append(h)
        h.start()
    for h in hilos:
        h.join()
    return resultados


def calcular(n):
    return sum(range(n))


def demo_multiprocessing():
    with Pool() as pool:
        return pool.map(calcular, [100000, 200000, 300000])


if __name__ == "__main__":
    print(demo_threading()[:2])
    print(demo_multiprocessing()[:2])
