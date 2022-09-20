from django.urls import path

from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('criar/receitas', views.criar_receitas, name='criar_receitas'),
    path('deletar_receita/<int:receita_id>', views.deletar_receita, name='deletar_receita'),
    path('editar_receita/<int:receita_id>', views.editar_receita, name='editar_receita'),
    path('atualiza_receita', views.atualiza_receita, name='atualiza_receita')
    
]
