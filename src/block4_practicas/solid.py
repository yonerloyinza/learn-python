"""SOLID: Responsabilidad única y Abierto/Cerrado en procesamiento de reportes."""
from abc import ABC, abstractmethod


class Reporte(ABC):
    @abstractmethod
    def generar(self, datos: dict) -> str:
        pass


class ReportePDF(Reporte):
    def generar(self, datos: dict) -> str:
        return f"PDF: {datos}"


class ReporteCSV(Reporte):
    def generar(self, datos: dict) -> str:
        return f"CSV: {datos}"


class GeneradorReportes:
    """Responsabilidad única: solo coordina la generación."""

    def __init__(self, reporte: Reporte):
        self.reporte = reporte

    def ejecutar(self, datos: dict) -> str:
        return self.reporte.generar(datos)


if __name__ == "__main__":
    g = GeneradorReportes(ReportePDF())
    print(g.ejecutar({"id": 1}))
