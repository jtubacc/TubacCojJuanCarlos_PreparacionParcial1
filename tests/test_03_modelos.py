"""Pruebas de las reglas de usuario y ticket."""
import importlib
import unittest

modelo = importlib.import_module('03_modelos')


class ModelosTests(unittest.TestCase):
    def setUp(self):
        self.solicitante = modelo.Usuario(1, 'Ana', 'ana@example.test', 'requester')
        self.ticket = modelo.Ticket(1, 'Red', 'Network', 'High', self.solicitante)

    def test_solo_tecnico_admitido_y_rol_normalizado(self):
        tecnico = modelo.Usuario(2, 'Luis', 'luis@example.test', ' Technician ')
        self.ticket.asignar_tecnico(tecnico)
        self.assertIs(self.ticket.tecnico, tecnico)
        for candidato in (self.solicitante, modelo.Usuario(3, 'X', 'x@example.test', None)):
            with self.subTest(candidato=candidato), self.assertRaises(ValueError):
                self.ticket.asignar_tecnico(candidato)
            self.assertIs(self.ticket.tecnico, tecnico)

    def test_estado_invalido_no_altera_estado_anterior(self):
        self.ticket.cambiar_estado('In Progress')
        with self.assertRaises(ValueError):
            self.ticket.cambiar_estado('Inexistente')
        self.assertEqual(self.ticket.status, 'In Progress')
