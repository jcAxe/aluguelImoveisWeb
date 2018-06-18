from django.conf.urls import url
from . import views
import aluguel

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^registrar/', views.registrar_imovel, name='registrar'),
    url(r'^registrarImovel/$', views.registrar_imovel, name='registrar_imovel'),
    url(r'^about/$', views.about, name='about'),

]