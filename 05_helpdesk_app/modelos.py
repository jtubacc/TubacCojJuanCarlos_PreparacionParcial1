"""Entidades usadas por la miniaplicación."""

ESTADOS = ('Open', 'In Progress', 'Resolved', 'Closed', 'Cancelled')


class Usuario:
    def __init__(self, id, nombre, email, rol):
        self.id, self.nombre, self.email, self.rol = id, nombre, email, rol

    def __str__(self):
        return f'{self.id}: {self.nombre} ({self.rol})'


class Ticket:
    def __init__(self, id, titulo, solicitante):
        self.id, self.titulo, self.solicitante = id, titulo, solicitante
        self.tecnico = None
        self.estado = 'Open'

    def __str__(self):
        nombre_tecnico = self.tecnico.nombre if self.tecnico else 'Sin asignar'
        return f'{self.id}: {self.titulo} | {self.solicitante.nombre} | {nombre_tecnico} | {self.estado}'
