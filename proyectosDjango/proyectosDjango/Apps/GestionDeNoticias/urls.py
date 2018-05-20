from django.urls import path

from proyectosDjango.Apps.GestionDeNoticias.views import index

urlpatterns = [
    path(r'', index),
]
