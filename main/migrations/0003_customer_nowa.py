# Generated by Django 4.2.6 on 2023-10-27 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_absen_tanggal'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='nowa',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
