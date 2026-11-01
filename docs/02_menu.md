# Ejercicio 2 — Menú modular

Una lista de diccionarios conserva los tickets hasta salir. El menú permite registrar, listar, buscar por solicitante y contar por prioridad. La búsqueda compara texto sin distinguir mayúsculas y minúsculas.

## Comprobación reproducible

```sh
python3 02_menu_helpdesk.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_02_menu.py' -v
```

El usuario puede registrar varios tickets desde la opción 1, buscar por la 3 y consultar las estadísticas con la 4. La prueba específica cubre una opción inválida, lista vacía, búsqueda sin coincidencias y cierre de entrada durante el registro. La prueba general ejecuta tres registros, búsqueda y resumen.
