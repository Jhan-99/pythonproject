from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from .views import Home, crearTag, ListarTag, actualizarTag,infoTag, Graficar, Graf_Datos_Tag, ListarDatosVariable,eliminarTag, DetallesVariable, Grapline,Graplinebar,Graptemplate
 


urlpatterns = [
    path('',Home, name = 'Home'),
    path('crear/',login_required (crearTag), name = 'crear'),
    path('listar/',login_required (ListarTag), name = 'listar'),
    path('editar/<int:id>',login_required(actualizarTag), name = 'editar'),
    path('info/<int:id>',login_required(infoTag), name = 'info'),
    path('chart/<int:id>',login_required(Graficar), name = 'chart'),
    path('chart/dv/<str:varname>',login_required(Graf_Datos_Tag), name = 'dv'),
    path('traer/',DetallesVariable, name = 'traer'),
    path('vars/',login_required(ListarDatosVariable), name = 'vars'),
    path('eliminar/<int:id>',login_required(eliminarTag), name = 'eliminar'),
    path('grapline/', Grapline, name = 'Grapline'),
    path('graplinebar/', Graplinebar, name = 'Graplinebar'),
    path('graptemplate/', Graptemplate, name = 'Graptemplate'),
    
]