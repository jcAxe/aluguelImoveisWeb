from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from aluguel.forms import ImovelForm

def index(request):
    frase = "Olá mundo"
    return render(request, 'projectbase/index.html', {'frase': frase})


def about(request):

    return render(request, 'projectbase/about.html')

def registrar_imovel(request):
    imovel = None
    if request.method == 'POST':
        form = ImovelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('projectbase:sucesso_registro'))
    else:
        form = ImovelForm()

    return render(request, 'projectbase/registrar.html', {'form': form})

def sucesso_registro(request):

    return render(request, 'projectbase/registroSucesso.html')
