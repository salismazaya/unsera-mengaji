from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from main.models import Customer, User

class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 30, min_length = 3, validators = [
        RegexValidator(r'^\w+$')
    ])
    nama = forms.CharField(max_length = 255)
    nim = forms.CharField(max_length = 20, validators = [
        RegexValidator(r'^\d+$')
    ])
    kelas = forms.CharField(max_length = 5)
    jurusan = forms.CharField(max_length = 255)
    nama_dosen = forms.CharField(max_length = 255)
    password = forms.CharField(widget = forms.PasswordInput())
    konfirmasi_password = forms.CharField(widget = forms.PasswordInput())
    nomor_whatsapp = forms.CharField(max_length = 255, required = False)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username = username).exists():
            raise ValidationError('username sudah ada')
        
        return username
    
    def konfirmasi_password_clean(self):
        password = self.cleaned_data['konfirmasi_password']
        password2 = self.data['password']

        if password != password2:
            raise ValidationError('password tidak sama')
        
        return password


class LoginForm(forms.Form):
    username = forms.CharField(max_length = 30, min_length = 3)
    password = forms.CharField(widget = forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data['username']

        if not User.objects.filter(username = username).exists():
            raise ValidationError('username tidak ditemukan')

        return username
    
    def clean_password(self):
        password = self.cleaned_data['password']

        user = User.objects.filter(username = self.data['username']).first()
        if user:
            if not user.check_password(password):
                raise ValidationError('password salah')


        return password