from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pagina1/$', views.pagina1, name='pagina1'),
    url(r'^about/$', views.about, name='about'),
]