from django.db import models
from datetime import datetime

class Receita(models.Model):
    nome_receita = models.CharField(max_length=200) # cria campo do tipo char com máximo 200 caracteres
    ingredientes = models.TextField() # cria campo do tipo texto
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField() # cria campo do tipo inteiro
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now(), blank=True) # cria campo do tipo date e pega o valor default do datetime