# Miniaplicación HelpDesk

Los modelos `Usuario` y `Ticket` están en `modelos.py`; las operaciones sobre la lista en memoria están en `servicios.py` y el menú en `main.py`. Al cerrar el programa se pierden los datos.

Desde esta carpeta:

```sh
python3 main.py
```

Para reproducir el flujo: cree un usuario `requester` y otro `technician`; registre un ticket con el identificador del solicitante, asígnelo al técnico, cambie su estado a `In Progress` y use la opción de listar.
