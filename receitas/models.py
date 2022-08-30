from django.db import models
from datetime import datetime


class Receita(models.Model):
    
    # ========================= CAMPOS =========================
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
