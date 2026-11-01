# Ejercicio 1 — Registro de un ticket

El programa recibe número, solicitante, título, descripción, categoría y prioridad. Convierte el número a entero, rechaza campos vacíos y opciones ajenas a los catálogos, y crea un diccionario con `status = Open`.

## Comprobación reproducible

Desde la raíz:

```sh
printf '17\nAna\nRed\nSin conexión\nNetwork\nHigh\n' | python3 01_registro_ticket.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_01_registro.py' -v
```

El primer comando muestra el resumen del ticket. La prueba automatizada verifica categorías sin distinguir mayúsculas, prioridad inválida y fin de entrada controlado. La prueba general `test_serie_iii.py` incluye número inválido, campo vacío y registro válido.
