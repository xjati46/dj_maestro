from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class BeritaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Berita
        fields = ('id', 'waktu_pos', 'judul', 'konten')

class ProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = ('id', 'nama_produk', 'harga', 'jumlah_pertemuan')

class PelatihSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelatih
        fields = ('id', 'user', 'nama_lengkap', 'nama_panggilan', 'jenis_kelamin', 'bagi_hasil')

class SiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Siswa
        fields = ('id', 'nama_lengkap', 'nama_panggilan', 'jenis_kelamin', 'usia')

class PesananSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesanan
        fields = ('id', 'pelatih', 'arsip', 'siswa', 'produk', 'diskon', 'tgl_transaksi', 'tgl_habis', 'p1', 'p1_c', 'p2', 'p2_c', 'p3', 'p3_c', 'p4', 'p4_c', 'p5', 'p5_c', 'p6', 'p6_c', 'p7', 'p7_c', 'p8', 'p8_c', 'status_habis', 'nilai_transaksi', 'p_total', 'p_c_total', 'margin_p_c', 'honor_per_sesi', 'honor_pencairan')