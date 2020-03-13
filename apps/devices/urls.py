from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from .views import Home, crearTag, ListarTag, editarTag, eliminarTag
urlpatterns = [
   # path('',Home, name = 'Home'),
    path('device/add/', devices.device_add, name='device_add'),
    path('device/list/', devices.device_list, name='device_list'),
    path('device/edit/<str:id>/', devices.device_edit, name='device_edit'),
    path('device/delete/<str:id>/', devices.device_delete, name='device_delete'),
]