from django import forms
from crud.models import Funcionario


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        exclude = ()

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'autofocus': ''}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'funcao': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'pattern': '\d*', 'maxlength': '11'}),
        }
