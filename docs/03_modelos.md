# Ejercicio 3 — Usuario y Ticket

`Usuario` reúne identificación, nombre, correo y rol. `Ticket` mantiene solicitante, técnico opcional y `_status`; `cambiar_estado` acepta únicamente los estados definidos y `asignar_tecnico` exige un usuario con rol técnico. Ambas clases ofrecen una representación mediante `__str__`.

## Comprobación reproducible

```sh
python3 03_modelos.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_03_modelos.py' -v
```

La demostración crea dos usuarios y tres tickets, asigna uno y cambia su estado. Las pruebas comprueban que un estado o técnico inválidos no sustituyen los valores anteriores y que el rol admite espacios y diferencias de mayúsculas.
