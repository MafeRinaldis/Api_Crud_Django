

from django.contrib import admin
from .models import programmer, student
# Register your models here.

admin.site.register(programmer) # se registra el modelo para poder verlo en el panel de acministracion
admin.site.register(student)