from django.db import models

from projects.models import Project

# Create your models here.
class FeaturedProject(models.Model):
   project = models.ForeignKey(Project, on_delete=models.CASCADE)

   class Meta:
      verbose_name = 'Featured Project'
      verbose_name_plural = 'Featured Projects'

   def __str__(self):
      return self.project.name
