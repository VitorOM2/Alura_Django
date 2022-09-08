from django.urls import path

from . import views

urlpatterns = [
    path('Cadastro', views.cadastro, name='cadastro'),
    path('Dashboard', views.dashboard, name='dashboard'),
    path('Login', views.login, name='login'),
    path('Logout', views.logout, name='logout'),
]
