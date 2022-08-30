# pylint: disable=import-error
"""Importação do Render"""
from django.shortcuts import render
from .models import Receita


def index(request):
    """Cria a view da página Index"""
    receitas = Receita.objects.all()
    dados = {
        'receitas' : receitas
    }
    return render(request, 'index.html',dados)

def receita(request):
    """Retorna a página Receita"""
    return render(request, 'receita.html')
