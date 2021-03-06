# Generated by Django 3.1.6 on 2021-09-17 05:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='berita',
            options={'ordering': ['-waktu_pos'], 'verbose_name_plural': 'Berita'},
        ),
        migrations.AlterModelOptions(
            name='pelatih',
            options={'ordering': ['nama_lengkap'], 'verbose_name_plural': 'Pelatih'},
        ),
        migrations.AlterModelOptions(
            name='pesanan',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Pesanan'},
        ),
        migrations.AlterModelOptions(
            name='produk',
            options={'ordering': ['nama_produk'], 'verbose_name_plural': 'Produk'},
        ),
        migrations.AlterModelOptions(
            name='siswa',
            options={'ordering': ['nama_lengkap'], 'verbose_name_plural': 'Siswa'},
        ),
        migrations.AddField(
            model_name='siswa',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pesanan',
            name='pelatih',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.pelatih'),
        ),
        migrations.AlterField(
            model_name='pesanan',
            name='produk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.produk'),
        ),
        migrations.AlterField(
            model_name='pesanan',
            name='siswa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.siswa'),
        ),
    ]
