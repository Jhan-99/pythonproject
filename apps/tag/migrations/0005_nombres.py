# Generated by Django 2.2.1 on 2020-03-01 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0004_auto_20200227_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nombres',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, null=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'nombre_variable',
                'verbose_name_plural': 'nombre_variables',
                'ordering': ['id'],
            },
        ),
    ]
