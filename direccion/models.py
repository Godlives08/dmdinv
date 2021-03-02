from django.db import models

# Create your models here.
class Pais(models.Model):
    description = models.CharField(max_length=155,default='')
    iso = models.CharField(max_length=155,default='')
    traduccion = models.CharField(max_length=155,default='')
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.description
    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'

class Provincia(models.Model):
    pais = models.ForeignKey(Pais,on_delete=models.CASCADE)
    description = models.CharField(max_length=155,default='')
    traduccion = models.CharField(max_length=155,default='')
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.description
    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'

class Sector(models.Model):
    provincias = models.ForeignKey(Provincia,on_delete=models.CASCADE)
    description = models.CharField(max_length=155,default='')
    traduccion = models.CharField(max_length=155,default='')
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.description
    class Meta:
        verbose_name = 'Sector'
        verbose_name_plural = 'Sector'

class Barrio(models.Model):
    sector = models.ForeignKey(Sector,on_delete=models.CASCADE)
    description = models.TextField(default='')
    traduccion = models.CharField(max_length=155,default='')
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.description
    class Meta:
        verbose_name = 'Barrio'
        verbose_name_plural = 'Barrio'