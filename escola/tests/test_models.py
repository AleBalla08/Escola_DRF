from django.test import TestCase
from escola.models import *

class ModelEstudanteTestCase(TestCase):
    # def teste_falha(self):
    #     self.fail('Test Fail')
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'teste modelo',
            email = 'testemodelo@gmail.com',
            cpf = '23497612067',
            data_nascimento = '2000-03-12',
            celular = '54 99999-9999'
        )

    def test_verify_student_attrs(self):
        """teste que verifica os atributos do estudante"""
        self.assertEqual(self.estudante.nome, 'teste modelo'),
        self.assertEqual(self.estudante.email, 'testemodelo@gmail.com'),
        self.assertEqual(self.estudante.cpf, '23497612067'),
        self.assertEqual(self.estudante.data_nascimento, '2000-03-12'),
        self.assertEqual(self.estudante.celular, '54 99999-9999')

class ModelCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo = 'DRF01',
            descricao = 'Curso de django rest 01',
            nivel = 'I'
        )

    def test_verify_curso_attrs(self):
        self.assertEqual(self.curso.codigo  ,'DRF01'),
        self.assertEqual(self.curso.descricao  ,'Curso de django rest 01'),
        self.assertEqual(self.curso.nivel  ,'I'),



class ModelMatriculaTestCase(TestCase):
    
    def setUp(self):

        self.estudante = Estudante.objects.create(
            nome='teste modelo',
            email='teste2@gmail.com',
            cpf='12345678901',
            data_nascimento='2001-05-15',
            celular='55 99999-8888'
        )


        self.curso = Curso.objects.create(
            codigo='DRF01',
            descricao='Curso de django rest 01',
            nivel='I'
        )

        self.matricula = Matricula.objects.create(
            estudante = self.estudante,
            curso = self.curso,
            periodo = 'M'
        )

    def test_verify_matricula_attrs(self):
        self.assertEqual(self.matricula.estudante.nome, 'teste modelo'),
        self.assertEqual(self.matricula.curso.codigo, 'DRF01'),
        self.assertEqual(self.matricula.periodo, 'M')