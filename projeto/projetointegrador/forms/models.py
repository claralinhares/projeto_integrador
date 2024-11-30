from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14)