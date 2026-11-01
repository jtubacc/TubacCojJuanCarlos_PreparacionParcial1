"""Regresiones del registro de un ticket por consola."""
import subprocess
import sys
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / '01_registro_ticket.py'


def ejecutar(datos):
    return subprocess.run([sys.executable, str(SCRIPT)], input=datos, text=True,
                          capture_output=True, timeout=5)


class RegistroTests(unittest.TestCase):
    def test_normaliza_catalogos_y_muestra_estado(self):
        resultado = ejecutar('17\nAna\nRed\nSin conexión\nnetwork\nhigh\n')
        self.assertEqual(resultado.returncode, 0)
        self.assertIn('Network | High | Open', resultado.stdout)

    def test_rechaza_prioridad_fuera_de_catalogo(self):
        resultado = ejecutar('17\nAna\nRed\nSin conexión\nNetwork\nUrgente\n')
        self.assertEqual(resultado.returncode, 0)
        self.assertIn('Prioridad no es válido', resultado.stdout)
        self.assertNotIn('Traceback', resultado.stderr)

    def test_fin_de_entrada_no_produce_traceback(self):
        resultado = ejecutar('17\nAna\n')
        self.assertEqual(resultado.returncode, 0)
        self.assertIn('Entrada finalizada', resultado.stdout)
        self.assertNotIn('Traceback', resultado.stderr)
