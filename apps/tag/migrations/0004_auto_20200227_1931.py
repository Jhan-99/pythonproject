# Generated by Django 2.2.1 on 2020-02-28 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0003_auto_20200227_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='cfg_rtu_puerto',
            field=models.CharField(max_length=10, null=True, verbose_name='cfg_rtu_puerto'),
        ),
    ]
