from django.shortcuts import render, redirect


def cadastro(request):
    if request.method == 'POST':
        
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha = request.POST['password2']
        
        print(f'\n ==================== Usuário Criado com Sucesso ==================== \n')
        
        return redirect('login')
    return render(request, 'usuarios/cadastro.html')

def dashboard(request):
    return render(request, 'usuarios/dashboard.html')

def login(request):
    return render(request, 'usuarios/login.html')

def logout(request):
    return render(request, 'usuarios/logout.html')
