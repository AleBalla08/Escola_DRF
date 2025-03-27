from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Estudantes-list')

    def test_autenticacao_user_credenciais_corretas(self):
        usuario = authenticate(username = 'admin', password='admin')
        self.assertTrue((usuario is not None) and usuario.is_authenticated)

    def test_autenticacao_user_username_incorreto(self):
        usuario = authenticate(username = 'ale', password='admin')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)

    def test_autenticacao_user_senha_incorreta(self):
        usuario = authenticate(username = 'admin', password='ale')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)

    def test_requisicao_get_autorizada(self):
        self.client.force_authenticate(self.usuario)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_negada(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    