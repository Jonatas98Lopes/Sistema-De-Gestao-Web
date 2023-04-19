from django.db import models

class Entretenimento(models.Model):
    nome = models.TextField(max_length=255)
    finalizado = models.BooleanField(default=False)
    resenha = models.TextField(max_length=500)
