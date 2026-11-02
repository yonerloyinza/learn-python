"""Builder: consultas SQL dinámicas con filtros opcionales."""


class ConsultaBuilder:
    def __init__(self):
        self._columnas = "*"
        self._tabla = ""
        self._filtros = []

    def columnas(self, columnas):
        self._columnas = columnas
        return self

    def tabla(self, tabla):
        self._tabla = tabla
        return self

    def donde(self, condicion):
        self._filtros.append(condicion)
        return self

    def construir(self):
        sql = f"SELECT {self._columnas} FROM {self._tabla}"
        if self._filtros:
            sql += " WHERE " + " AND ".join(self._filtros)
        return sql


if __name__ == "__main__":
    sql = (ConsultaBuilder()
           .columnas("nombre, edad")
           .tabla("usuarios")
           .donde("edad > 18")
           .donde("activo = 1")
           .construir())
    print(sql)
