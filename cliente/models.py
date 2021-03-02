import datetime
from django.utils import timezone
from django.db import models

from sucursal.models import Sucursal
from direccion.models import Pais, Provincia, Sector, Barrio
# Create your models here.

class Cliente(models.Model):
    SEXO = [('M','Masculino'),('F','Femenino'),('I','Indefinido')]
    nombre = models.CharField(max_length=155) 
    apellido = models.CharField(max_length=155)
    cedopass = models.CharField(max_length=25, unique=True)
    codigocliente = models.CharField(max_length=45,unique=True)
    pais = models.ForeignKey(Pais,on_delete=models.CASCADE)
    provincia = models.ForeignKey(Provincia,on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector,on_delete=models.CASCADE)
    barrio = models.ForeignKey(Barrio,on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal,on_delete=models.CASCADE)
    sexo = models.CharField(
        max_length=1,
        choices=SEXO,
        default='I',
    )
    fechanacimiento = models.DateField() 
    direccion = models.TextField(default='',max_length=500)
    cadelaimg = models.FileField(max_length=500)
    email = models.CharField(max_length=155)
    email2 = models.CharField(max_length=155)
    telefono = models.CharField(max_length=50)
    telefono2 = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre
    def __str__(self):
        return self.apellido
    def __str__(self):
        return self.cedopass
    def __str__(self):
        return self.codigocliente

    class Meta:
        permissions = (("permiso_vercliente", "Permiso a ver Cliente"),("permiso_crearcliente", "Permiso a Crear Cliente"),("permiso_actualizarcliente", "Permiso a Actualizar Cliente"),("permiso_eliminarcliente", "Permiso a Eliminar Cliente"))
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nombre']



