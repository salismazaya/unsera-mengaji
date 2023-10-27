from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth import login as auth_login
from main.models import User, Customer, Absen
from main.forms import LoginForm, RegisterForm

@require_http_methods(['GET', 'POST'])
def index(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('/dashboard/')

    if request.method == 'GET':
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, 'main/index.html', context)

    form = LoginForm(request.POST)

    if form.is_valid():
        user = User.objects.cache().get(username = form.cleaned_data['username'])
        auth_login(request, user)
        return redirect('/dashboard')

    context = {
        'form': form
    }
    return render(request, 'main/index.html', context)

@require_http_methods(['GET', 'POST'])
def register(request: HttpRequest):
    if request.method == 'GET':
        form = RegisterForm()
        context = {
            'form': form
        }
        return render(request, 'main/register.html', context)

    form = RegisterForm(request.POST)
    if form.is_valid():
        with transaction.atomic():
            user = User()
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password'])
            user.save()

            customer = Customer()
            customer.user = user
            customer.nama = form.cleaned_data['nama']
            customer.nim = form.cleaned_data['nim']
            customer.kelas = form.cleaned_data['kelas']
            customer.jurusan = form.cleaned_data['jurusan']
            customer.dosen = form.cleaned_data['nama_dosen']
            customer.nowa = form.cleaned_data['nomor_whatsapp']
            customer.save()
            auth_login(request, user)
            return redirect('/dashboard')

    context = {
        'form': form
    }
    return render(request, 'main/register.html', context)


@login_required
def dashboard(request: HttpRequest):
    customer = Customer.objects.cache().get(user__pk = request.user.pk)
    absen = Absen.objects.cache().filter(customer__id = customer.id)
    context = {
        'customer': customer,
        'absen': absen,
    }
    
    return render(request, 'main/dashboard.html', context)