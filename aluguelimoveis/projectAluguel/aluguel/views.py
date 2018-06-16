from .forms import EnderecoForm
import googlemaps


from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect


from django.shortcuts import render, get_object_or_404
from .models import Categoria, Imovel



def lista_imoveis(request, slug_da_categoria=None):
    categoria = None
    proximidade = False
    categorias = Categoria.objects.all()
    imoveis = Imovel.objects.filter(disponivel=True)
    if slug_da_categoria:
        categoria = get_object_or_404(Categoria, slug=slug_da_categoria)
        imoveis = imoveis.filter(categoria=categoria)

    return render(request, 'aluguel/imovel/lista.html', {'categorias': categorias,
                                                         'imoveis': imoveis,
                                                         'categoria': categoria,
                                                         'proximidade': proximidade})
def lista_proximidade(request):
    latitude = None
    longitude = None
    categoria = None
    proximidade = True
    endereco = None
    categorias = Categoria.objects.all()
    imoveis = Imovel.objects.filter(disponivel=True)
    form = EnderecoForm()  # A form bound to the POST data


    return render(request, 'aluguel/imovel/lista.html', {'categorias': categorias,
                                                         'imoveis': imoveis,
                                                         'categoria': categoria,
                                                         'proximidade':proximidade,
                                                         'latitude': latitude,
                                                         'longitude': longitude,
                                                         'endereco':endereco,
                                                         'form':form})


def busca_proximidade(request):
    categoria = None
    proximidade = True
    endereco = None

    categorias = Categoria.objects.all()
    imoveis = Imovel.objects.filter(disponivel=True)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EnderecoForm(request.POST)
        imoveis = Imovel.objects.filter(disponivel=True)
        imoveisProximos = []

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            endereco = form.cleaned_data['endereco']
            #AIzaSyCAvoQ71ulU2zlKfea1QfARc7aQlzVLCfo
            gmaps = googlemaps.Client("AIzaSyCAvoQ71ulU2zlKfea1QfARc7aQlzVLCfo")
            geocode = gmaps.geocode(endereco)

            latitude = geocode[0]['geometry']['location']['lat']
            longitude = geocode[0]['geometry']['location']['lng']
            for imovel in imoveis:
                geocodeImovel = gmaps.geocode(imovel.endereco)
                imovelLat = geocodeImovel[0]['geometry']['location']['lat']
                imovelLon = geocodeImovel[0]['geometry']['location']['lng']
                if((abs(latitude-imovelLat)< 0.1)and (abs(longitude-imovelLon)< 0.1)):
                    imoveisProximos.append(imovel)



            #print(lng)
            print(imoveisProximos)


    # if a GET (or any other method) we'll create a blank form
    else:
        form = EnderecoForm()

    return render(request, 'aluguel/imovel/lista.html', {'form': form,
                                                         'categorias': categorias,
                                                         'imoveis': imoveis,
                                                         'categoria': categoria,
                                                         'proximidade': proximidade,
                                                         'endereco': endereco,
                                                         'imoveisProximos':imoveisProximos}
                  )



def exibe_imovel(request, id, slug_do_imovel):
    # Esta view espera receber o id do produto e seu slug para recuperar o produto
    # Podemos recuperar o produto apenas com o seu id uma vez que ele é unique.
    # Incluímos o slug para podermos construir 'SEO friendly URLs'.
    # SEO = Search Engine Optimization.
    # Exemplo: http://www.dominio.com.br/produto?id=721 <== Ruim
    # Exemplo: http://www.dominio.com.br/721/notebook-del-vostro-3458-i3 <== Bom

    imovel = get_object_or_404(Imovel, id=id, slug=slug_do_imovel, disponivel=True)
    return render(
        request, 'aluguel/imovel/exibe.html', {'imovel': imovel})