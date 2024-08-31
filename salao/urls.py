from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.salao_list, name='salao_list'),
  path('<int:salao_id>/', views.salao_detail, name='salao_detail'),
  path('add/', views.salao_add, name='salao_add'),
  path('edit/<int:salao_id>/', views.salao_edit, name='salao_edit'),
  path('delete/<int:salao_id>/', views.salao_delete, name='salao_delete'),
  path('<int:salao_id>/produtos/', include('produto.urls'))
]