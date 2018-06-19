from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.lista_imoveis, name='lista_imoveis'),
    url(r'^proximidade/$', views.lista_proximidade, name='proximidade'),
    url(r'^busca/$', views.busca_proximidade, name='busca_proximidade'),
    url(r'^(?P<id>\d+)/(?P<slug_do_imovel>[-\w]+)/sucesso/$', views.sucesso_aluguel, name='sucesso_aluguel'),
    url(r'^(?P<slug_da_categoria>[-\w]+)/$', views.lista_imoveis, name='lista_imoveis_por_categoria'),
    url(r'^(?P<id>\d+)/(?P<slug_do_imovel>[-\w]+)/$', views.exibe_imovel, name='exibe_imovel'),
]
