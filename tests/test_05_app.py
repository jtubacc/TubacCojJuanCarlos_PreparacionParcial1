"""Pruebas de errores y recuperación del menú de la miniaplicación."""
import subprocess
import sys
import unittest
from pathlib import Path

APP = Path(__file__).resolve().parents[1] / '05_helpdesk_app'


def ejecutar(datos):
    return subprocess.run([sys.executable, 'main.py'], cwd=APP, input=datos,
                          text=True, capture_output=True, timeout=5)


class AppTests(unittest.TestCase):
    def test_ticket_desconocido_no_interrumpe_menu(self):
        resultado = ejecutar('3\n999\n2\n5\n7\n')
        self.assertEqual(resultado.returncode, 0)
        self.assertIn('Ticket no encontrado', resultado.stdout)
        self.assertIn('No hay tickets', resultado.stdout)

    def test_solicitante_ausente_se_rechaza(self):
        resultado = ejecutar('2\n10\nSin red\n999\n5\n7\n')
        self.assertEqual(resultado.returncode, 0)
        self.assertIn('Solicitante no encontrado', resultado.stdout)
        self.assertIn('No hay tickets', resultado.stdout)

    def test_fin_de_entrada_se_controla(self):
        resultado = ejecutar('1\n')
        self.assertEqual(resultado.returncode, 0)
        self.assertIn('Entrada finalizada', resultado.stdout)
        self.assertNotIn('Traceback', resultado.stderr)
