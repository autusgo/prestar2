from django.urls import path
from . import views

urlpatterns = [

    path('', views.sobre_conami, name='sobre_conami'),
    path('simulador/', views.sim_index, name='sim_index'),
    path('simulador/list/', views.simulaciones_list, name='simulaciones_list'),
    path('simulador/propias/', views.simulaciones_propias,
         name='simulaciones_propias'),
    path('simulador/<int:pk>/', views.simulacion_detail, name='simulacion_detail'),
    path('simulador/new/', views.simulacion_new, name='simulacion_new'),
    path('simulador/<int:pk>/edit/', views.simulacion_edit, name='simulacion_edit'),
    path('simulador/<pk>/remove/', views.simulacion_remove,
         name='simulacion_remove'),
    path("prueba/", views.jsondata, name="jsondata"),

    path('sobre_conami/', views.sobre_conami, name='sobre_conami'),
    path('sobre_creditos/', views.sobre_creditos, name='sobre_creditos'),

    path('solicitudes/new/', views.solicitud_new, name='solicitud_new'),
    path('solicitudes/<int:pk>/edit/',
         views.solicitud_edit, name='solicitud_edit'),
    path('solicitudes/<int:pk>/', views.solicitud_detail, name='solicitud_detail'),
    path('solicitudes/list/', views.solicitud_list, name='solicitud_list'),
    path('solicitudes/propias/', views.solicitudes_propias,
         name='solicitudes_propias'),

    path('configuracion/', views.configuracion, name='configuracion'),

    path('configuracion/smvm/new/', views.smvm_new, name='smvm_new'),
    path('configuracion/smvm/<int:pk>/', views.smvm_detail, name='smvm_detail'),
    path('configuracion/smvm/<int:pk>/edit/',
         views.smvm_edit, name='smvm_edit'),

    path('configuracion/tasa/new/', views.tasa_new, name='tasa_new'),
    path('configuracion/tasa/<int:pk>/', views.tasa_detail, name='tasa_detail'),
    path('configuracion/tasa/<int:pk>/edit/',
         views.tasa_edit, name='tasa_edit'),


    # path('login/', views.LoginView.as_view(), name='login'),
]
