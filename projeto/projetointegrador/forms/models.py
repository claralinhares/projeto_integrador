from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14)

class Event(models.Model):
    name = models.CharField(max_length=100)  # Nome do evento
    description = models.TextField(blank=True, null=True)  # Descrição opcional
    date = models.DateField()  # Data do evento
    location = models.CharField(max_length=200)  # Local do evento

    def __str__(self):
        return self.name
class Participant(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    cpf = models.CharField(max_length=11)
    qr_code_data = models.TextField() 