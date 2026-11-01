# Serie III: Programación II — HelpDesk EDU

Soluciones prácticas de consola y modelado en Python. Los ejemplos usan datos ficticios y almacenan información solo durante la ejecución.

## 1. Registro de ticket

`01_registro_ticket.py` solicita número, solicitante, título, descripción, categoría y prioridad; valida las entradas, guarda un diccionario con estado inicial y muestra un resumen.

```sh
python3 01_registro_ticket.py
```

## 2. Menú modular en memoria

`02_menu_helpdesk.py` registra, lista y busca tickets por solicitante, muestra un resumen por prioridad y permite salir. Usa una lista de diccionarios.

```sh
python3 02_menu_helpdesk.py
```

## 3. Usuarios y tickets con POO

`03_modelos.py` incluye clases con `__init__`, `__str__`, estado protegido y métodos para cambiar estado y asignar técnico. La ejecución crea dos usuarios y tres tickets y muestra un error de estado controlado.

```sh
python3 03_modelos.py
```

## 4. UML y relaciones

`04_modelo_helpdesk.puml` modela User, Ticket, Comment, History y Article; `04_modelos_base.py` contiene esqueletos consistentes y `04_justificacion_relaciones.md` explica multiplicidades y composición. El diagrama fue comprobado y renderizado con PlantUML local; aún falta una captura obtenida en VS Code si el formato de evidencia del examen la exige.

## 5. Miniaplicación modular

`05_helpdesk_app/` separa modelos, servicios y menú. Permite crear solicitante y técnico, registrar, asignar, cambiar estado, buscar y listar tickets.

```sh
cd 05_helpdesk_app
python3 main.py
```

## Pruebas

Desde la raíz del repositorio:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

La prueba ejecuta los casos normales y de error del registro, un menú con tres tickets, las reglas del modelo y un recorrido de consola de la miniaplicación. `01_registro_tickt.py` es un archivo previo conservado; el registro solicitado está en `01_registro_ticket.py`.

No se han añadido capturas del programa.
