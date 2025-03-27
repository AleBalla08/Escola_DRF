from django.test import TestCase
from escola.models import *

class ModelEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'Model Test',
            email = 'modeltest@gmail.com',
            cpf = '98351575020',
            data_nascimento = '2023-02-02',
            celular = '86 99999-9999'
        )
    def test_verify_student_attrs(self):    
        self.assertEqual(self.estudante.nome, 'Model Test')
        self.assertEqual(self.estudante.email, 'modeltest@gmail.com')
        self.assertEqual(self.estudante.cpf, '98351575020')
        self.assertEqual(self.estudante.data_nascimento, '2023-02-02')
        self.assertEqual(self.estudante.celular, '86 99999-9999')


class ModelCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo = 'CDT02',
            descricao = 'Curso de teste numero 2',
            nivel = 'I'
        )
    def test_verify_course_attrs(self):
        self.assertEqual(self.curso.codigo, 'CDT02')
        self.assertEqual(self.curso.descricao, 'Curso de teste numero 2')
        self.assertEqual(self.curso.nivel, 'I')


class ModelMatriculaTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo = 'CDT02',
            descricao = 'Curso de teste numero 2',
            nivel = 'I'
        )
        
        self.estudante = Estudante.objects.create(
            nome = 'Model Test',
            email = 'modeltest@gmail.com',
            cpf = '98351575020',
            data_nascimento = '2023-02-02',
            celular = '86 99999-9999'
        )

        self.matricula = Matricula.objects.create(
            estudante=self.estudante,  
            curso=self.curso,  
            periodo='M'
        )

    def test_verify_registration_attrs(self):
        self.assertEqual(self.matricula.estudante.nome, 'Model Test')
        self.assertEqual(self.matricula.curso.codigo, 'CDT02')
        self.assertEqual(self.matricula.periodo, 'M')
