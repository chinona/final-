# Generated by Django 5.0.6 on 2024-08-16 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfinal', '0005_obras_obra_alter_artistas_obras'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artistas',
            name='obras',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='obra',
        ),
        migrations.AddField(
            model_name='artistas',
            name='imagenes',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/'),
        ),
        migrations.AddField(
            model_name='obras',
            name='imagenes',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/'),
        ),
    ]
