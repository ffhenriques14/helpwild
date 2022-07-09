from venv import create
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# class User(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200, null=True)
#     phone = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200, null=True)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)

#     def __str__(self):
#         return self.name


class Customer(models.Model):
    # donation = models.ManyToManyField(Donate)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Donate(models.Model):
    # customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    cardname = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    value = models.IntegerField(default='0')

    def __str__(self):
        return f"{self.cardname}"


class Quiz(models.Model):
    nome = models.CharField(max_length=50)
    # Quantos Animais morrem por ano? (10789)
    pergunta1 = models.CharField(max_length=50)
    # O que é a HelpWild? (Instituição de proteção dos animais em via de extinção)
    pergunta2 = models.CharField(max_length=100)
    # Em que ano foi extinto o Tigre da Sibéria? (2005)
    pergunta3 = models.CharField(max_length=10)
    # Em que ano foi dada a maior quantidade de mortes de uma só especie de animais? (1991)
    pergunta4 = models.CharField(max_length=10)
    # Qual o animal que esá mais em vias de extinção (Garça da Tunisia)
    pergunta5 = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome}"


class Comments(models.Model):
    autor = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.autor}"
