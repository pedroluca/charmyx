from django.urls import path
from . import views

urlpatterns = [
  # Add your URL patterns here
  # Example: path('home/', views.home, name='home'),
  path('', views.salao_list, name='salao_list'),
  path('<int:id>/', views.salao_detail, name='salao_detail'),
  path('add/', views.salao_add, name='salao_add'),
  path('edit/<int:id>/', views.salao_edit, name='salao_edit'),
  path('delete/<int:id>/', views.salao_delete, name='salao_delete'),
]