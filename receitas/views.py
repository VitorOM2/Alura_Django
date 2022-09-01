# pylint: disable=import-error
"""Importação do Render"""
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receita


def index(request):
    """Cria a view da página Index"""
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)
    dados = {
        'receitas' : receitas
    }
    return render(request, 'index.html',dados)

def receita(request, receita_id):
    """Retorna a página Receita"""
    receita = get_object_or_404(Receita, pk=receita_id)
    
    receita_a_exibir = {
        'receita': receita
    }
    
    return render(request, 'receita.html', receita_a_exibir)
