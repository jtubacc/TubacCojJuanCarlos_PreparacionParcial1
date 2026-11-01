"""Regresiones del menú de tickets en memoria."""
import subprocess
import sys
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / '02_menu_helpdesk.py'


def ejecutar(datos):
    return subprocess.run([sys.executable, str(SCRIPT)], input=datos, text=True,
                          capture_output=True, timeout=5)


class MenuTests(unittest.TestCase):
    def test_opcion_invalida_y_lista_vacia(self):
        resultado = ejecutar('9\n2\n5\n')
        self.assertEqual(resultado.returncode, 0)
        self.assertIn('Opción inválida', resultado.stdout)
        self.assertIn('No hay tickets', resultado.stdout)

    def test_busqueda_sin_coincidencias(self):
        resultado = ejecutar('3\nNadie\n5\n')
        self.assertEqual(resultado.returncode, 0)
        self.assertIn('No hay tickets', resultado.stdout)

    def test_fin_durante_registro_se_controla(self):
        resultado = ejecutar('1\n1\n')
        self.assertEqual(resultado.returncode, 0)
        self.assertIn('Entrada finalizada', resultado.stdout)
        self.assertNotIn('Traceback', resultado.stderr)
