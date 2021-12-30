from django.contrib import admin
from .models import Receita

class ListandoReceitas(admin.ModelAdmin): # Muda a forma com que as receitas são apresentas no admin
    list_display = ('id', 'nome_receita', 'categoria', 'tempo_preparo', 'publicada') # informações da receita que serão renderizadas no admin
    list_display_links = ('id', 'nome_receita') # transforma os campos nome e id em links para acessar a receita no admin
    search_fields = ('nome_receita',) # cria um campo de busca pelo nome da receita no admin
    list_filter = ('categoria',) # cria um campo de filtro por categoria
    list_editable = ('publicada',) # torna campos ediitaveis no menu de admin geral 
    list_per_page = 10 # cria uma paginação, exibindo 10 itens por página
    


admin.site.register(Receita, ListandoReceitas) # Cria o campo para registrar receita na aba admin