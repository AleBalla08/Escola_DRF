from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

from escola.models import Curso
from escola.serializers import CursoSerializer

class CursoTestCase(APITestCase):
    fixtures = ['prototipo_banco.json']
    def setUp(self):
        self.usuario = User.objects.get(username='ale')
        self.url = reverse('Cursos-list')
        self.client.force_authenticate(user=self.usuario)
        self.curso_01 = Curso.objects.get(pk=1)
    
    def test_requisicao_get_cursos(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_um_curso(self):
        response = self.client.get(self.url + '1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_curso = Curso.objects.get(pk=1)
        dados_curso_serialized = CursoSerializer(instance=dados_curso).data
        print('dados curso: ', dados_curso_serialized)
        self.assertEqual(response.data, dados_curso_serialized)
    
    def test_requisicao_post_um_curso(self):
        dados = {
            'codigo':'CTT01',
            'descricao':'curso um',
            'nivel': 'A'
        }
        response = self.client.post(self.url, data=dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_requisicao_delete_um_curso(self):
        response = self.client.delete(f'{self.url}1/')#/cursos/2/
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_editar_um_curso(self):
        dados={
            'codigo':'PUT01',
            'descricao':'teste de Put',
            'nivel' : 'I'
        }
        response = self.client.put(self.url + '1/', data=dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

