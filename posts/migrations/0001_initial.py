# Generated by Django 4.1.3 on 2023-03-18 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('images', '0004_remove_image_thumbnail_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('thumbnail', models.ImageField(upload_to='')),
                ('summary', models.TextField()),
                ('body', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('pictures', models.ManyToManyField(to='images.image')),
            ],
        ),
    ]