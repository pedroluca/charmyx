from django.urls import path, include
from . import views

urlpatterns = [
  path('<int:produto_id>/', views.produto_detail, name='produto_detail'),
  path('add/', views.produto_add, name='produto_add'),
  path('edit/<int:produto_id>/', views.produto_edit, name='produto_edit'),
  path('delete/<int:produto_id>/', views.produto_delete, name='produto_delete'),
]