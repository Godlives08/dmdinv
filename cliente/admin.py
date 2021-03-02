from django.contrib import admin

# Register your models here.
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'cedopass')
    list_filter = ['created_at']
    search_fields = ['nombre']

admin.site.register(Cliente, ClienteAdmin)