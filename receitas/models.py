from distutils.command.upload import upload
from django.db import models
from datetime import datetime

from pessoas.models import Pessoas


class Receita(models.Model):
    
    # ========================= CAMPOS =========================
    # ForeingKey
    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    # CharFields
    nome_receita = models.CharField(max_length=200)
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    
    #TextFields
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    
    # IntegerFields
    tempo_preparo = models.PositiveBigIntegerField()
    
    # DateTimeFields
    data_receita = models.DateTimeField(default=datetime.now, blank=True)
    
    # ImageFields
    foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y/',blank=True)

    # BooleanFields
    publicada = models.BooleanField(default=False)