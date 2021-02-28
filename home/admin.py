# Register your models here.
from django.contrib import admin
from .models import Grupo_Itemurl, Itemurl

# Register your models here.
class ItemMenuInline(admin.TabularInline):
    model = Itemurl
    extra = 5

class GruposMenulAdmin(admin.ModelAdmin):
    inlines = [ItemMenuInline]
    list_display = ('description_1', 'description_2', 'create_date','order')
    list_filter = ['create_date']
    search_fields = ['description_1']

admin.site.register(Grupo_Itemurl, GruposMenulAdmin)