# Generated by Django 4.1.3 on 2022-12-30 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
        ('projects', '0002_alter_project_cartegories_alter_project_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='cartegories',
            field=models.ManyToManyField(blank=True, to='projects.category'),
        ),
        migrations.AlterField(
            model_name='project',
            name='images',
            field=models.ManyToManyField(blank=True, to='images.image'),
        ),
    ]
