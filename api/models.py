from django.db import models

# Create your models here.


class Contato(models.Model):

    nome = models.CharField(max_length=255, null=False)
    canal = models.CharField(max_length=255, null=False)
    valor = models.CharField(max_length=100, null=False)
    obs = models.TextField()

    def __str__(self):
        return self.nome
