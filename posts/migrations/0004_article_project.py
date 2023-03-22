# Generated by Django 4.1.3 on 2023-03-18 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_rename_cartegories_project_categories'),
        ('posts', '0003_alter_article_body_alter_article_pictures_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.project'),
        ),
    ]