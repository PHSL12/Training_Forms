from matricula.models import Aluno
from django import forms

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'
        labels = {
            'nome': 'Nome',
            'endereco': 'Endereço',
            'cidade': 'Cidade',
            'email': 'E-mail',
            'curso': 'Curso'
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'curso': forms.TextInput(attrs={'class': 'form-control'}),
        }