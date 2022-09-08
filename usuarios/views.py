from django.shortcuts import render


def cadastro(request):
    render(request, 'cadastro.html')

def dashboard(request):
    render(request, 'dashboard.html')

def login(request):
    render(request, 'login.html')

def logout(request):
    render(request, 'logout.html')
