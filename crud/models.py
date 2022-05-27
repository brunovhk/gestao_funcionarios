from django.db import models


class Funcionario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    funcao = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    telefone = models.IntegerField()