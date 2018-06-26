from django.shortcuts import render
from django.shortcuts import get_object_or_404
import googlemaps

from aluguel.models import Categoria, Imovel
from aluguel.forms import EnderecoForm


def lista_imoveis(request, slug_da_categoria=None):
    categoria = None
    proximidade = False
    categorias = Categoria.objects.all()
    imoveis = Imovel.objects.filter(disponivel=True)
    if slug_da_categoria:
        categoria = get_object_or_404(Categoria, slug=slug_da_categoria)
        imoveis = imoveis.filter(categoria=categoria)

    return render(request, 'aluguel/imovel/lista.html', {
        'categorias': categorias,
        'imoveis': imoveis,
        'categoria': categoria,
        'proximidade': proximidade,
        })

def lista_proximidade(request):
    categoria = None
    proximidade = True
    endereco = None
    categorias = Categoria.objects.all()
    imoveis = Imovel.objects.filter(disponivel=True)
    form = EnderecoForm()

    return render(request, 'aluguel/imovel/lista.html', {
        'categorias': categorias,
        'imoveis': imoveis,
        'categoria': categoria,
        'proximidade':proximidade,
        'endereco':endereco,
        'form':form,
        })

def busca_proximidade(request):
    categoria = None
    proximidade = True
    endereco = None
    categorias = Categoria.objects.all()
    imoveis = Imovel.objects.filter(disponivel=True)
    buscou = False
    if request.method == 'POST':
        form = EnderecoForm(request.POST)
        imoveis = Imovel.objects.filter(disponivel=True)
        imoveis_proximos = []

        if form.is_valid():
            buscou = True

            endereco = form.cleaned_data['endereco']
            g_maps = googlemaps.Client("AIzaSyCAvoQ71ulU2zlKfea1QfARc7aQlzVLCfo")
            geo_code = g_maps.geocode(endereco)

            latitude = geo_code[0]['geometry']['location']['lat']
            longitude = geo_code[0]['geometry']['location']['lng']

            for imovel in imoveis:
                geo_code_imovel = g_maps.geocode(imovel.endereco)
                imovel_latitude = geo_code_imovel[0]['geometry']['location']['lat']
                imovel_longitude = geo_code_imovel[0]['geometry']['location']['lng']
                if((abs(latitude-imovel_latitude)< 0.1)
                   and (abs(longitude-imovel_longitude)< 0.1)):
                    imoveis_proximos.append(imovel)



    else:
        form = EnderecoForm()

    return render(request, 'aluguel/imovel/lista.html', {
        'form': form,
        'categorias': categorias,
        'imoveis': imoveis,
        'categoria': categoria,
        'proximidade': proximidade,
        'endereco': endereco,
        'imoveis_proximos':imoveis_proximos,
        'buscou':buscou,
        })



def exibe_imovel(request, id, slug_do_imovel):
    imovel = get_object_or_404(Imovel, id=id,
                               slug=slug_do_imovel, disponivel=True)
    return render(request, 'aluguel/imovel/exibe.html', {'imovel': imovel})

def sucesso_aluguel(request, id, slug_do_imovel):
    imovel = get_object_or_404(Imovel, id=id, slug=slug_do_imovel, disponivel=True)
    endereco = imovel.endereco
    return render(request, 'aluguel/imovel/sucessoAluguel.html', {
        'imovel': imovel,
        'endereco':endereco,
        })
