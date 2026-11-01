# Ejercicio 4 — Relaciones UML

`04_modelo_helpdesk.puml` representa solicitante y técnico como asociaciones, comentarios e historial como composiciones y artículos mediante asociación con su autor. `04_justificacion_relaciones.md` explica multiplicidades y ciclos de vida. El PNG se generó con PlantUML; los rombos de composición se sitúan del lado de Ticket.

## Comprobación reproducible

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_04_relaciones.py' -v
```

Con PlantUML instalado, se puede verificar la sintaxis y volver a generar el diagrama:

```sh
plantuml -checkonly 04_modelo_helpdesk.puml
plantuml -tpng 04_modelo_helpdesk.puml
```

Las pruebas verifican extremos obligatorios y listas independientes. La composición es conceptual: el esqueleto en memoria no implementa borrado en cascada. La consigna pide verificar en VS Code; no se ha registrado una captura de ese paso.
