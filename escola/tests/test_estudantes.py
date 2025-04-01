from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

from escola.models import Estudante
from escola.serializers import EstudanteSerializer

class EstudanteTestCase(APITestCase):
    fixtures = ['prototipo_banco.json']
    def setUp(self):
        self.usuario = User.objects.get(username='ale')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.usuario)
        self.cliente_01 = Estudante.objects.get(pk=1)
        self.cliente_02 = Estudante.objects.get(pk=2)

    def test_requisicao_get_estudantes(self):
        response = self.client.get(self.url)#/estudantes/
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_um_estudante(self):
        response = self.client.get(self.url + '1/')#/estudantes/1/
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_estudante = Estudante.objects.get(pk=1)
        dados_estudante_serialized = EstudanteSerializer(instance=dados_estudante).data
        print('dados estudante: ',dados_estudante_serialized)
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

    def test_requisicao_put_editar_um_estudante(self):
        dados={
            'nome':'testePut',
            'email':'testePut@gmail.com',
            'cpf':'80239700031',
            'data_nascimento':'1990-03-03',
            'celular':'54 22345-1224'
        }
        response = self.client.put(self.url + '1/', data=dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)