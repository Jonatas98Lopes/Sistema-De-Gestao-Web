from django.shortcuts import render, redirect
from .models import Entretenimento
from .forms import EntretenimentoForm
def pagina_inicial(request):
    dados = {
        'dados': Entretenimento.objects.all()
    }
    return render(request,'app_web/pagina_inicial.html', context=dados)


def novo_conteudo(request):
    if request.method == 'POST':
        entretenimento = EntretenimentoForm(request.POST)
        if entretenimento.is_valid():
            entretenimento.save()
            return redirect('pagina_inicial')
    entretenimento = EntretenimentoForm()
    return render(request, 'app_web/novo_conteudo.html', {'formulario': entretenimento})
    
