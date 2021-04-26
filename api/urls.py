from django.urls import path, include
from rest_framework import routers
from .models import *
from .views import *


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('berita', BeritaViewSet)
router.register('produk', ProdukViewSet)
router.register('pelatih', PelatihViewSet)
router.register('siswa', SiswaViewSet)
router.register('pesanan', PesananViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
