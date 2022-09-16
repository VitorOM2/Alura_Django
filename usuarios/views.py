from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User


def cadastro(request):
    """Função com as validações do cadastro de usuários e que renderiza a view de cadastros"""
    if  request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':      
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
    
        if not nome.strip():  # Verifica se o campo nome está vazio
            print('O campo não pode ficar em branco')
            return redirect('cadastro')
        
        if not email.strip():  # Verifica se o campo email está vazio
            print('O campo email não pode ficar em branco')
            return redirect('cadastro')
        
        if senha != senha2:  # Verifica se o campo das senhas são iguais
            print('As senhas não são iguais')
            return redirect('cadastro')
        
        if User.objects.filter(email=email).exists():  # Verifica se o usuário existe
            print('Usuário já cadastrado')
            return redirect('cadastro')
        
        # Cria o usuário
        user = User.objects.create_user(username=nome, email=email,
                                        password=senha)
        user.save()
        
        print('\n ==================== Usuário Criado com Sucesso ==================== \n')
        
        return redirect('login')
    return render(request, 'usuarios/cadastro.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/dashboard.html')
    return redirect('index')

def login(request):
    """Função com as validações do login de usuários e que renderiza a view de login"""
    if  request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        
        if email == "" or senha == "":
            print("Email e Senhas não podem estar vazios")
            return redirect('login')
        
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            
            if user is not None:
                auth.login(request, user)
                print('\n ==================== Login Realizado com Sucesso ==================== \n')     
                return redirect('dashboard')
    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    print('\n ==================== Logout Realizado com Sucesso ==================== \n')
    return redirect('index')

def criar_receitas(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/criar_receitas.html')
    return redirect('index')