from django.db import models

# Create your models here.
class programmer (models.Model):
    fullname =models.CharField(max_length=50)
    nickname =models.CharField(max_length=30)
    age= models.PositiveSmallIntegerField(default=True)
    is_active =models.BooleanField(default=True)
    