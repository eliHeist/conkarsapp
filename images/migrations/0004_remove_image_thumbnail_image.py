# Generated by Django 4.1.3 on 2023-01-26 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_image_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='thumbnail_image',
        ),
    ]