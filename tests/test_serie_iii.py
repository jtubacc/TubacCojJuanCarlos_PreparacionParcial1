import importlib
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def ejecutar(script, entrada, cwd=ROOT):
    return subprocess.run([sys.executable, str(script)], input=entrada, text=True,
                          capture_output=True, cwd=cwd, timeout=10)


class SerieIII(unittest.TestCase):
    def test_registro_ticket_valido_y_errores(self):
        script = ROOT / '01_registro_ticket.py'
        valido = ejecutar(script, '1\nAna\nSin red\nNo conecta\nNetwork\nHigh\n')
        self.assertEqual(valido.returncode, 0)
        self.assertIn('Ticket 1 | Ana | Sin red | No conecta | Network | High | Open', valido.stdout)
        for datos in ('abc\n', '1\n\n', '1\nAna\nSin red\nNo conecta\nOtra\n'):
            with self.subTest(datos=datos):
                resultado = ejecutar(script, datos)
                self.assertEqual(resultado.returncode, 0)
                self.assertIn('Error:', resultado.stdout)
                self.assertNotIn('Traceback', resultado.stderr)

    def test_menu_tres_tickets_busqueda_y_resumen(self):
        datos = ('1\n1\nAna\nRed\nSin red\nNetwork\nHigh\n'
                 '1\n2\nLuis\nTeclado\nNo sirve\nHardware\nLow\n'
                 '1\n3\nAna\nPrograma\nNo abre\nSoftware\nHigh\n'
                 '3\nana\n4\n5\n')
        resultado = ejecutar(ROOT / '02_menu_helpdesk.py', datos)
        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        self.assertEqual(resultado.stdout.count('Ticket registrado.'), 3)
        self.assertIn('Ticket 1 | Ana', resultado.stdout)
        self.assertIn('Ticket 3 | Ana', resultado.stdout)
        self.assertIn('High: 2', resultado.stdout)
        self.assertIn('Low: 1', resultado.stdout)

    def test_modelos_asignacion_y_estado_invalido(self):
        modulo = importlib.import_module('03_modelos')
        solicitante = modulo.Usuario(1, 'Ana', 'ana@example.test', 'requester')
        tecnico = modulo.Usuario(2, 'Luis', 'luis@example.test', 'technician')
        ticket = modulo.Ticket(1, 'Red', 'Network', 'High', solicitante)
        ticket.asignar_tecnico(tecnico)
        ticket.cambiar_estado('In Progress')
        self.assertIs(ticket.tecnico, tecnico)
        with self.assertRaises(ValueError):
            ticket.cambiar_estado('No permitido')
        self.assertEqual(ticket.status, 'In Progress')
        with self.assertRaises(ValueError):
            ticket.asignar_tecnico(solicitante)

    def test_miniaplicacion_consola_completa(self):
        carpeta = ROOT / '05_helpdesk_app'
        datos = ('1\n1\nAna\nana@example.test\nrequester\n'
                 '1\n2\nLuis\nluis@example.test\ntechnician\n'
                 '2\n10\nSin red\n1\n3\n10\n2\n'
                 '4\n10\nIn Progress\n5\n6\n10\n7\n')
        resultado = ejecutar(carpeta / 'main.py', datos, cwd=carpeta)
        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        self.assertIn('10: Sin red | Ana | Luis | In Progress', resultado.stdout)
        self.assertNotIn('Traceback', resultado.stderr)


if __name__ == '__main__':
    unittest.main()
