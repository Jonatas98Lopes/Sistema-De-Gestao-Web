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
    

def detalhes(request, dado_id):
    entretenimento = Entretenimento.objects.get(pk=dado_id)
    return render(request, 'app_web/detalhes.html', {'item': entretenimento})

def editar(request, dado_id):
    conteudo = Entretenimento.objects.get(pk=dado_id)
    if request.method == 'POST':
        entretenimento = EntretenimentoForm(request.POST, instance=conteudo)
        if entretenimento.is_valid():
            entretenimento.save()
            return redirect('pagina_inicial')
    forms = EntretenimentoForm(instance=conteudo)
    return render(request, 'app_web/novo_conteudo.html', {'formulario': forms})

def excluir(request, dado_id):
    if request.method == 'POST':
        entretenimento = Entretenimento.objects.get(pk=dado_id)
        entretenimento.delete()
        return redirect('pagina_inicial')
    return render(request, 'app_web/excluir.html')