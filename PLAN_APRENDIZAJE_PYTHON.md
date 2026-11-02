# Plan de aprendizaje Python — directo al grano (por casos de uso)

Bloques progresivos: fundamentos → estructuras de datos → algoritmos → buenas prácticas → patrones y arquitectura.

## Bloque 1. Fundamentos avanzados del lenguaje

| Tema | Concepto clave | Caso de uso / Ejercicio |
|------|---------------|-------------------------|
| Tipado dinámico y fuerte | Todo es objeto; tipos se resuelven en runtime | Validador de entrada de API que rechace tipos incorrectos sin crashes |
| Gestión de memoria | Stack vs heap, reference counting, GC, `gc` module | Contador de objetos vivos en un procesamiento de lotes grande |
| Ámbito y closures | `nonlocal`/`global`, funciones que capturan variables | Generador de contadores independientes por cliente |
| Decoradores | Funciones que envuelven funciones | Logger de ejecución y medición de tiempos en endpoints |
| Generadores e iteradores | `yield`, lazy evaluation, protocol iterator | Lectura de archivo CSV de 2 GB sin cargarlo en memoria |
| Concurrencia: threading | GIL, hilos para I/O-bound | Descarga paralela de 100 URLs |
| Concurrencia: multiprocessing | Evita el GIL para CPU-bound | Procesamiento de imágenes en paralelo |
| Async / await | `asyncio`, event loop, corrutinas | Servidor de chat con miles de conexiones concurrentes |
| Funcional: map/filter/reduce, lambdas | Funciones de orden superior | Pipeline de transformación de datos de sensores |

## Bloque 2. Estructuras de datos

| Tema | Concepto clave | Caso de uso / Ejercicio |
|------|---------------|-------------------------|
| Listas / Tuples / Sets / Dicts | Secuencias, hash maps, unicidad | Índice invertido de un buscador de documentos |
| Linked list | Nodos con punteros, inserción O(1) | Historial de navegación con deshacer/rehacer |
| Stack | LIFO | Validador de paréntesis balanceados en código |
| Queue / deque | FIFO, extremos dobles | Cola de impresión de documentos |
| Árbol binario | Nodos, raíz, hojas, recorridos | Directorio de archivos jerárquico |
| Heap | Cola de prioridad | Planificador de tareas por prioridad |
| Grafo | Nodos y aristas, dirigido/no dirigido | Mapa de redes sociales o rutas de transporte |
| Hash map | Diccionarios, colisiones, O(1) promedio | Caché de resultados de consultas costosas |

## Bloque 3. Algoritmia y lógica

| Tema | Concepto clave | Caso de uso / Ejercicio |
|------|---------------|-------------------------|
| Big O | Complejidad temporal y espacial | Comparar búsqueda lineal vs binaria en 1M de registros |
| Recursividad | Caso base, caso recursivo, stack overflow | Cálculo de factorial y recorrido de árbol de carpetas |
| Búsqueda binaria | Divide y vencerás, lista ordenada | Buscar precio en catálogo ordenado |
| Ordenamiento | Quicksort, Mergesort, Timsort (Python) | Ordenar transacciones por fecha y monto |
| BFS | Cola (queue), recorrido por niveles | Ruta más corta entre dos estaciones de metro |
| DFS | Pila (stack), recorrido en profundidad | Detector de ciclos en dependencias de paquetes |
| Programación dinámica | Memoización, subproblemas superpuestos | Cambio mínimo de monedas |

## Bloque 4. Buenas prácticas y calidad

| Tema | Concepto clave | Caso de uso / Ejercicio |
|------|---------------|-------------------------|
| PEP 8 / estilo | Formato consistente | Linter y formateador en un paquete reusable |
| Docstrings y type hints | Documentación y tipado estático opcional | API interna con contratos claros entre equipos |
| SOLID | Responsabilidad única, abierto/cerrado, etc. | Refactorizar script monolítico a módulos acoplados |
| DRY / KISS / YAGNI | Sin repetición, simple, nada innecesario | Eliminar código duplicado en reportes mensuales |
| Testing unitario | `pytest`, asserts, fixtures | Pruebas para funciones de cálculo financiero |
| TDD | Escribir prueba primero | Desarrollar carrito de compras por pruebas |
| Mocks | Simular dependencias externas | Probar integración con API externa sin llamadas reales |
| Manejo de errores | `try/except/finally`, excepciones personalizadas | Servicio robusto que no cae ante fallos de red |

## Bloque 5. Patrones de diseño y arquitectura

| Tema | Concepto clave | Caso de uso / Ejercicio |
|------|---------------|-------------------------|
| Singleton | Una única instancia global | Configuración de aplicación (settings) |
| Factory | Creación de objetos sin exponer lógica | Filtros de reporte según tipo de usuario |
| Builder | Construcción paso a paso de objetos complejos | Consultas SQL dinámicas con muchos filtros opcionales |
| Adapter | Interfaz incompatible hecha compatible | Integrar librería de pago de terceros |
| Decorator | Añadir comportamiento en runtime | Control de acceso (auth) en métodos |
| Proxy | Placeholder que controla acceso | Carga perezosa de imágenes grandes |
| Observer | Sujeto y suscriptores | Notificaciones al cambiar estado de orden |
| Strategy | Algoritmos intercambiables | Métodos de envío distintos (correo, mensajería) |
| Command | Encapsular solicitud como objeto | Cola de comandos con deshacer en editor de texto |
| Clean Architecture / Capas | Separación de dominio, infraestructura, presentación | Reestructurar app en capas independientes de framework |
| MVC | Modelo, vista, controlador | App web con Flask/Django separando lógica y plantillas |

### Hoja de ruta sugerida (8 semanas)

1. Semana 1: Bloque 1 (tipado, memoria, decoradores, generadores)
2. Semana 2: Bloque 1 (concurrencia, async, funcional)
3. Semana 3: Bloque 2 (lineales + diccionarios/sets)
4. Semana 4: Bloque 2 (árboles, heaps, grafos)
5. Semana 5: Bloque 3 (Big O, recursividad, búsqueda, ordenamiento, BFS/DFS)
6. Semana 6: Bloque 3 (DP) + Bloque 4 (estilo, tipos, SOLID, pruebas)
7. Semana 7: Bloque 4 (TDD, mocks, manejo de errores) + Bloque 5 (patrones creacionales/estructurales)
8. Semana 8: Bloque 5 (patrones de comportamiento, arquitectura, proyecto final)

### Proyecto final sugerido

Sistema de procesamiento de pedidos: lectura de CSV masivo (generadores), validación con type hints, descuentos con Strategy, persistencia con Repository, notificaciones con Observer, tests con pytest/unittest, expuesto como API async con FastAPI.

---

## Referencias de implementación

Cada tema tiene su ejemplo de código y su test correspondiente:

| Bloque | Código fuente | Tests |
|--------|--------------|-------|
| 1. Fundamentos avanzados | `src/block1_fundamentos/` | `tests/test_block1_fundamentos.py` |
| 2. Estructuras de datos | `src/block2_estructuras/` | `tests/test_block2_estructuras.py` |
| 3. Algoritmia | `src/block3_algoritmos/` | `tests/test_block3_algoritmos.py` |
| 4. Buenas prácticas | `src/block4_practicas/` | `tests/test_block4_practicas.py` |
| 5. Patrones y arquitectura | `src/block5_patrones/` | `tests/test_block5_patrones.py` |

### Ejecutar los tests

```bash
python3 -m unittest discover -s tests -v
```

Total: 39 tests, todos pasando.
