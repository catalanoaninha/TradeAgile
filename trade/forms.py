#Importa modelos e configurações
from django import forms
from .models import Cliente
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


#Carrega configurações do Django nos formulários criados
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True) #Define que o Email é obrigatório inserir

    class Meta:
        model = User #Modelo do Django para o formulário
        fields = ('username', 'email', 'password1', 'password2') #Campos do form
