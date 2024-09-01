from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path

urlpatterns = [
  path('admin/', admin.site.urls),
  path('saloes/', include('salao.urls')),
  path('proprietario/', include('proprietario.urls')),
  path('cliente/', include('cliente.urls')),
  path('', lambda request: render(request, 'index.html')),
  path('pessoa/', include('django.contrib.auth.urls')),
]
