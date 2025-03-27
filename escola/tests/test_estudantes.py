from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

from escola.models import Estudante
from escola.serializers import EstudanteSerializer

class EstudanteTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.usuario)
        self.cliente_01 = Estudante.objects.create(
            nome = 'Estudante Um',
            email = 'estudante01@gmail.com',
            cpf = '29207126087',
            data_nascimento = '2024-01-02',
            celular = '54 99123-6789'
        )
        self.cliente_02 = Estudante.objects.create(
            nome = 'Estudante Dois',
            email = 'estudante02@gmail.com',
            cpf = '51703986032',
            data_nascimento = '2024-01-02',
            celular = '54 99123-6759'
        )

    def test_requisicao_get_estudantes(self):
        response = self.client.get(self.url)#/estudantes/
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_um_estudante(self):
        response = self.client.get(self.url + '1/')#/estudantes/1/
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_estudante = Estudante.objects.get(pk=1)
        dados_estudante_serialized = EstudanteSerializer(instance=dados_estudante).data
        self.assertEqual(response.data, dados_estudante_serialized)
    
    def test_requisicao_criar_um_estudante(self):
        dados={
            'nome':'teste',
            'email':'teste@gmail.com',
            'cpf':'96472629064',
            'data_nascimento':'1990-02-03',
            'celular':'54 22346-1224'
        }
        response = self.client.post(self.url, data=dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_um_estudante(self):
        response = self.client.delete(f'{self.url}2/')#/estudante/2/
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)