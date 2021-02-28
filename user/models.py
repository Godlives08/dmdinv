from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    nivelsecurity = models.IntegerField(default=100)
    niveladmin = models.IntegerField(default=100) 
    cambiopass = models.BooleanField(default=True)
    ipontrol = models.TextField(max_length=155,default='')
    parametros = models.TextField(default='')
    timeseccion = models.IntegerField(default=3600)
