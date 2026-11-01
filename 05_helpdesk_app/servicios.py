"""Operaciones sobre la colección de tickets en memoria."""
from modelos import ESTADOS, Ticket, Usuario


def registrar_ticket(tickets, id, titulo, solicitante):
    if any(ticket.id == id for ticket in tickets):
        raise ValueError('El ticket ya existe')
    if not titulo.strip() or not isinstance(solicitante, Usuario):
        raise ValueError('Título y solicitante son obligatorios')
    ticket = Ticket(id, titulo.strip(), solicitante)
    tickets.append(ticket)
    return ticket


def listar_tickets(tickets):
    return list(tickets)


def buscar_ticket(tickets, id):
    return next((ticket for ticket in tickets if ticket.id == id), None)


def asignar_tecnico(tickets, id, tecnico):
    ticket = buscar_ticket(tickets, id)
    if ticket is None:
        raise ValueError('Ticket no encontrado')
    if not isinstance(tecnico, Usuario) or tecnico.rol.casefold() != 'technician':
        raise ValueError('El usuario debe tener rol technician')
    ticket.tecnico = tecnico
    return ticket


def cambiar_estado(tickets, id, estado):
    ticket = buscar_ticket(tickets, id)
    if ticket is None:
        raise ValueError('Ticket no encontrado')
    if estado not in ESTADOS:
        raise ValueError('Estado no permitido')
    ticket.estado = estado
    return ticket
