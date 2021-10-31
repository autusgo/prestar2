from django.urls import path
from . import views

urlpatterns = [
    path('', views.simulaciones_list, name='simulaciones_list'),
    path('simulador/<int:pk>/', views.simulacion_detail, name='simulacion_detail'),
    path('simulador/new/', views.simulacion_new, name='simulacion_new'),
    path('simulador/<int:pk>/edit/', views.simulacion_edit, name='simulacion_edit'),
]
