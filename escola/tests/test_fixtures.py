from django.test import TestCase
from escola.models import *

class FixturesTestCase(TestCase):
    fixtures = ['prototipo_banco.json']

    def teste_carregamento_fixtures(self):
        estudante = Estudante.objects.get(cpf='19302671690')
        curso = Curso.objects.get(pk=1)
        self.assertEqual(estudante.celular, '50 94492-6156')
        self.assertEqual(curso.codigo, 'CPOO1')