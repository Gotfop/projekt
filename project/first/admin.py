from django.contrib import admin
from .models import Tomat, Oder, Client

# Register your models here.
@admin.register(Tomat)
class TomatoAdmin(admin.ModelAdmin):
    list_display = ['color','weight','price']


@admin.register(Oder)
class OderAdmin(admin.ModelAdmin):
    list_display = ['number_order','client_id','date','status']
    ordering = ['number_order']
    list_editable = ['status']
    list_filter = ['status','date']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name','email','addres']


