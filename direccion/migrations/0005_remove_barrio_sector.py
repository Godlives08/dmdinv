# Generated by Django 3.1.7 on 2021-03-01 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0004_auto_20210228_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barrio',
            name='sector',
        ),
    ]
