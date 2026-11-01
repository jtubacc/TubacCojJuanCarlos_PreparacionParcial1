"""Menú modular de tickets en memoria."""
from importlib import import_module

registro = import_module('01_registro_ticket')


def pedir_opcion():
    return input('1 Registrar | 2 Listar | 3 Buscar solicitante | 4 Resumen | 5 Salir: ').strip()


def registrar_ticket(tickets):
    try:
        ticket = registro.registrar_ticket()
    except ValueError as exc:
        print(f'Error: {exc}')
        return None
    tickets.append(ticket)
    print('Ticket registrado.')
    return ticket


def listar_tickets(tickets):
    if not tickets:
        print('No hay tickets.')
    for ticket in tickets:
        print(registro.resumen(ticket))


def buscar_por_solicitante(tickets, solicitante):
    consulta = solicitante.strip().casefold()
    return [ticket for ticket in tickets if ticket['solicitante'].casefold() == consulta]


def mostrar_resumen(tickets):
    print(f'Total: {len(tickets)}')
    for prioridad in registro.PRIORIDADES:
        print(f"{prioridad}: {sum(1 for ticket in tickets if ticket['prioridad'] == prioridad)}")


def ejecutar_menu():
    tickets = []
    while True:
        opcion = pedir_opcion()
        if opcion == '1':
            registrar_ticket(tickets)
        elif opcion == '2':
            listar_tickets(tickets)
        elif opcion == '3':
            listar_tickets(buscar_por_solicitante(tickets, input('Solicitante: ')))
        elif opcion == '4':
            mostrar_resumen(tickets)
        elif opcion == '5':
            break
        else:
            print('Opción inválida.')


if __name__ == '__main__':
    ejecutar_menu()
