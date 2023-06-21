from django.contrib import admin
from .models import Compra,Genero,Comuna,Cliente
# Register your models here.
admin.site.register(Compra)
admin.site.register(Genero)
admin.site.register(Comuna)
admin.site.register(Cliente)