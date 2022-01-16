from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if campo_vazio(nome):
            messages.error(request, 'O campo nome deve ser preenchido')
            return redirect('cadastro')
        if campo_vazio(email):
            messages.error(request, 'O campo email deve ser preenchido')
            return redirect('cadastro')
        if senha != senha2:
            messages.error(request, 'As senhas não são iguais!')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists() or User.objects.filter(username=nome).exists():
            messages.error(request, 'Usuário já cadastrado!')
            return redirect('cadastro')
        
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'Os campos email e senha não podem ficar em branco')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email = email).values_list('username', flat=True).get() # se o email for real trás o usuario
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        id_criador_receita = request.user.id
        receitas = Receita.objects.order_by('-data_receita').filter(pessoa=id_criador_receita)
        
        dados = {
            'receitas': receitas
        }
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')

def cria_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        user = get_object_or_404(User, pk=request.user.id) #recupera o id do usuario que criou a receita
        receita = Receita.objects.create(pessoa=user, nome_receita=nome_receita, ingredientes=ingredientes, 
                                         modo_preparo=modo_preparo, tempo_preparo=tempo_preparo, rendimento=rendimento, 
                                         categoria=categoria, foto_receita=foto_receita)
        receita.save() #salva receita no db
        messages.success(request, 'Receita criada com sucesso!')
        return redirect('dashboard')
    else:
        return render(request, 'usuarios/cria_receita.html')
      
def deleta_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)   
    receita.delete()
    return redirect('dashboard')

def edita_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)   
    receita_a_editar = {'receita': receita}
    return render(request, 'usuarios/edita_receita.html', receita_a_editar)
    
def atualiza_receita(request):
    if request.method == 'POST':
        receita_id = request.POST['receita_id']
        r = Receita.objects.get(pk=receita_id)
        r.nome_receita = request.POST['nome_receita']
        r.ingredientes = request.POST['ingredientes']
        r.modo_preparo = request.POST['modo_preparo']
        r.tempo_preparo = request.POST['tempo_preparo']
        r.rendimento = request.POST['rendimento']
        r.categoria = request.POST['categoria']
        if 'foto_receita' in request.FILES:
            r.foto_receita = request.FILES['foto_receita']
        r.save()
        return redirect('dashboard')

def campo_vazio(campo):
    return not campo.strip()