from django.db import models

# Create your models here.
class Project(models.Model):
   name = models.CharField(max_length=50)
   thumbnail = models.ImageField()
   active = models.BooleanField(default=True)
   short_description = models.CharField(max_length=200)
   long_description = models.TextField()
   # images = models.ManyToManyField()
