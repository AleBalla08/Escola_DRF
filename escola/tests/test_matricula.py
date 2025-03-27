from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

from escola.models import Curso, Estudante, Matricula
from escola.serializers import MatriculaSerializer

class MatriculaTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.estudante = Estudante.objects.create(
            nome = 'Estudante Um',
            email = 'estudante01@gmail.com',
            cpf = '29207126087',
            data_nascimento = '2024-01-02',
            celular = '54 99123-6789'
        )
        
        self.curso = Curso.objects.create(
            codigo = 'CDT03',
            descricao = 'Curso de teste número 3',
            nivel = 'I'
        )

        self.matricula = Matricula.objects.create(
            estudante = self.estudante,
            curso = self.curso,
            periodo = 'V'

        )

        self.url = reverse('Matriculas-list')
        self.client.force_authenticate(user=self.usuario)
    
    def test_requisicao_get_matriculas(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_um_Matricula(self):
        response = self.client.get(self.url + '1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_matricula = Matricula.objects.get(pk=1)
        dados_matricula_serialized = MatriculaSerializer(instance=dados_matricula).data
        self.assertEqual(response.data, dados_matricula_serialized)
    
    def test_requisicao_post_um_Matricula(self):
        dados = {
            'estudante':self.estudante.pk,
            'curso':self.curso.pk,
            'periodo': 'M'
        }
        response = self.client.post(self.url, data=dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_um_matricula(self):
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)