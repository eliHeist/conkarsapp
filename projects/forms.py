from django.forms import ModelForm

from projects.models import Category, Project

class ProjectForm(ModelForm):
   class Meta:
      model = Project
      fields = '__all__'
   

class CartegoryForm(ModelForm):
   class Meta:
      model = Category
      fields = '__all__'