# Generated by Django 2.1.dev20180423170307 on 2018-05-01 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GestionDeNoticias', '0002_noticia_autor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidoalta',
            name='Periodista',
        ),
    ]
