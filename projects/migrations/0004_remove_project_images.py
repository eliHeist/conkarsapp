# Generated by Django 4.1.3 on 2022-12-30 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_cartegories_alter_project_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='images',
        ),
    ]
