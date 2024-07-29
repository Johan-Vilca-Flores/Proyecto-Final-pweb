from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Define la URL para la vista de índice
    # Puedes agregar más rutas aquí según sea necesario
]
