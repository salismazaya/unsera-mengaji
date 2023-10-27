from django.contrib import admin
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User as AuthUser, Group as AuthGroup
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin, GroupAdmin as AuthGroupAdmin
from django.urls import path
from main.models import Customer, Absen
import json

class AdminSite(admin.AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        last_url = urls.pop()

        urls.extend([
            path('qr/', self.qr_view, name = 'qr'),
            path('api/qr/', self.scan),
        ])
        urls.append(last_url)

        return urls

    def qr_view(self, request: HttpRequest):
        if not request.user.is_staff:
            return HttpResponse('Forbidden')

        context = self.each_context(request)
        context['title'] = 'Scan'
        return render(request, 'admin/qr.html', context)

    @csrf_exempt
    def scan(self, request: HttpRequest):
        if not request.user.is_staff:
            return HttpResponse('Forbidden')
        
        data = json.loads(request.body)
        customer_id = data.get('id')

        try:
            if customer_id:
                customer = Customer.objects.filter(pk = customer_id).first()
                if customer:
                    absen = Absen()
                    absen.customer = customer
                    absen.save()

                    return HttpResponse(customer.nama)
        except:
            pass
            
        return HttpResponse('!')

admin_site = AdminSite()
admin_site.register(AuthUser, AuthUserAdmin)
admin_site.register(AuthGroup, AuthGroupAdmin)

class CustomerAdmin(admin.ModelAdmin):
    search_fields = ('nama', 'nim', 'dosen', 'jurusan', 'kelas')

admin_site.register(Customer, CustomerAdmin)

class AbsenAdmin(admin.ModelAdmin):
    list_display = ('customer', 'tanggal')
    search_fields = ('customer__nama', 'customer__nim')


admin_site.register(Absen, AbsenAdmin)