"""Pruebas de multiplicidad básica y aislamiento del modelo UML."""
import importlib
import unittest

modelo = importlib.import_module('04_modelos_base')


class RelacionesTests(unittest.TestCase):
    def test_listas_de_componentes_independientes(self):
        usuario = modelo.User(1, 'Ana', 'ana@example.test', 'requester')
        primero = modelo.Ticket(1, 'Red', usuario)
        segundo = modelo.Ticket(2, 'Impresora', usuario)
        primero.add_comment('Revisar')
        primero.record_event('Registrado')
        self.assertEqual(len(primero.comments), 1)
        self.assertEqual(len(primero.history), 1)
        self.assertEqual(segundo.comments, [])
        self.assertEqual(segundo.history, [])

    def test_extremos_de_asociacion_obligatorios(self):
        usuario = modelo.User(1, 'Ana', 'ana@example.test', 'requester')
        with self.assertRaises(ValueError):
            modelo.Ticket(1, 'Red', None)
        with self.assertRaises(ValueError):
            modelo.Ticket(1, 'Red', usuario, technician='no es User')
        with self.assertRaises(ValueError):
            modelo.Article(1, 'Ayuda', None)
        self.assertIsNone(modelo.Ticket(2, 'Impresora', usuario).technician)
