from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Type(models.Model):
    type_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.type_name.title()}'

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    code = models.CharField('Codigo', max_length=30, null=True, blank=True)
    name = models.CharField('Nombre Item', max_length=30)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField('Precio Unitario', default='0', null=True, blank=True)
    quantity = models.IntegerField('Cantidad en Stock',default='0', null=True, blank=True )

    date_create = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
