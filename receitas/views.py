from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receita

def index(request):

    dados = {
        'receitas': Receita.objects.order_by('-data_receita').filter(publicada=True) #recupera os dados do banco de acordo com os filtros
    }
    
    return render(request, 'index.html', dados)


def receita(request, receita_id): # recupera o id passado pela url
    
    receita_a_exibir = {
        'receita': get_object_or_404(Receita, pk=receita_id)
    }
    
    return render(request, 'receita.html', receita_a_exibir)

def buscar(request):
    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)
    
    if 'buscar' in request.GET: #verifica se existe o buscar na requisição    
        nome_a_buscar = request.GET['buscar'] #recupera o nome digitado pela URL
        if buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar) #verifica se o nome buscado existe na lista
        
    dados = {
        'receitas': lista_receitas
    }
        
    return render(request, 'buscar.html', dados)
    