from django.db import models

# Create your models here.
# aqui se crean los modelos (las tablas o colecciones)
class programmer(models.Model):
    fullname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=30)
    age= models.PositiveSmallIntegerField(default=True)
    phone= models.CharField(max_length=20, null=True, default=None)
    is_active = models.BooleanField(default=True)




class student(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    numero_ficha = models.PositiveSmallIntegerField()
    formacion = models.CharField(max_length=50)
    fecha_ingreso = models.DateField()
    activo = models.BooleanField(default=True)