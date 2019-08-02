from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from .forms import TagForm
from .models import Tag
from django.views.generic import TemplateView, ListView, UpdateView
def Home(request):
    return render(request,'tag/index.html')

def ListarTag(request):
    tag = Tag.objects.all()
    #mandar la consulta al template y renderizar los datos traídos
    return render(request, 'tag/listar.html', {'tag': tag})

    return render(request, 'tag/listar.html')

def crearTag(request):
    if request.method == 'POST':
        tag_form = TagForm(request.POST)
        nombre_var  = request.POST.get('nombre_var')
        cfg_tipo  = request.POST.get('cfg_tipo')
        cfg_hab_var  = request.POST.get('cfg_hab_var')
        cfg_hab_sim  = request.POST.get('cfg_hab_sim')
        cfg_cmd_sim  = request.POST.get('cfg_cmd_sim')
        cfg_min_raw = request.POST.get('cfg_min_raw')
        cfg_max_raw = request.POST.get('cfg_max_raw')
        cfg_min_eu = request.POST.get('cfg_min_eu')
        cfg_max_eu = request.POST.get('cfg_max_eu')
        cfg_unidad = request.POST.get('cfg_unidad')
        cfg_sp_alarma_ll = request.POST.get('cfg_sp_alarma_ll')
        cfg_sp_alarma_l = request.POST.get('cfg_sp_alarma_l')
        cfg_sp_alarma_hh = request.POST.get('cfg_sp_alarma_hh')
        cfg_sp_alarma_h = request.POST.get('cfg_sp_alarma_h')
        cfg_hab_alarma_ll = request.POST.get('cfg_hab_alarma_ll')
        cfg_hab_alarma_l = request.POST.get('cfg_hab_alarma_l')
        cfg_hab_alarma_h = request.POST.get('cfg_hab_alarma_h')
        cfg_hab_alarma_hh = request.POST.get('cfg_hab_alarma_hh')
        cfg_ip = request.POST.get('cfg_ip')
        cfg_mth_puerto = request.POST.get('cfg_mth_puerto')
        cfg_rtu_baud = request.POST.get('cfg_rtu_baud')
        cfg_rtu_puerto = request.POST.get('cfg_rtu_puerto')
        cfg_esclavo = request.POST.get('cfg_esclavo')
        cfg_reg = request.POST.get('cfg_reg')
        cfg_formato = request.POST.get('cfg_formato')
        sts_data_raw = request.POST.get('sts_data_raw')
        sts_data_eu = request.POST.get('sts_data_eu')
        sts_falla_io = request.POST.get('sts_falla_io')
        sts_alarma_hh = request.POST.get('sts_alarma_hh')
        sts_alarma_h = request.POST.get('sts_alarma_h')
        sts_alarma_l = request.POST.get('sts_alarma_l')
        sts_alarma_ll = request.POST.get('sts_alarma_ll')

        tag = Tag(
        nombre_var = nombre_var, 
        cfg_tipo = cfg_tipo, 
        cfg_hab_var = cfg_hab_var, 
        cfg_hab_sim = cfg_hab_sim, 
        cfg_cmd_sim = cfg_cmd_sim, 
        cfg_min_raw = cfg_min_raw , 
        cfg_max_raw = cfg_max_raw , 
        cfg_min_eu = cfg_min_eu , 
        cfg_max_eu = cfg_max_eu , 
        cfg_unidad = cfg_unidad ,
        cfg_sp_alarma_ll = cfg_sp_alarma_ll,
        cfg_sp_alarma_l =  cfg_sp_alarma_l, 
        cfg_sp_alarma_hh =  cfg_sp_alarma_hh,  
        cfg_sp_alarma_h =  cfg_sp_alarma_h, 
        cfg_hab_alarma_ll =  cfg_hab_alarma_ll, 
        cfg_hab_alarma_l =  cfg_hab_alarma_l, 
        cfg_hab_alarma_h =  cfg_hab_alarma_h,
        cfg_hab_alarma_hh =  cfg_hab_alarma_hh,
        cfg_ip = cfg_ip,
        cfg_mth_puerto = cfg_mth_puerto,
        cfg_rtu_baud = cfg_rtu_baud,
        cfg_rtu_puerto = cfg_rtu_puerto,
        cfg_esclavo = cfg_esclavo,
        cfg_reg = cfg_reg,
        cfg_formato     = cfg_formato,
        sts_data_raw = sts_data_raw,
        sts_data_eu = sts_data_eu,
        sts_falla_io = sts_falla_io,
        sts_alarma_hh = sts_alarma_hh,
        sts_alarma_h = sts_alarma_h,
        sts_alarma_l = sts_alarma_l,
        sts_alarma_ll = sts_alarma_ll,
            
        )
        tag.save()
        return redirect('index')
    return render(request, 'tag/crear.html') 
 
def editarTag(request, id):
    tag_form =  None
    error = None
    try:
        tags = Tag.objects.get(id = id)
        if request.method == 'GET':
            tag_form = TagForm(instance = tags) 
        else:
            tag_form = TagForm(request.POST, instance = tags)
            if tag_form.is_valid():
                tag_form.save()
            return redirect('tag:listar')
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'tag/editar.html', {'tag_form': tag_form, 'error': error})      

def eliminarTag(request, id):
    tags = Tag.objects.get(id = id)
    if request.method == 'POST':
        tags.delete()
        #fabricas.save()
        return redirect('tag:listar')
    return render(request, 'tag/eliminar.html', {'tags': tags})