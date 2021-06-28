from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Berita(models.Model):
    waktu_pos = models.DateTimeField(auto_now_add=True)
    judul = models.CharField(max_length=100)
    konten = models.TextField(max_length=2000)

    def __str__(self):
        return self.judul

    class Meta:
        ordering = ['-waktu_pos']
        verbose_name_plural = "Berita"


class Produk(models.Model):
    nama_produk = models.CharField(max_length=100)
    harga = models.IntegerField()
    jumlah_pertemuan = models.IntegerField()

    def __str__(self):
        return self.nama_produk

    class Meta:
        ordering = ['nama_produk']
        verbose_name_plural = "Produk"


# PELATIH ##################################################################


class Pelatih(models.Model):
    PILIHAN_JENIS_KELAMIN = models.TextChoices(
        'Jenis Kelamin',
        'Laki-laki Perempuan',)

    user = models.OneToOneField(
            User,
            on_delete=models.SET_NULL,
            null=True,
            blank=True,)
    nama_lengkap = models.CharField(max_length=100,)
    nama_panggilan = models.CharField(max_length=50,)
    jenis_kelamin = models.CharField(
        max_length=10,
        choices=PILIHAN_JENIS_KELAMIN.choices,)
    bagi_hasil = models.FloatField(default=0.6)
   
    class Meta:
        ordering = ['nama_lengkap']
        verbose_name_plural = "Pelatih"

    def __str__(self):
        return f'Coach {self.nama_panggilan}'


# SISWA ##################################################################


class Siswa(models.Model):
    PILIHAN_JENIS_KELAMIN = models.TextChoices(
        'Jenis Kelamin',
        'Laki-laki Perempuan',
    )

    nama_lengkap = models.CharField(max_length=100,)
    nama_panggilan = models.CharField(max_length=50,)
    jenis_kelamin = models.CharField(
        max_length=10,
        choices=PILIHAN_JENIS_KELAMIN.choices,
    )
    usia = models.IntegerField()
   
    class Meta:
        ordering = ['nama_lengkap']
        verbose_name_plural = "Siswa"

    def __str__(self):
        return f'{self.nama_lengkap} ({self.nama_panggilan})'


# PESANAN ##################################################################


class Pesanan(models.Model):
    siswa = models.ForeignKey(Siswa, on_delete=models.SET_NULL, null=True, blank=True)
    pelatih = models.ForeignKey(Pelatih, on_delete=models.SET_NULL, null=True, blank=True)
    produk = models.ForeignKey(Produk, on_delete=models.SET_NULL, null=True, blank=True)
    diskon = models.FloatField(null=True, blank=True)

    tgl_transaksi = models.DateField()
    tgl_habis = models.DateField()

    arsip = models.BooleanField(default=False)

    p1 = models.DateField('Pertemuan 1', null=True, blank=True)
    p2 = models.DateField('Pertemuan 2', null=True, blank=True)
    p3 = models.DateField('Pertemuan 3', null=True, blank=True)
    p4 = models.DateField('Pertemuan 4', null=True, blank=True)
    p5 = models.DateField('Pertemuan 5', null=True, blank=True)
    p6 = models.DateField('Pertemuan 6', null=True, blank=True)
    p7 = models.DateField('Pertemuan 7', null=True, blank=True)
    p8 = models.DateField('Pertemuan 8', null=True, blank=True)

    p1_c = models.BooleanField(default=False)
    p2_c = models.BooleanField(default=False)
    p3_c = models.BooleanField(default=False)
    p4_c = models.BooleanField(default=False)
    p5_c = models.BooleanField(default=False)
    p6_c = models.BooleanField(default=False)
    p7_c = models.BooleanField(default=False)
    p8_c = models.BooleanField(default=False)


    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Pesanan"

    def __str__(self):
        try:
            return f'{self.id}/{self.siswa.nama_panggilan}'
        except:
            return f'{self.id}/deleted_account'

    def status_habis(self):
        return self.tgl_habis < timezone.now().date()

    def nilai_transaksi(self):
        x = 0
        if self.diskon:
            x = (1 - self.diskon) * self.produk.harga
            return int(x)
        return self.produk.harga

    def p_total(self):
        count = 0
        if self.p1:
            count += 1
        if self.p2:
            count += 1
        if self.p3:
            count += 1
        if self.p4:
            count += 1
        if self.p5:
            count += 1
        if self.p6:
            count += 1
        if self.p7:
            count += 1
        if self.p8:
            count += 1
        return count

    def p_c_total(self):
        count = 0
        if self.p1_c:
            count += 1
        if self.p2_c:
            count += 1
        if self.p3_c:
            count += 1
        if self.p4_c:
            count += 1
        if self.p5_c:
            count += 1
        if self.p6_c:
            count += 1
        if self.p7_c:
            count += 1
        if self.p8_c:
            count += 1
        return count

    def margin_p_c(self):
        return self.p_total() - self.p_c_total()

    def honor_per_sesi(self):
        try:
            x = self.nilai_transaksi() * self.pelatih.bagi_hasil
            y = x / self.produk.jumlah_pertemuan
            return int(y)
        except:
            return 0

    def honor_pencairan(self):
        return int(self.honor_per_sesi() * self.margin_p_c())