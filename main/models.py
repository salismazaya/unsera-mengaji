from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Customer(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = 'Peserta'

    user = models.OneToOneField(User, on_delete = models.PROTECT)
    nama = models.CharField(max_length = 255)
    nim = models.PositiveBigIntegerField()
    kelas = models.CharField(max_length = 255)
    jurusan = models.CharField(max_length = 255)
    dosen = models.CharField(max_length = 255)
    nowa = models.CharField(max_length = 255, null = True, blank = True)


    def __str__(self):
        return self.nama
    
class Absen(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = 'Absen'
        unique_together = ('customer', 'tanggal')

    customer = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name = 'sekeren')
    tanggal = models.DateField(default = timezone.now)