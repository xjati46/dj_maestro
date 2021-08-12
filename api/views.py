from django.shortcuts import render
from rest_framework import views, viewsets, generics, response
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class BeritaViewSet(viewsets.ModelViewSet):
    queryset = Berita.objects.all()
    serializer_class = BeritaSerializer
    authentication_classes = (TokenAuthentication,)

class ProdukViewSet(viewsets.ModelViewSet):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer
    authentication_classes = (TokenAuthentication,)

class PelatihViewSet(viewsets.ModelViewSet):
    queryset = Pelatih.objects.all()
    serializer_class = PelatihSerializer
    authentication_classes = (TokenAuthentication,)

class SiswaViewSet(viewsets.ModelViewSet):
    queryset = Siswa.objects.all()
    serializer_class = SiswaSerializer
    authentication_classes = (TokenAuthentication,)

class PesananViewSet(viewsets.ModelViewSet):
    queryset = Pesanan.objects.all()
    serializer_class = PesananSerializer
    authentication_classes = (TokenAuthentication,)
