from django.db import models

# Create your models here.
class Tag(models.Model):
    id =                models.AutoField(primary_key = True)
    nombre_var =        models.CharField('nombre_var', max_length = 100, null = False)
    cfg_hab_var =       models.CharField('cfg_hab_var', max_length = 10, null = True)
    cfg_tipo =          models.CharField('cfg_tipo', max_length = 10, null = True)
    cfg_hab_sim =       models.CharField('cfg_hab_sim', max_length = 10, null = True)
    cfg_cmd_sim =       models.CharField('cfg_cmd_sim', max_length = 10, null = True)
    cfg_min_raw =       models.CharField('cfg_min_raw', max_length = 10, null = True)
    cfg_max_raw =       models.CharField('cfg_max_raw', max_length = 10, null = True)
    cfg_min_eu =        models.CharField('cfg_min_eu', max_length = 10, null = True)
    cfg_max_eu =        models.CharField('cfg_max_eu', max_length = 10, null = True)
    cfg_unidad =        models.CharField('cfg_unidad', max_length = 10, null = True)
    cfg_sp_alarma_ll =  models.CharField('cfg_sp_alarma_ll', max_length = 10, null = True)
    cfg_sp_alarma_l =   models.CharField('cfg_sp_alarma_l', max_length = 10, null = True)
    cfg_sp_alarma_h =   models.CharField('cfg_sp_alarma_h', max_length = 10, null = True)
    cfg_sp_alarma_hh =  models.CharField('cfg_sp_alarma_hh', max_length = 10, null = True)
    cfg_hab_alarma_ll = models.CharField('cfg_hab_alarma_ll', max_length = 10, null = True)
    cfg_hab_alarma_l =  models.CharField('cfg_hab_alarma_l', max_length = 10, null = True)
    cfg_hab_alarma_h =  models.CharField('cfg_hab_alarma_h', max_length = 10, null = True)
    cfg_hab_alarma_hh = models.CharField('cfg_hab_alarma_hh', max_length = 10, null = True)
    cfg_ip =            models.CharField('cfg_ip', max_length = 10, null = True)
    cfg_reg =           models.CharField('cfg_reg', max_length = 10, null = True)
    cfg_esclavo =       models.CharField('cfg_esclavo', max_length = 10, null = True)
    cfg_formato =       models.CharField('cfg_formato', max_length = 10, null = True)
    cfg_rtu_baud =      models.CharField('cfg_rtu_baud', max_length = 10, null = True)
    cfg_rtu_puerto =    models.CharField('cfg_rtu_puerto', max_length = 10, null = True)
    cfg_mth_puerto =    models.CharField('cfg_mth_puerto', max_length = 10, null = True)
    sts_data_raw =      models.CharField('sts_data_raw', max_length = 10, null = True)
    sts_data_eu =       models.CharField('sts_data_eu', max_length = 10, null = True)
    sts_falla_io =      models.CharField('sts_falla_io', max_length = 10, null = True)
    sts_alarma_ll =     models.CharField('sts_alarma_ll', max_length = 10, null = True)
    sts_alarma_l =      models.CharField('sts_alarma_l', max_length = 10, null = True)
    sts_alarma_h =      models.CharField('sts_alarma_h', max_length = 10, null = True)
    sts_alarma_hh =     models.CharField('sts_alarma_hh', max_length = 10, null = True)
    estado = models.BooleanField('Estado', default = True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['id']
    
    def __str__(self):
        return '{}'.format(self.id)