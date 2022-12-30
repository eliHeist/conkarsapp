from django.db import models

from images.models import Image

# Create your models here.
class Project(models.Model):
   name = models.CharField(max_length=50)
   thumbnail = models.ImageField()
   active = models.BooleanField(default=True)
   short_description = models.TextField()
   long_description = models.TextField()
   images = models.ManyToManyField(Image)
   cartegories = models.ManyToManyField("Category")

   def __str__(self):
      return self.name

   class Meta:
      verbose_name = 'Project'
      verbose_name_plural = 'Projects'


class Category(models.Model):
   name = models.CharField(max_length=50)

   def __str__(self):
      return self.name

   class Meta:
      verbose_name = 'Category'
      verbose_name_plural = 'Categories'