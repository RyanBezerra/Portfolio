from django.db import models
from uuid import uuid4
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Jogos(models.Model):

    chave_jogo = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    Nome = models.CharField(max_length=255)
    Desenvolvedora = models.CharField(max_length=255)
    Versão = models.CharField(max_length=255)
    Categoria = models.CharField(max_length=255)
    Média_Avaliações = models.FloatField(
        validators=[
            MinValueValidator(0.0),  
            MaxValueValidator(10.0)
        ]
    )
    Média_Horas_Jogando = models.CharField(max_length=255)

