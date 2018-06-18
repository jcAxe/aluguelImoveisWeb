from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from aluguel.forms import ImovelForm
from aluguel.models import Imovel
# Create your views here.

def index(request):
    # return HttpResponse("Olá Mundo! Você está vendo o conteúdo da view index da aplicação 'vendas'")
    frase = "Olá mundo"
    return render(request, 'projectbase/index.html', {'frase': frase})

#def pagina1(request):
#    frase = "Você está na página 1"
#    return render(request, 'aluguel/pagina1.html', {'frase': frase})

def about(request):

    return render(request, 'projectbase/about.html')

def registrar_imovel(request):
    imovel = None
    if request.method == 'POST':
        form = ImovelForm(request.POST, request.FILES)
        if form.is_valid():
            # categoria = form.cleaned_data['categoria']
            # slug = form.cleaned_data['slug']
            # imagem = form.cleaned_data['imagem']
            # descricao = form.cleaned_data['descricao']
            # dono = form.cleaned_data['dono']
            # preco = form.cleaned_data['preco']
            # numero = form.cleaned_data['numero']
            # rua = form.cleaned_data['rua']
            # bairro = form.cleaned_data['bairro']
            # cidade = form.cleaned_data['cidade']
            # estado = form.cleaned_data['estado']
            # pais = form.cleaned_data['pais']
            # cep = form.cleaned_data['cep']
            # disponivel = forms.BooleanField(default=True)
            form.save()
            # endereco = form.cleaned_data['endereco']
            # imovel = Imovel.objects.create(
            #     categoria = categoria,
            #     slug = slug,
            #     imagem=imagem,
            #     descricao = descricao,
            #     dono=dono,
            #     preco=preco,
            #     numero=numero,
            #     rua=rua,
            #     bairro = bairro,
            #     cidade = cidade,
            #     estado = estado,
            #     pais = pais,
            #     cep = cep,
            #     endereco = endereco)
            return HttpResponseRedirect(reverse('projectbase:sucesso_registro'))
    else:
        form = ImovelForm()

    return render(request, 'projectbase/registrar.html', {'form': form})

def sucesso_registro(request):

    return render(request, 'projectbase/registroSucesso.html')
