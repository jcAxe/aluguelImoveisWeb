from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^', include('projectbase.urls', namespace='projectbase')),
    url(r'^aluguel/', include('aluguel.urls', namespace='aluguel')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
