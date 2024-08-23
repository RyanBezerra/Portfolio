from django.db import models

# Create your models here.

class LivroModel(models.Model):
    nome = models.CharField(max_length=255)
    qtd_paginas = models.IntegerField()
    descricao = models.TextField()
    genero = models.CharField(max_length=255)

    def __str__(self):
        return f'o livro{self.nome} foi criado'
