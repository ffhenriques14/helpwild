from django.forms import ModelForm
from django import forms
from matplotlib import widgets
from .models import Donate, Quiz, Comments
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class DonateForm(ModelForm):
    cardname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Card name",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    value = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Donation amount",
                "class": "form-control"
            }
        ))

    class Meta:
        model = Donate
        fields = ('cardname', 'email', 'value')


class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o seu nome'}),
        }
        labels = {

            'nome': 'Qual o seu nome?',

            # Quantos Animais morreram no ano de 2021? (10789)
            'pergunta1': 'Quantos Animais morreram no ano de 2021?',

            # O que é a HelpWild? (Instituição de proteção dos animais em via de extinção)
            'pergunta2': 'O que é a HelpWild? ',

            # Em que ano foi extinto o Tigre da Sibéria? (2005)
            'pergunta3': 'Em que ano foi extinto o Tigre da Sibéria? ',

            # Em que ano foi dada a maior quantidade de mortes de uma só especie de animais? (1991)
            'pergunta4': 'Em que ano foi dada a maior quantidade de mortes de uma só especie de animais?',

            # Qual a especie com menos animais no mundo? (Garça da Tunisia)
            'pergunta5': 'Qual a especie com menos animais no mundo?',

        }

        help_texts = {
            'pergunta1': '(escreva em minusculas)',
            'pergunta2': '(escreva em minusculas)',
            'pergunta5': '(escreva em minusculas)',
        }


class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição da tarefa...'}),
            'prioridade': forms.NumberInput(attrs={'class': 'form-control', 'max': 3, 'min': 1}),
        }
        # texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Título',
            'concluido': 'Concluída',

        }

        # texto auxiliar a um determinado campo do formulário
        help_texts = {
            'prioridade': ' prioridade: baixa=1, media=2, alta=3',
        }
