from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    STATUS_CHOICES = (
        ('A', 'Aridos'),
        ('B', 'Mamposteria'),
        ('C', 'Griferia')   
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    code = models.CharField('Codigo', max_length=30)
    name = models.CharField('Nombre Item', max_length=30)
    tipe = models.CharField('Tipo de Item', max_length=20, choices=STATUS_CHOICES, default='A')
    price = models.CharField('Precio Unitario', max_length=30)
    quantity = models.CharField('Cantidad en Stock',max_length=30)

    date_create = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)