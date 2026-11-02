# learn-python

Repositorio de práctica y aprendizaje de Python, organizado en bloques progresivos:

- **Bloque 1** – Fundamentos avanzados del lenguaje (tipado, memoria, closures, decoradores, generadores, concurrencia, asyncio, funcional).
- **Bloque 2** – Estructuras de datos (listas, tuples, sets, dicts, linked list, stack, queue, árbol binario, heap, grafo, hash map).
- **Bloque 3** – Algoritmia y lógica (Big O, recursividad, búsqueda binaria, ordenamiento, BFS).
- **Bloque 4** – Buenas prácticas y calidad (DRY/KISS, manejo de errores, mocks, SOLID, TDD, testing, tipos).
- **Bloque 5** – Patrones de diseño y arquitectura (adapter, builder, clean architecture, command, decorator, factory, mvc, observer, proxy, singleton, strategy).

## Estructura

```
src/           Código fuente por bloque
tests/         Pruebas por bloque
PLAN_APRENDIZAJE_PYTHON.md   Plan de aprendizaje con casos de uso
```

## Requisitos

Python 3.10+. No requiere dependencias externas (solo librería estándar).

## Ejecutar pruebas

```bash
python -m pytest tests/
# o
python -m unittest discover -s tests
```

## Licencia

MIT
