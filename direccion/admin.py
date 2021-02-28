from django.contrib import admin

# Register your models here.
from .models import Pais, Provincia, Sector

class PaisAdmin(admin.ModelAdmin):
    list_display = ('description', 'iso', 'activo')
    search_fields = ['description']

class ProvinciaslAdmin(admin.ModelAdmin):
    list_display = ('pais', 'description', 'activo')
    list_filter = ['pais']
    search_fields = ['description']

class SectorAdmin(admin.ModelAdmin):
    list_display = ('provincias', 'description', 'activo')
    list_filter = ['provincias']
    search_fields = ['description']

admin.site.register(Pais, PaisAdmin)
admin.site.register(Provincia, ProvinciaslAdmin)
admin.site.register(Sector, SectorAdmin)