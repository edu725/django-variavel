from django.db import models

# Create your models here.

class Picture(models.Model):
    img = models.ImageField(upload_to='imagens/')

class Itens(models.Model):
    nome = models.CharField(max_length=240)
    email = models.EmailField()