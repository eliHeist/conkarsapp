from django.db import models

# Create your models here.
class Person(models.Model):
   name = models.CharField(max_length=50)
   title = models.CharField(max_length=15, default='Mr')
   position = models.CharField(max_length=50)
   image = models.ImageField()

   def full_name(self):
      return f'{self.title}. {self.name}'

   def __str__(self):
      return self.title