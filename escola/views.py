from escola.models import Estudante,Curso, Matricula
from escola.serializers import EstudanteSerializer,CursoSerializer, MatriculaSerializer, ListaMatriculasEstudanteSerializer, ListaMatriculasCursoSerializer, EstudanteSerializerV2
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from escola.throttles import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class EstudanteViewSet(viewsets.ModelViewSet):
    """
    Descrição da View:
    -Dados do Estudante;
    -Ordena por nome (alfabetica);
    -pode ser pesquisado por nome ou cpf;
    """
    queryset = Estudante.objects.all().order_by('id')
    #serializer_class = EstudanteSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome','cpf']
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return EstudanteSerializerV2
        return EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    """
    Descrição da View:
    -Dados do curso;
    -Ordena por ID;
    """
    queryset = Curso.objects.all().order_by('id')
    serializer_class = CursoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



class MatriculaViewSet(viewsets.ModelViewSet):
    """
    Descrição da View:
    -Dados da Matrícula;
    Metodos Permitidos:
    - get e post;
    Throttle Classes:
    -UserRateThrottle: limite de requisições para usuarios autenticados;
    -AnonRateThrottle: limite de requisições para usuários não autenticados;
    """
    throttle_classes = [UserRateThrottle, MatriculaAnonRateThrottle]
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    http_method_names = ["get", "post"]

class ListaMatriculaEstudante(generics.ListAPIView):
    """
    Descrição da View:
    -Lista as matrículas por estudante;
    Parâmetros:
    -pk: é o identificador de cada estudante. Deve ser um número inteiro;
    """

    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by('id')
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer

class ListaMatriculaCurso(generics.ListAPIView):
    """
    Descrição da View:
    -Lista as matrículas por curso;
    Parâmetros:
    -pk: é o identificador de cada curso. Deve ser um número inteiro;
    """
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasCursoSerializer