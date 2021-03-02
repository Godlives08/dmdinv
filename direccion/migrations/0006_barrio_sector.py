# Generated by Django 3.1.7 on 2021-03-01 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0005_remove_barrio_sector'),
    ]

    operations = [
        migrations.AddField(
            model_name='barrio',
            name='sector',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='direccion.sector'),
            preserve_default=False,
        ),
    ]
