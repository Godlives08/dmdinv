# Generated by Django 3.1.7 on 2021-02-27 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210227_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo_itemurl',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]