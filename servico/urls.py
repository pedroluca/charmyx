from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.servico_list, name='servico_list'),
    path('add/', views.servico_add, name='servico_add'),
    path('edit/<int:id>/', views.servico_edit, name='servico_edit'),
    path('delete/<int:id>/', views.servico_delete, name='servico_delete'),
    path('<int:id>/', views.servico_detail, name='servico_detail'),
]
