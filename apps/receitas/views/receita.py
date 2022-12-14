# pylint: disable=import-error
"""Importação do Render"""
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from receitas.models import Receita


def index(request):
    """Configura a view da página Index"""
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)
    paginator = Paginator(receitas, 6)
    page = request.GET.get('page')
    receitas_por_pagina = paginator.get_page(page)
    
    dados = {
        'receitas' : receitas_por_pagina
    }
    return render(request, 'receitas/index.html',dados)

def receita(request, receita_id):
    """Configura a página Receita"""
    receita = get_object_or_404(Receita, pk=receita_id)   
    receita_a_exibir = {
        'receita': receita
    }
    return render(request, 'receitas/receita.html', receita_a_exibir)

def criar_receitas(request):
    """ Realiza a criação de receitas """
    if request.method == 'POST':
        nome_receita  = request.POST['nome_receita']
        ingredientes  = request.POST['ingredientes']
        modo_preparo  = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento    = request.POST['rendimento']
        categoria     = request.POST['categoria']
        foto_receita  = request.FILES['foto_receita']
        user = get_object_or_404(User, pk=request.user.id)
        receitas = Receita.objects.create(pessoa=user,nome_receita=nome_receita, ingredientes=ingredientes, modo_preparo=modo_preparo,tempo_preparo=tempo_preparo, rendimento=rendimento,categoria=categoria, foto_receita=foto_receita)
        receitas.save()
        return redirect('dashboard')
    else:
        return render(request, 'receitas/criar_receitas.html')

def deletar_receita(request, receita_id):
    """Exclui uma receita"""
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')

def editar_receita(request, receita_id):
    """ Edita uma receita """
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_editar = { 'receita':receita }
    return render(request, 'receitas/editar_receita.html', receita_a_editar)

def atualiza_receita(request):
    """ Atualiza os dados da receita após editar"""
    if request.method == 'POST':
        receita_id = request.POST['receita_id']
        receita = Receita.objects.get(pk=receita_id)
        receita.nome_receita   = request.POST['nome_receita']
        receita.ingredientes   = request.POST['ingredientes']
        receita.modo_preparo   = request.POST['modo_preparo']
        receita.tempo_preparo  = request.POST['tempo_preparo']
        receita.rendimento     = request.POST['rendimento']
        receita.categoria      = request.POST['categoria']
        
        if 'foto_receita' in request.FILES:
            receita.foto_receita = request.FILES['foto_receita']
            
        receita.save()
        return redirect('dashboard')
