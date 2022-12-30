from django.db import models

# Create your models here.
class Image(models.Model):
   image = models.ImageField(upload_to=None)
   thumbnail_image = models.ImageField(blank=True, null=True)
   title = models.CharField(blank=True, null=True, max_length=50)
   description = models.TextField(blank=True, null=True)

   def thumbnail(self):
      return self.thumbnail_image.url or self.image.url
   
   def image(self):
      return self.image.url
   
   def __str__(self):
      return self.title or "image"

   class Meta:
      verbose_name = 'Image'
      verbose_name_plural = 'Images'
