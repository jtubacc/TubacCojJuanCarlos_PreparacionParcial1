"""Registro de un ticket por consola, con validación de entradas."""

CATEGORIAS = ('General', 'Hardware', 'Software', 'Network')
PRIORIDADES = ('Low', 'Medium', 'High', 'Critical')


def pedir_texto(nombre, entrada=input):
    texto = entrada(f'{nombre}: ').strip()
    if not texto:
        raise ValueError(f'{nombre} no puede estar vacío')
    return texto


def pedir_catalogo(nombre, opciones, entrada=input):
    valor = pedir_texto(nombre, entrada)
    for opcion in opciones:
        if opcion.casefold() == valor.casefold():
            return opcion
    raise ValueError(f'{nombre} no es válido')


def registrar_ticket(entrada=input):
    try:
        numero = int(pedir_texto('Número de ticket', entrada))
    except ValueError as exc:
        raise ValueError('Número de ticket inválido') from exc
    solicitante = pedir_texto('Solicitante', entrada)
    titulo = pedir_texto('Título', entrada)
    descripcion = pedir_texto('Descripción', entrada)
    categoria = pedir_catalogo('Categoría', CATEGORIAS, entrada)
    prioridad = pedir_catalogo('Prioridad', PRIORIDADES, entrada)
    return {'numero': numero, 'solicitante': solicitante, 'titulo': titulo,
            'descripcion': descripcion, 'categoria': categoria, 'prioridad': prioridad,
            'status': 'Open'}


def resumen(ticket):
    return (f"Ticket {ticket['numero']} | {ticket['solicitante']} | {ticket['titulo']} | "
            f"{ticket['descripcion']} | {ticket['categoria']} | {ticket['prioridad']} | {ticket['status']}")


def main():
    try:
        print(resumen(registrar_ticket()))
    except ValueError as exc:
        print(f'Error: {exc}')
    except EOFError:
        print('Entrada finalizada sin completar el registro.')


if __name__ == '__main__':
    main()
