import email
from django.db import models


class Pessoas(models.Model):
    
    # ========================= CAMPOS =========================
    # CharFields
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome
    