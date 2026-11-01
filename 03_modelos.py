"""Clases de usuarios y tickets para el ejercicio de POO."""

ESTADOS = ('Open', 'In Progress', 'Resolved', 'Closed', 'Cancelled')


class Usuario:
    def __init__(self, id, nombre, email, rol):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.rol = rol

    def __str__(self):
        return f'{self.id}: {self.nombre} ({self.rol})'


class Ticket:
    def __init__(self, id, titulo, categoria, prioridad, solicitante, tecnico=None, estado='Open'):
        self.id = id
        self.titulo = titulo
        self.categoria = categoria
        self.prioridad = prioridad
        self.solicitante = solicitante
        self.tecnico = None
        self._status = 'Open'
        self.cambiar_estado(estado)
        if tecnico is not None:
            self.asignar_tecnico(tecnico)

    @property
    def status(self):
        return self._status

    def cambiar_estado(self, estado):
        if estado not in ESTADOS:
            raise ValueError('Estado no permitido')
        self._status = estado

    def asignar_tecnico(self, tecnico):
        if not isinstance(tecnico, Usuario) or tecnico.rol.casefold() != 'technician':
            raise ValueError('El usuario debe tener rol technician')
        self.tecnico = tecnico

    def __str__(self):
        tecnico = self.tecnico.nombre if self.tecnico else 'Sin asignar'
        return f'{self.id}: {self.titulo} | {self.solicitante.nombre} | {tecnico} | {self.status}'


def demostracion():
    solicitante = Usuario(1, 'Ana', 'ana@example.test', 'requester')
    tecnico = Usuario(2, 'Luis', 'luis@example.test', 'technician')
    tickets = [Ticket(1, 'Sin red', 'Network', 'High', solicitante),
               Ticket(2, 'Teclado', 'Hardware', 'Low', solicitante),
               Ticket(3, 'Programa', 'Software', 'Medium', solicitante)]
    tickets[0].asignar_tecnico(tecnico)
    tickets[0].cambiar_estado('In Progress')
    for ticket in tickets:
        print(ticket)
    try:
        tickets[0].cambiar_estado('Estado inválido')
    except ValueError as exc:
        print(f'Error controlado: {exc}')


if __name__ == '__main__':
    demostracion()
