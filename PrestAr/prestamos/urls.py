from django.urls import path
from . import views

urlpatterns = [
    path('', views.simulaciones_list, name='simulaciones_list'),
]
