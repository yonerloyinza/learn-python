"""Heap (cola de prioridad): planificador de tareas."""


import heapq


class Planificador:
    def __init__(self):
        self.cola = []

    def agregar(self, prioridad, tarea):
        heapq.heappush(self.cola, (prioridad, tarea))

    def siguiente(self):
        if self.esta_vacia():
            raise IndexError("Sin tareas")
        return heapq.heappop(self.cola)

    def esta_vacia(self):
        return len(self.cola) == 0


if __name__ == "__main__":
    p = Planificador()
    p.agregar(3, "baja")
    p.agregar(1, "alta")
    p.agregar(2, "media")
    print(p.siguiente())  # (1, 'alta')
