from django import forms
from .models import Tag
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['nombre_var', 'cfg_hab_var',  'cfg_tipo', 'cfg_hab_sim',  'cfg_cmd_sim',  'cfg_min_raw', 'cfg_max_raw', 'cfg_min_eu', 'cfg_max_eu', 'cfg_unidad',  'cfg_sp_alarma_ll', 'cfg_sp_alarma_l',  'cfg_sp_alarma_h', 'cfg_sp_alarma_hh',  'cfg_hab_alarma_ll',  'cfg_hab_alarma_l',  'cfg_hab_alarma_h', 'cfg_hab_alarma_hh',  'cfg_ip',  'cfg_reg', 'cfg_esclavo',  'cfg_formato',  'cfg_rtu_baud',  'cfg_rtu_puerto',  'cfg_mth_puerto',  'sts_data_raw',  'sts_data_eu',  'sts_falla_io', 'sts_alarma_ll',  'sts_alarma_l', 'sts_alarma_h', 'sts_alarma_hh', 'estado']
        labels = {
             'nombre_var': 'Nombre variable',
         }