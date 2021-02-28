from django.contrib import admin

# Register your models here.
from .models import Sucursal

class SucursalAdmin(admin.ModelAdmin):
    list_display = ('description', 'sigla', 'created_at')
    list_filter = ['created_at']
    search_fields = ['description']

admin.site.register(Sucursal, SucursalAdmin)