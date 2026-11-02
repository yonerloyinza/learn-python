"""Command: cola de comandos con deshacer."""
from abc import ABC, abstractmethod


class Comando(ABC):
    @abstractmethod
    def ejecutar(self):
        pass

    @abstractmethod
    def deshacer(self):
        pass


class EscribirTexto(Comando):
    def __init__(self, editor, texto):
        self.editor = editor
        self.texto = texto

    def ejecutar(self):
        self.editor.contenido += self.texto

    def deshacer(self):
        self.editor.contenido = self.editor.contenido[:-len(self.texto)]


class Editor:
    def __init__(self):
        self.contenido = ""
        self.historial = []

    def ejecutar(self, comando: Comando):
        comando.ejecutar()
        self.historial.append(comando)

    def deshacer(self):
        if self.historial:
            self.historial.pop().deshacer()


if __name__ == "__main__":
    editor = Editor()
    editor.ejecutar(EscribirTexto(editor, "hola "))
    print(editor.contenido)
    editor.deshacer()
    print(repr(editor.contenido))
