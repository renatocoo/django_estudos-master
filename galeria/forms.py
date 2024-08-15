from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Atividade, Conteudo

class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = ['titulo', 'descricao', 'data_entrega']

class ConteudoForm(forms.ModelForm):
    class Meta:
        model = Conteudo
        fields = ['titulo', 'descricao', 'arquivo', 'materia']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
