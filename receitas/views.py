# pylint: disable=import-error
"""Importação do Render"""
from django.shortcuts import render


def index(request):
    """Cria a view da página Index"""
    receitas = {
        1:'Lasanha',
        2:'Pizza',
        3:'Sorvete',
        4:'Sopa de Legumes'
    }
    dados = {
        'nome_das_receitas' : receitas
    }
    return render(request, 'index.html',dados)

def receita(request):
    """Retorna a página Receita"""
    return render(request, 'receita.html')
