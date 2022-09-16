from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.models import User
from receitas.models import Receita


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
            messages.error(request, 'O campo não pode ficar em branco')
        
        if not email.strip():  # Verifica se o campo email está vazio
            messages.error(request, 'O campo email não pode ficar em branco')
            return redirect('cadastro')
        
        if senha != senha2:  # Verifica se o campo das senhas são iguais
            messages.error(request, 'As senhas não são iguais')
            return redirect('cadastro')
        
        if User.objects.filter(email=email).exists():  # Verifica se o usuário existe
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro')
        
        # Cria o usuário
        user = User.objects.create_user(username=nome, email=email,
                                        password=senha)
        user.save()
        
        messages.success(request, 'Usuário Cadastrado com sucesso')
        
        return redirect('login')
    return render(request, 'usuarios/cadastro.html')

def dashboard(request):
    if request.user.is_authenticated:
        
        id = request.user.id
        
        receitas = Receita.objects.order_by('-data_receita').filter(pessoa=id)
        
        dados = {
            'receitas' : receitas
        }
        
        return render(request, 'usuarios/dashboard.html', dados)
    return redirect('index')

def login(request):
    """Função com as validações do login de usuários e que renderiza a view de login"""
    if  request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        
        if email == "" or senha == "":
            messages.error(request, 'Email e Senhas não podem estar vazios')
            return redirect('login')
        
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso')
                return redirect('dashboard')
    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def criar_receitas(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        user = get_object_or_404(User, pk=request.user.id)
        receitas = Receita.objects.create(pessoa=user,nome_receita=nome_receita, ingredientes=ingredientes, modo_preparo=modo_preparo,tempo_preparo=tempo_preparo, rendimento=rendimento,categoria=categoria, foto_receita=foto_receita)
        receitas.save()
        return redirect('dashboard')
    else:
        return render(request, 'usuarios/criar_receitas.html')
