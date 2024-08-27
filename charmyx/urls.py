from django.contrib import admin
from django.urls import include, path
import salao

urlpatterns = [
  path('admin/', admin.site.urls),
  path('saloes/', include(salao.urls)),
]
