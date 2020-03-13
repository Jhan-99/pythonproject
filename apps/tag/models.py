from django.db import models

# Create your models here.
class Tag(models.Model):
    id =                models.AutoField('id',primary_key = True)
    nombre_var =        models.CharField('nombre_var', max_length = 100, null = False)
    cfg_hab_var =       models.IntegerField('cfg_hab_var', null = True)
    cfg_tipo =          models.CharField('cfg_tipo', max_length = 10, null = True)
    cfg_hab_sim =       models.IntegerField('cfg_hab_sim', null = True)
    cfg_cmd_sim =       models.FloatField('cfg_cmd_sim', null = True)
    cfg_min_raw =       models.FloatField('cfg_min_raw', max_length = 10, null = True)
    cfg_max_raw =       models.FloatField('cfg_max_raw', max_length = 10, null = True)
    cfg_min_eu =        models.FloatField('cfg_min_eu', max_length = 10, null = True)
    cfg_max_eu =        models.FloatField('cfg_max_eu', null = True)
    cfg_unidad =        models.CharField('cfg_unidad', max_length = 10, null = True)
    cfg_sp_alarma_ll =  models.FloatField('cfg_sp_alarma_ll', null = True)
    cfg_sp_alarma_l =   models.FloatField('cfg_sp_alarma_l', null = True)
    cfg_sp_alarma_h =   models.IntegerField('cfg_sp_alarma_h', null = True)
    cfg_sp_alarma_hh =  models.IntegerField('cfg_sp_alarma_hh', null = True)
    cfg_hab_alarma_ll = models.FloatField('cfg_hab_alarma_ll', null = True)
    cfg_hab_alarma_l =  models.FloatField('cfg_hab_alarma_l', null = True)
    cfg_hab_alarma_h =  models.IntegerField('cfg_hab_alarma_h',  null = True)
    cfg_hab_alarma_hh = models.IntegerField('cfg_hab_alarma_hh', null = True)
    cfg_ip =            models.CharField('cfg_ip', max_length = 30, null = True)
    cfg_reg =           models.IntegerField('cfg_reg',  null = True)
    cfg_esclavo =       models.IntegerField('cfg_esclavo',  null = True)
    cfg_formato =       models.CharField('cfg_formato', max_length = 10, null = True)
    cfg_rtu_baud =      models.IntegerField('cfg_rtu_baud', null = True)
    cfg_rtu_puerto =    models.CharField('cfg_rtu_puerto' ,max_length = 10, null = True)
    cfg_mth_puerto =    models.IntegerField('cfg_mth_puerto', null = True)
    sts_data_raw =      models.FloatField('sts_data_raw', null = True)
    sts_data_eu =       models.FloatField('sts_data_eu', null = True)
    sts_falla_io =      models.FloatField('sts_falla_io', null = True)
    sts_alarma_ll =     models.IntegerField('sts_alarma_ll', null = True)
    sts_alarma_l =      models.IntegerField('sts_alarma_l', null = True)
    sts_alarma_h =      models.IntegerField('sts_alarma_h', null = True)
    sts_alarma_hh =     models.IntegerField('sts_alarma_hh',null = True)
    estado = models.BooleanField('Estado', default = True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        db_table = 'tag'
        ordering = ['id']
    
    def __str__(self):
        return '{}'.format(self.id)
    
class Datos_Tag(models.Model):
    id_dt = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre', max_length = 100, null = True)
    valor = models.IntegerField('Valor', null = True)
    fecha_hora = models.DateField('Fecha hora', null = True)    
    class Meta:
        verbose_name = 'Datos_Variable'
        db_table = 'datos_tag'
        verbose_name_plural = 'Datos_Variables'
        ordering = ['id_dt']
    
    def __str__(self):
        return '{}'.format(self.id_dt)
    
 