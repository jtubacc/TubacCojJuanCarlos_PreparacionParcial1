"""Menú para el flujo mínimo de la miniaplicación."""
from modelos import Usuario
from servicios import asignar_tecnico, buscar_ticket, cambiar_estado, listar_tickets, registrar_ticket


def ejecutar_menu():
    usuarios = {}
    tickets = []
    while True:
        opcion = input('1 Crear usuario | 2 Registrar ticket | 3 Asignar | 4 Cambiar estado | 5 Listar | 6 Buscar | 7 Salir: ').strip()
        try:
            if opcion == '1':
                id = int(input('ID usuario: '))
                nombre = input('Nombre: ').strip()
                email = input('Email: ').strip()
                rol = input('Rol (requester/technician): ').strip().lower()
                if id in usuarios or not nombre or not email or rol not in ('requester', 'technician'):
                    raise ValueError('Datos inválidos o ID duplicado')
                usuarios[id] = Usuario(id, nombre, email, rol)
                print('Usuario registrado.')
            elif opcion == '2':
                id = int(input('ID ticket: '))
                titulo = input('Título: ')
                usuario = usuarios.get(int(input('ID solicitante: ')))
                if usuario is None or usuario.rol != 'requester':
                    raise ValueError('Solicitante no encontrado')
                print(registrar_ticket(tickets, id, titulo, usuario))
            elif opcion == '3':
                id = int(input('ID ticket: '))
                tecnico = usuarios.get(int(input('ID técnico: ')))
                print(asignar_tecnico(tickets, id, tecnico))
            elif opcion == '4':
                id = int(input('ID ticket: '))
                estado = input('Estado (Open/In Progress/Resolved/Closed/Cancelled): ').strip()
                print(cambiar_estado(tickets, id, estado))
            elif opcion == '5':
                encontrados = listar_tickets(tickets)
                for ticket in encontrados:
                    print(ticket)
                if not encontrados:
                    print('No hay tickets.')
            elif opcion == '6':
                ticket = buscar_ticket(tickets, int(input('ID ticket: ')))
                print(ticket if ticket else 'Ticket no encontrado')
            elif opcion == '7':
                break
            else:
                print('Opción inválida.')
        except ValueError as exc:
            print(f'Error: {exc}')


if __name__ == '__main__':
    try:
        ejecutar_menu()
    except EOFError:
        print('Entrada finalizada.')
