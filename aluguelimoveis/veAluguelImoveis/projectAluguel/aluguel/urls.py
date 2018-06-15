from django.conf.urls import url
from . import views


urlpatterns = [
    # Esta primeira view tem por objetivo listar todos os produtos


    url(r'^$', views.lista_imoveis, name='lista_imoveis'),
    url(r'^buscaproximidade/$', views.lista_proximidade, name='lista_proximidade'),
    url(r'^buscaproximidade/(?P<latitude>[-\w]+)/(?P<longitude>[-\w]+)/$', views.lista_proximidade, name='lista_proximidade'),
    # E esta view é utilizada para listar os produtos de uma determinada categoria
    url(r'^(?P<slug_da_categoria>[-\w]+)/$', views.lista_imoveis, name='lista_imoveis_por_categoria'),

    # Esta view é utilizada para exibir um determinado produto
    url(r'^(?P<id>\d+)/(?P<slug_do_imovel>[-\w]+)/$', views.exibe_imovel, name='exibe_imovel'),

    # ?	- zero ou um do elemento anterior.
    # *	- zero ou mais do elemento anterior.
    # +	- um ou mais do elemento anterior.
    # \w - para encontrar um word character. Um word character é um caracter de a-z, A-Z, 0-9, e _ (underscore).
]
