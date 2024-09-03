from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('admin/', admin.site.urls),
  path('salao/', include('salao.urls')),
  path('proprietario/', include('proprietario.urls')),
  path('cliente/', include('cliente.urls')),
  path('', lambda request: render(request, 'index.html')),
  path('pessoa/', include('django.contrib.auth.urls')),
  path('agendamento/', include('agendamento.urls')),
  path('servico/', include('servico.urls')),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)