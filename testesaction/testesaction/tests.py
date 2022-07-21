from tokenize import Number
import unittest
from xmlrpc.client import boolean

#import TestCase


#biblioteca python para testes unitários
# TestCase ferramenta do django para testes automatizados

class ActionsTest (unittest.TestCase):

    def test_hello_world(self):
        x = 'dev web'
        self.assertEqual(x.split(), ['dev', 'web'])
        with self.assertRaises(TypeError):
            x.split(2)
        #deverá retornar verdadeiro pois faz a chegarem a função x.split se funciona quando o separador não é string

    def test_Upper(self):
        self.assertEqual('izabel'.upper(), 'IZABEL')
        #deverá retornar verdadeiro pois o .upper vai transformar o nome em questão em caixa alta, logo são iguais

    def test_islower(self):
        self.assertFalse('ISLOWER'.islower())
        #deverá retornar verdadeiro pois a afirmação é falsa

    def test_number(self):
        y = 3
        self.assertNotEquals(y, 'tres')
        #deverá retornar verdadeiro pois são tipo string e number

    def test_string(self):

        self.assertGreater(51000, 5000)
        #deverá retornar verdadeiro pois o primeiro é maior que o segundo
