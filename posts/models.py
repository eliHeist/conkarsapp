from django.db import models

from images.models import Image
from projects.models import Project

# Create your models here.

class Article(models.Model):
   title = models.CharField(max_length=100)
   thumbnail = models.ImageField(blank=True, null=True)
   date_posted = models.DateTimeField(auto_now_add=True)
   summary = models.TextField(null=True, blank=True)
   body = models.TextField(null=True)
   pictures = models.ManyToManyField(Image, null=True, blank=True)
   project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)

   def __str__(self):
      return self.title