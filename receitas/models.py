from django.db import models
from datetime import datetime

from django.db.models.deletion import CASCADE
from pessoas.models import Pessoa

class Receita(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome_receita = models.CharField(max_length=200) # cria campo do tipo char com máximo 200 caracteres
    ingredientes = models.TextField() # cria campo do tipo texto
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField() # cria campo do tipo inteiro
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now(), blank=True) # cria campo do tipo date e pega o valor default do datetime
    foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    publicada = models.BooleanField(default=False)
    def __str__(self):
        return self.nome_receita