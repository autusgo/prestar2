from django.urls import path
from . import views

urlpatterns = [
    path('', views.sim_index, name='sim_index'),
    path('simulador/', views.sim_index, name='sim_index'),
    path('simulador/list/', views.simulaciones_list, name='simulaciones_list'),
    path('simulador/<int:pk>/', views.simulacion_detail, name='simulacion_detail'),
    path('simulador/new/', views.simulacion_new, name='simulacion_new'),
    path('simulador/<int:pk>/edit/', views.simulacion_edit, name='simulacion_edit'),
    # path('login/', views.LoginView.as_view(), name='login'),
]
