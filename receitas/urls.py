from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:receita_id>', views.receita, name='receita'), #avisa a url que irá receber um id
    path('buscar', views.buscar, name='buscar')
]