from django.db import models

class Menu(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=10)

    def __str__(self):
        return self.nome


