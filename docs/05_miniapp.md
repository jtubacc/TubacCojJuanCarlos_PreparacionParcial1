# Ejercicio 5 — Miniaplicación modular

`05_helpdesk_app/modelos.py` contiene las entidades, `servicios.py` las operaciones de la lista de tickets y `main.py` el menú. Un recorrido completo crea solicitante y técnico, registra un ticket, lo asigna, cambia su estado y lo lista.

## Comprobación reproducible

```sh
cd 05_helpdesk_app
python3 main.py
```

Para probar el flujo y los errores desde la raíz del repositorio:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_05_app.py' -v
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_serie_iii.py' -v
```

Las pruebas comprueban el flujo de creación, asignación y cambio de estado, así como solicitante ausente, ticket inexistente y finalización controlada de la entrada. Los datos residen únicamente en memoria.
