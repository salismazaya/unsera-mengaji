# Generated by Django 4.2.6 on 2023-10-26 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('nim', models.PositiveBigIntegerField()),
                ('kelas', models.CharField(max_length=255)),
                ('jurusan', models.CharField(max_length=255)),
                ('dosen', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Peserta',
                'verbose_name_plural': 'Peserta',
            },
        ),
        migrations.CreateModel(
            name='Absen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sekeren', to='main.customer')),
            ],
            options={
                'verbose_name': 'Absen',
                'verbose_name_plural': 'Absen',
                'unique_together': {('customer', 'tanggal')},
            },
        ),
    ]