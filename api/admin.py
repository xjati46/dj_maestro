from django.contrib import admin
from .models import *


@admin.register(Berita)
class BeritaAdmin(admin.ModelAdmin):
    pass

@admin.register(Produk)
class ProdukAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'harga')

@admin.register(Pelatih)
class PelatihAdmin(admin.ModelAdmin):
    pass

@admin.register(Siswa)
class SiswaAdmin(admin.ModelAdmin):
    pass


@admin.register(Pesanan)
class PesananAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'produk', 'pelatih', 'arsip')
    list_filter = ('arsip', 'pelatih', 'produk')
    fieldsets = (
        ('Data Pesanan', {
            'fields': ('siswa', 'pelatih', 'produk', 'diskon', 'tgl_transaksi', 'tgl_habis')
        }),
        ('Data Latihan', {
            'fields': ('arsip', 'p1', 'p1_c', 'p2', 'p2_c', 'p3', 'p3_c', 'p4', 'p4_c', 'p5', 'p5_c', 'p6', 'p6_c', 'p7', 'p7_c', 'p8', 'p8_c')
        }),
    )