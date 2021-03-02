from django.contrib import admin

# Register your models here.
from .models import Pais, Provincia, Sector, Barrio

class PaisAdmin(admin.ModelAdmin):
    list_display = ('description', 'iso', 'activo')
    search_fields = ['description']

class ProvinciaslAdmin(admin.ModelAdmin):
    list_display = ('description', 'pais', 'activo')
    list_filter = ['pais']
    search_fields = ['description']

class SectorAdmin(admin.ModelAdmin):
    list_display = ('description', 'provincias', 'activo')
    list_filter = ['provincias']
    search_fields = ['description']

class BarrioAdmin(admin.ModelAdmin):
    list_display = ('description','sector', 'activo')
    list_filter = ['sector']
    search_fields = ['description']

admin.site.register(Pais, PaisAdmin)
admin.site.register(Provincia, ProvinciaslAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Barrio, BarrioAdmin)