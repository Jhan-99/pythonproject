import json
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import datetime, time, random
from .forms import TagForm
from .models import Tag , Datos_Tag
from django.db.models import Count, Q
from django.views.generic import TemplateView, ListView, UpdateView

def Home(request):
    return render(request,'tag/index.html')

def Grapline(request):
    dataset = Datos_Tag.objects.filter(nombre='Wet Bulb Temperature') \
        .values('nombre','valor','fecha_hora') \
        .order_by('nombre').all()[:15000] \
        
    dataset1 = Datos_Tag.objects.filter(nombre='Humidity') \
        .values('nombre','valor','fecha_hora') \
        .order_by('nombre').all()[:15000] \
 
    dataset2 = Datos_Tag.objects.filter(nombre='Air Temperature') \
        .values('nombre','valor','fecha_hora') \
        .order_by('nombre').all()[:15000] \

    return render(request, 'tag/grapline.html', {'dataset': dataset, 'dataset1': dataset1, 'dataset2': dataset2})

def Graplinebar(request):
    dataset = Datos_Tag.objects.filter(nombre='Wet Bulb Temperature') \
        .values('nombre','valor','fecha_hora') \
        .order_by('nombre').all()[:10] \
        
    dataset1 = Datos_Tag.objects.filter(nombre='Humidity') \
        .values('nombre','valor','fecha_hora') \
        .order_by('nombre').all()[:10] \
 
    dataset2 = Datos_Tag.objects.filter(nombre='Air Temperature') \
        .values('nombre','valor','fecha_hora') \
        .order_by('nombre').all()[:10] \

    return render(request, 'tag/graplinebar.html', {'dataset': dataset, 'dataset1': dataset1, 'dataset2': dataset2})


def Graptemplate(request):
    dataset = Datos_Tag.objects.filter(nombre='Wet Bulb Temperature') \
        .values('nombre','valor','fecha_hora') \
        .order_by('nombre').all()[:50] \
        
    dataset1 = Datos_Tag.objects.filter(nombre='Humidity') \
        .values('nombre','valor','fecha_hora') \
        .order_by('nombre').all()[:50] \
 
    dataset2 = Datos_Tag.objects.filter(nombre='Air Temperature') \
        .values('nombre','valor','fecha_hora') \
        .order_by('nombre').all()[:50] \

    return render(request, 'tag/graptemplate.html', {'dataset': dataset, 'dataset1': dataset1, 'dataset2': dataset2})

def ListarDatosVariable(request):
    datos_variable = Tag.objects.all()
    #mandar la consulta al template y renderizar los datos traídos
    return render(request, 'tag/datos_variable.html', {'datos_variable': datos_variable})


def Graficar(request, id):
    if request.method == 'POST':
        variables = request.POST.getlist('variables[]') 
        vars = request.POST.getlist('variables[]') 
        for var, vars in zip(variables, vars):
            print("las vars " + str(var)) 
            dataset = Tag.objects \
                .values('nombre_var','cfg_max_raw','cfg_min_eu') \
                .order_by('nombre_var').filter(nombre_var__in = var)[:6]
        return render(request, 'tag/graf_line_dt.html', {'dataset': dataset})

def Graf_Datos_Tag(request, varname):
    if request.method == 'POST':
        variables = ["Humidity", "Air Temperature", "Rain Intensity", "Wet Bulb Temperature"]
        va = request.POST.getlist('variables[]')
        from_d =  request.POST.get('from_date')
        from_date = datetime.datetime.strptime(from_d, '%Y-%m-%d')
        to_d =  request.POST.get('to_date')
        to_date = datetime.datetime.strptime(to_d, '%Y-%m-%d')
        numrows =  int(request.POST.get('filas_add'))
        #from_date = "2015-04-25"
        #to_date = "2015-06-22"
        dt = request.POST.get('var_added')
        forma_obtencion = request.POST.get('val_obtencion')
        data_vars = ''
        
        if forma_obtencion == "date_range":
            data_vars = Datos_Tag.objects.filter(fecha_hora__range=(from_date, to_date), nombre = dt)[:numrows]
        else:
            absolute_range = request.POST.get('val_time_obtencion')
            if absolute_range == "one_month_ago":
                ahora = datetime.datetime.utcnow()
                hoy = ahora.strftime('%Y-%m-%d')
                print("Hoy es : " +str(hoy))
                anterior = ahora - datetime.timedelta(days=30)
                n_anterior = anterior.strftime('%Y-%m-%d')
                print("Hace un mes: " + str(n_anterior))
                data_vars = Datos_Tag.objects.filter(fecha_hora__range=(n_anterior, hoy), nombre = dt)[:numrows]
            elif absolute_range == "two_months_ago":
                ahora = datetime.datetime.utcnow()
                hoy = ahora.strftime('%Y-%m-%d')
                print("Hoy es : " +str(hoy))
                anterior = ahora - datetime.timedelta(days=60)
                n_anterior = anterior.strftime('%Y-%m-%d')
                print("Hace 2 meses: " + str(n_anterior))
                data_vars = Datos_Tag.objects.filter(fecha_hora__range=(n_anterior, hoy), nombre = dt)[:numrows]
            elif absolute_range == "one_year_ago":    
                ahora = datetime.datetime.utcnow()
                hoy = ahora.strftime('%Y-%m-%d')
                print("Hoy es : " +str(hoy))
                anterior = ahora - datetime.timedelta(days=365)
                n_anterior = anterior.strftime('%Y-%m-%d')
                print("Hace 1 año: " + str(n_anterior))
                data_vars = Datos_Tag.objects.filter(fecha_hora__range=(n_anterior, hoy), nombre = dt)[:numrows]
        
        
        #for ns in Tag.objects.raw('SELECT * FROM tag t INNER JOIN datos_tag d ON  t.nombre_var = d.nombre'):
            #print("Nombres " + str(ns.nombre_var))
 
        color_list = ["#f44336","#880e4f","#689f38","#42a5f5","#004d40","#ffc107","#795548","#212121","#cddc39","#ffa000","#827717","#b2dfdb","#ffcdd2"]
        color_var = random.choice(color_list)
        datos_variable = Tag.objects.all()
        return render(request, 'tag/datos_variable.html', {'data_vars': data_vars,  'dt':dt, 'datos_variable':datos_variable , 'from_date':from_date, 'to_date':to_date, 'color_var':color_var})    
        
    else:
        nombre_var = varname    
        dataset_once = Datos_Tag.objects.filter(nombre = nombre_var).order_by('-id_dt')[:30][::-1]
        return render(request, 'tag/graficar.html', {'dataset_once': dataset_once, 'nombre_var':nombre_var})
    
def DetallesVariable(request):
    if request.method == 'POST':
        nombre_var = request.POST.getlist("vars[]")
        nombre = request.POST.getlist("vars[]")
        s_dates = request.POST.get('s_dates')
        tipo_graf = request.POST.get('tipo_graf')
        print("Fechas " + str(s_dates))
        array = []
        for a, b in zip(nombre_var, nombre):
            array +=  [a]
        for x in array:
            print("x" + str(x))
        
        if tipo_graf == "line":
            return render(request, 'tag/graf_line_dt.html', {'array':array, 's_dates': s_dates})
        else:
            return render(request, 'tag/graf_bar_dt.html', {'array':array, 's_dates': s_dates})
    
def ListarTag(request):
    tag = Tag.objects.all()
    #mandar la consulta al template y renderizar los datos traídos
    return render(request, 'tag/listar.html', {'tag': tag})
  

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
        return redirect('tag:listar')
    return render(request, 'tag/crear.html') 
 
    
def actualizarTag(request, id):
    if request.method == 'POST':
        id  = request.POST.get('id')
        nombre_var  = request.POST.get('nombre_var')
        cfg_tipo  = request.POST.get('cfg_tipo')
        cfg_hab_var  = request.POST.get('cfg_hab_var')
        cfg_hab_sim  = request.POST.get('cfg_hab_sim')
        cfg_cmd_sim  = request.POST.get('cfg_cmd_sim')
        cfg_min_raw  = request.POST.get('cfg_min_raw')
        cfg_max_raw  = request.POST.get('cfg_max_raw')
        cfg_min_eu  = request.POST.get('cfg_min_eu')
        cfg_max_eu  = request.POST.get('cfg_max_eu')
        cfg_unidad  = request.POST.get('cfg_unidad')
        cfg_sp_alarma_ll  = request.POST.get('cfg_sp_alarma_ll')
        cfg_sp_alarma_l  = request.POST.get('cfg_sp_alarma_l')
        cfg_sp_alarma_hh  = request.POST.get('cfg_sp_alarma_hh')
        cfg_sp_alarma_h  = request.POST.get('cfg_sp_alarma_h')
        cfg_hab_alarma_ll  = request.POST.get('cfg_hab_alarma_ll')
        cfg_hab_alarma_l  = request.POST.get('cfg_hab_alarma_l')
        cfg_hab_alarma_h  = request.POST.get('cfg_hab_alarma_h')
        cfg_hab_alarma_hh  = request.POST.get('cfg_hab_alarma_hh')
        cfg_mth_puerto  = request.POST.get('cfg_mth_puerto')
        cfg_ip  = request.POST.get('cfg_ip')
        #parametrización comunicación
        cfg_rtu_baud  = request.POST.get('cfg_rtu_baud')
        cfg_rtu_puerto  = request.POST.get('cfg_rtu_puerto')
        #-------------------#
        cfg_esclavo  = request.POST.get('cfg_esclavo')
        cfg_reg  = request.POST.get('cfg_reg')
        cfg_formato  = request.POST.get('cfg_formato')
        sts_data_raw  = request.POST.get('sts_data_raw')
        sts_data_eu  = request.POST.get('sts_data_eu')
        sts_falla_io  = request.POST.get('sts_falla_io')
        sts_alarma_hh  = request.POST.get('sts_alarma_hh')
        sts_alarma_h  = request.POST.get('sts_alarma_h')
        sts_alarma_l  = request.POST.get('sts_alarma_l')
        sts_alarma_ll  = request.POST.get('sts_alarma_ll')
        
        Tag.objects.filter(pk=id).update(nombre_var= nombre_var, cfg_tipo = cfg_tipo, cfg_hab_var=cfg_hab_var, cfg_hab_sim= cfg_hab_sim, cfg_cmd_sim = cfg_cmd_sim, cfg_min_raw = cfg_min_raw, cfg_max_raw = cfg_max_raw, cfg_min_eu = cfg_min_eu, cfg_max_eu = cfg_max_eu, cfg_unidad = cfg_unidad, cfg_sp_alarma_ll = cfg_sp_alarma_ll, cfg_sp_alarma_l = cfg_sp_alarma_l, cfg_sp_alarma_hh=cfg_sp_alarma_hh, cfg_sp_alarma_h = cfg_sp_alarma_h, cfg_hab_alarma_ll= cfg_hab_alarma_ll, cfg_hab_alarma_l=cfg_hab_alarma_l,cfg_hab_alarma_h=cfg_hab_alarma_h, cfg_hab_alarma_hh= cfg_hab_alarma_hh, cfg_mth_puerto=cfg_mth_puerto, cfg_ip=cfg_ip, cfg_rtu_baud =cfg_rtu_baud , cfg_rtu_puerto = cfg_rtu_puerto, cfg_esclavo=cfg_esclavo, cfg_reg=cfg_reg, cfg_formato=cfg_formato, sts_data_raw= sts_data_raw, sts_data_eu=sts_data_eu, sts_falla_io=sts_falla_io, sts_alarma_hh= sts_alarma_hh, sts_alarma_h= sts_alarma_h, sts_alarma_l=sts_alarma_l, sts_alarma_ll=sts_alarma_ll)
        return redirect('tag:listar')
    else:
         dataset = Tag.objects.filter(id = id)    
    return render(request, 'tag/editar.html', {'dataset': dataset})


def infoTag (request, id):
    tag_info = Tag.objects.filter(id = id)
    if request.method == 'POST':
        id  = request.POST.get('id')
    return render(request, 'tag/tagInfo.html', {'tag_info': tag_info})
        
        
def eliminarTag(request, id):
    tags = Tag.objects.get(id = id)
    if request.method == 'POST':
        tags.delete()
        #fabricas.save()
        return redirect('tag:listar')
    return render(request, 'tag/eliminar.html', {'tags': tags})