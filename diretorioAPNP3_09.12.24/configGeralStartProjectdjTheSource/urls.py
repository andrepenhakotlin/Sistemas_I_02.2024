from django.urls import path
from . import views

urlpatterns = [
    path('artistas/', views.listar_artistas, name='listar_artistas'),
    path('artistas/criar/', views.criar_artista, name='criar_artista'),
    path('artistas/editar/<int:pk>/', views.editar_artista, name='editar_artista'),
    path('artistas/deletar/<int:pk>/', views.deletar_artista, name='deletar_artista'),
    path('artistas/<int:pk>/', views.ver_artista, name='ver_artista'),
]
