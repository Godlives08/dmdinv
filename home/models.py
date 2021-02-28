import datetime
from django.utils import timezone
from django.db import models

# Create your models here.
class Grupo_Itemurl(models.Model):
    description_1 = models.CharField(max_length=80)
    description_2 = models.CharField(max_length=80)
    icon = models.CharField(max_length=80,default='')
    create_date = models.DateField(("Date"), auto_now_add=True)
    order = models.IntegerField(default=0)
    nivelsecurity = models.IntegerField(default=100)
    niveladmin = models.IntegerField(default=100)
    order = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.description_1
    def __str__(self):
        return self.description_2
    class Meta:
        verbose_name = 'Grupo Menu'
        verbose_name_plural = 'Grupos Menu'
        permissions = (("permiso_itemurl", "Permiso a ver Url"),)
        ordering = ['order']

class Itemurl(models.Model):
    grupo = models.ForeignKey(Grupo_Itemurl, on_delete=models.CASCADE)
    description_1 = models.CharField(max_length=80)
    description_2 = models.CharField(max_length=80)
    icon = models.CharField(max_length=80,default='')
    url = models.CharField(max_length=80)
    fullurl = models.CharField(max_length=80)
    appname = models.CharField(max_length=80)
    create_date = models.DateField(("Date"), auto_now_add=True)
    nivelsecurity = models.IntegerField(default=100)
    niveladmin = models.IntegerField(default=100)
    is_staff = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.description_1
    def __str__(self):
        return self.description_2
    def __str__(self):
        return self.appname
    class Meta:
        verbose_name = 'Item Menu'
        verbose_name_plural = 'Items Menu'
        ordering = ['order']
    
