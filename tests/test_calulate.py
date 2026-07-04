import unittest
from src.calculator import  sumar, restar, multiplicar, dividir

class TestCalculator(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(5, 3), 8)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)

    def test_restar(self):
        self.assertEqual(restar(5, 3), 2)
        self.assertEqual(restar(-1, 1), -2)
        self.assertEqual(restar(-1, -1), 0)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(5, 3), 15)
        self.assertEqual(multiplicar(-1, 1), -1)
        self.assertEqual(multiplicar(-1, -1), 1)

    def test_dividir(self):
        self.assertEqual(dividir(6, 3), 2.0)
        self.assertEqual(dividir(-6, 3), -2.0)
        self.assertEqual(dividir(-6, -3), 2.0)
        with self.assertRaises(ValueError):
            dividir(6, 0)

