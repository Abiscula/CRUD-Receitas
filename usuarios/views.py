from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if not nome.strip():
            print('O campo nome deve ser preenchido')
            return redirect('cadastro')
        if not email.strip():
            print('O campo email deve ser preenchido')
            return redirect('cadastro')
        if senha != senha2:
            print('As senhas devem ser iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print('Usuário já cadastrado!')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        print('Usuário cadastrado com sucesso!')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == '' or senha == '':
            print('Os campos email e senha não podem ficar em branco')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email = email).values_list('username', flat=True).get() # se o email for real trás o usuario
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('dashboard')
    return render(request, 'usuarios/login.html')


def logout(request):
    pass


def dashboard(request):
    return render(request, 'usuarios/dashboard.html')

