# pylint: disable=import-error
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:receita_id>', receita, name='receita'),
    path('buscar', buscar, name='buscar'),
    path('criar/receitas', criar_receitas, name='criar_receitas'),
    path('deletar_receita/<int:receita_id>', deletar_receita, name='deletar_receita'),
    path('editar_receita/<int:receita_id>', editar_receita, name='editar_receita'),
    path('atualiza_receita', atualiza_receita, name='atualiza_receita'),
    
]
