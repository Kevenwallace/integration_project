from django.db import models

# Create your models here.
class cores(models.Model):
    cor = models.CharField()
    index = models.BigAutoField()

class Estoque(models.Model):
    nome = models.CharField()
    sku = models.CharField(max_length=15)
    cor = models.IntegerField()
    