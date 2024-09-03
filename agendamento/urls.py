from django.urls import path
from . import views

urlpatterns = [
    path("", views.agendamento_list, name="agendamento_list"),
    path("add/", views.agendamento_add, name="agendamento_add"),
    path("edit/<int:id>/", views.agendamento_edit, name="agendamento_edit"),
    path("delete/<int:id>/", views.agendamento_delete, name="agendamento_delete"),
    path("<int:id>/", views.agendamento_detail, name="agendamento_detail"),
    path('confirm/<int:id>/', views.agendamento_confirm, name='agendamento_confirm'),
    path('complete/<int:id>/', views.agendamento_complete, name='agendamento_complete'),
    
] 