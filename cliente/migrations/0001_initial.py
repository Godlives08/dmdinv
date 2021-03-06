# Generated by Django 3.1.7 on 2021-03-02 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('direccion', '0006_barrio_sector'),
        ('sucursal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=155)),
                ('apellido', models.CharField(max_length=155)),
                ('cedopass', models.CharField(max_length=25, unique=True)),
                ('codigocliente', models.CharField(max_length=45, unique=True)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('I', 'Indefinido')], default='I', max_length=1)),
                ('fechanacimiento', models.DateField()),
                ('direccion', models.TextField(default='', max_length=500)),
                ('cadelaimg', models.FileField(max_length=500, upload_to='')),
                ('email', models.CharField(max_length=155)),
                ('email2', models.CharField(max_length=155)),
                ('telefono', models.CharField(max_length=50)),
                ('telefono2', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('barrio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='direccion.barrio')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='direccion.pais')),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='direccion.provincia')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='direccion.sector')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sucursal.sucursal')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['nombre'],
                'permissions': (('permiso_vercliente', 'Permiso a ver Cliente'), ('permiso_crearcliente', 'Permiso a Crear Cliente'), ('permiso_actualizarcliente', 'Permiso a Actualizar Cliente'), ('permiso_eliminarcliente', 'Permiso a Eliminar Cliente')),
            },
        ),
    ]
