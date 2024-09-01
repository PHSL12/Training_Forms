from django.shortcuts import render
from matricula.forms import AlunoForm

# Create your views here.
def cadastro_aluno(request):
    form = AlunoForm
    return render(request, 'form.html', {'form': form})