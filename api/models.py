from django.db import models

from django.urls import reverse
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Berita(models.Model):
    waktu_pos = models.DateTimeField(auto_now_add=True)
    judul = models.CharField(max_length=100)
    konten = models.TextField(max_length=2000)

    def __str__(self):
        return self.judul

    class Meta:
        ordering = ['-waktu_pos']


class Produk(models.Model):
    nama_produk = models.CharField(max_length=100)
    harga = models.IntegerField()

    def __str__(self):
        return self.nama_produk

    class Meta:
        ordering = ['nama_produk']


# COACH ##################################################################

class Pelatih(models.Model):
    PILIHAN_JENIS_KELAMIN = models.TextChoices(
        'Jenis Kelamin',
        'Laki-laki Perempuan',
    )

    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    nama_lengkap = models.CharField(max_length=50,)
    nama_panggilan = models.CharField(max_length=10,)
    jenis_kelamin = models.CharField(
        max_length=10,
        choices=PILIHAN_JENIS_KELAMIN.choices,
    )
    tempat_lahir = models.CharField(
        max_length=10,
        )
    tanggal_lahir = models.DateField(
        help_text='format "tahun-bulan-tanggal" (Contoh "2000-01-31")',
    )

    nomor_ktp = models.CharField(
        max_length=20,
        blank=True,
        )
    alamat_tinggal = models.CharField(
        max_length=100,
        blank=True,
        )
    alamat_kotakab = models.CharField(
        'Alamat Kota/ Kab.', 
        max_length=20,
        blank=True,
        )
    nomor_ponsel = models.CharField(
        max_length=20,
        blank=True,
        )
    nama_bank = models.CharField(
        max_length=20,
        help_text='Diutamakan Bank Mandiri',
        blank=True,
    )
    nomor_rekening = models.CharField(
        max_length=30, 
        blank=True,
        )
    deskripsi = models.TextField(
        max_length=100,
        help_text='latar belakang, pendidikan, keahlian',
        blank=True,
    )

    class Meta:
        ordering = ['nama_panggilan']

    def __str__(self):
        return f'Coach {self.nama_panggilan}'

    def usia(self):
        return int((timezone.now().date() - self.tanggal_lahir).days / 365.25)

# STUDENT ##################################################################

class Student(models.Model):
    PILIHAN_JENIS_KELAMIN = models.TextChoices(
        'Jenis Kelamin',
        'Laki-laki Perempuan',
    )

    nama_lengkap = models.CharField(max_length=50,)
    nama_panggilan = models.CharField(max_length=10,)
    jenis_kelamin = models.CharField(
        max_length=10,
        choices=PILIHAN_JENIS_KELAMIN.choices,
    )
    tempat_lahir = models.CharField(max_length=10,)
    tanggal_lahir = models.DateField(
        help_text='format "tahun-bulan-tanggal" (Contoh "2000-01-31")',
    )

    alamat_tinggal = models.CharField(max_length=100, blank=True,)
    alamat_kotakab = models.CharField('Alamat Kota/ Kab.', max_length=20, blank=True,)
    nomor_ponsel = models.CharField(max_length=20, blank=True,)
    deskripsi = models.TextField(
        max_length=100,
        help_text='harapan latihan, penyakit, kebiasaan, dll',
        blank=True,
    )

    # KHUSUS STUDENT

    PILIHAN_AFILIASI = models.TextChoices(
        'Afiliasi',
        'Dnurs',
    )

    afiliasi = models.CharField(
        max_length=10,
        choices=PILIHAN_AFILIASI.choices,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['-nama_lengkap']

    def get_absolute_url(self):
        return reverse('student-app:student-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.nama_lengkap} ({self.nama_panggilan})'

    def usia(self):
        return int((timezone.now().date() - self.tanggal_lahir).days / 365.25)


class Pesanan(models.Model):
    # siswa = models.ForeignKey(Student,on_delete=models.SET_NULL,null=True)
    # pelatih = models.ForeignKey(Coach, on_delete=models.SET_NULL, null=True)
    produk = models.ForeignKey(Produk, on_delete=models.SET_NULL, null=True)
    diskon = models.FloatField(blank=True, null=True)

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
        ordering = ['student']

    def __str__(self):
        try:
            return f'{self.id}/{self.student.nama_panggilan}'
        except:
            return f'{self.id}/deleted_account'

    def is_expired(self):
        if self.tanggal_expired < timezone.now().date():
            return "✘EXPIRED"
        else:
            return ""

    def bill(self):
        x = 0
        if self.diskon:
            x = (1 - self.diskon) * self.product.harga
            return int(x)
        return int(self.product.harga)

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
        x = int(self.p_total())
        y = int(self.p_c_total())
        if x != y:
            return x-y
        else:
            return ''

    def income_coach_normal(self):
        return int(self.p_c_total() * self.product.fee_pelatih)

    def potential_income_coach_normal(self):
        return int(
            (self.product.jumlah_pertemuan - self.p_c_total())
            * self.product.fee_pelatih
            )

    def p_status(self):
        if self.p_total() >= self.product.jumlah_pertemuan:
            return "✘SELESAI"
        else:
            return ""

    def income_coach_actual_normal(self):
        return self.margin_p_c() * self.product.fee_pelatih

