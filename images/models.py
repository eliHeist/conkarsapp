from django.db import models

from projects.models import Project

# Create your models here.
class Image(models.Model):
   title = models.CharField(blank=True, null=True, max_length=50)
   project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='photos', blank=True, null=True)
   image = models.ImageField()
   thumbnail_image = models.ImageField(blank=True, null=True)
   description = models.TextField(blank=True, null=True)

   def thumbnail(self):
      return self.thumbnail_image.url or self.image.url
   
   def imageurl(self):
      return self.image.url
   
   def __str__(self):
      return self.title or "image"

   class Meta:
      verbose_name = 'Image'
      verbose_name_plural = 'Images'
