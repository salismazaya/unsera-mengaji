# Generated by Django 4.2.6 on 2023-10-26 16:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absen',
            name='tanggal',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
