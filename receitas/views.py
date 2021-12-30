from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receita

def index(request):

    dados = {
        'receitas': Receita.objects.filter(publicada=True)
    }
    
    return render(request, 'index.html', dados)


def receita(request, receita_id): # recupera o id passado pela url
    
    receita_a_exibir = {
        'receita': get_object_or_404(Receita, pk=receita_id)
    }
    
    return render(request, 'receita.html', receita_a_exibir)