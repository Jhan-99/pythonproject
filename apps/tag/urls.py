from django.urls import path, re_path
from .views import Home, crearTag, ListarTag, editarTag, eliminarTag
urlpatterns = [
    path('',Home, name = 'Home'),
    path('crear/',crearTag, name = 'crear'),
    path('listar/',ListarTag, name = 'listar'),
    path('editar/<int:id>',editarTag, name = 'editar'),
    path('eliminar/<int:id>',eliminarTag, name = 'eliminar'),
]