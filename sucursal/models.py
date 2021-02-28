from django.db import models
from django.utils import timezone
from django.db import models
# Create your models here.


class Sucursal(models.Model):
    description = models.CharField(max_length=155) 
    sigla = models.CharField(max_length=5) 
    calle = models.CharField(max_length=155) 
    local = models.CharField(max_length=155) 
    ciudad = models.CharField(max_length=155) 
    municipio = models.CharField(max_length=155) 
    pais = models.CharField(max_length=155) 
    longitud = models.CharField(max_length=155) 
    latitud = models.CharField(max_length=155) 
    email = models.CharField(max_length=155) 
    email2 = models.CharField(max_length=155) 
    telefono = models.CharField(max_length=155) 
    telefono2 = models.CharField(max_length=155) 
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.description
    def __str__(self):
        return self.Sigla

    class Meta:
        permissions = (("permiso_versucursal", "Permiso a ver Sucursal"),("permiso_crearsucursal", "Permiso a Crear Sucursal"),("permiso_actualizarsucursal", "Permiso a Actualizar Sucursal"),("permiso_eliminarsucursal", "Permiso a Eliminar Sucursal"))
        verbose_name = 'Sucursal' 
        verbose_name_plural = 'Sucursales'
