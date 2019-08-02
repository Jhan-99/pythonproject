# Generated by Django 2.2.1 on 2019-07-29 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_var', models.CharField(max_length=100, verbose_name='nombre_var')),
                ('cfg_hab_var', models.CharField(max_length=10, verbose_name='cfg_hab_var')),
                ('cfg_tipo', models.CharField(max_length=10, verbose_name='cfg_tipo')),
                ('cfg_hab_sim', models.CharField(max_length=10, verbose_name='cfg_hab_sim')),
                ('cfg_cmd_sim', models.CharField(max_length=10, verbose_name='cfg_cmd_sim')),
                ('cfg_min_raw', models.CharField(max_length=10, verbose_name='cfg_min_raw')),
                ('cfg_max_raw', models.CharField(max_length=10, verbose_name='cfg_max_raw')),
                ('cfg_min_eu', models.CharField(max_length=10, verbose_name='cfg_min_eu')),
                ('cfg_max_eu', models.CharField(max_length=10, verbose_name='cfg_max_eu')),
                ('cfg_unidad', models.CharField(max_length=10, verbose_name='cfg_unidad')),
                ('cfg_sp_alarma_ll', models.CharField(max_length=10, verbose_name='cfg_sp_alarma_ll')),
                ('cfg_sp_alarma_l', models.CharField(max_length=10, verbose_name='cfg_sp_alarma_l')),
                ('cfg_sp_alarma_h', models.CharField(max_length=10, verbose_name='cfg_sp_alarma_h')),
                ('cfg_sp_alarma_hh', models.CharField(max_length=10, verbose_name='cfg_sp_alarma_hh')),
                ('cfg_hab_alarma_ll', models.CharField(max_length=10, verbose_name='cfg_hab_alarma_ll')),
                ('cfg_hab_alarma_l', models.CharField(max_length=10, verbose_name='cfg_hab_alarma_l')),
                ('cfg_hab_alarma_h', models.CharField(max_length=10, verbose_name='cfg_hab_alarma_h')),
                ('cfg_hab_alarma_hh', models.CharField(max_length=10, verbose_name='cfg_hab_alarma_hh')),
                ('cfg_ip', models.CharField(max_length=10, verbose_name='cfg_ip')),
                ('cfg_reg', models.CharField(max_length=10, verbose_name='cfg_reg')),
                ('cfg_esclavo', models.CharField(max_length=10, verbose_name='cfg_esclavo')),
                ('cfg_formato', models.CharField(max_length=10, verbose_name='cfg_formato')),
                ('cfg_rtu_baud', models.CharField(max_length=10, verbose_name='cfg_rtu_baud')),
                ('cfg_rtu_puerto', models.CharField(max_length=10, verbose_name='cfg_rtu_puerto')),
                ('cfg_mth_puerto', models.CharField(max_length=10, verbose_name='cfg_mth_puerto')),
                ('sts_data_raw', models.CharField(max_length=10, verbose_name='sts_data_raw')),
                ('sts_data_eu', models.CharField(max_length=10, verbose_name='sts_data_eu')),
                ('sts_falla_io', models.CharField(max_length=10, verbose_name='sts_falla_io')),
                ('sts_alarma_ll', models.CharField(max_length=10, verbose_name='sts_alarma_ll')),
                ('sts_alarma_l', models.CharField(max_length=10, verbose_name='sts_alarma_l')),
                ('sts_alarma_h', models.CharField(max_length=10, verbose_name='sts_alarma_h')),
                ('sts_alarma_hh', models.CharField(max_length=10, verbose_name='sts_alarma_hh')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'ordering': ['id'],
            },
        ),
    ]