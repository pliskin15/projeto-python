from django.urls import path
from .views import IndexView, SobreView, ModeloView
from . import views
urlpatterns = [
    path('', IndexView.as_view(), name='inicio'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('questoes/', views.mat, name='questoes'),
    path('login/', views.login, name ='login'),
    path('formulario/', views.index, name ='form'),
    path('modelo/', ModeloView.as_view(), name ='modelo'),
    path('resultado/', views.lista, name='resultado')
]
    