from django.shortcuts import render
from projects.forms import ProjectForm

from projects.models import Category, Project

# Create your views here.
class RegMod():
   def __init__(self, model, form_class, list_display=None):
      self.model = model
      self.list_display = list_display # should be set to a list of the fields to display
      self.form_class = form_class
      
registered_models = {
   RegMod(
      model=Project,
      form_class=ProjectForm,
      list_display={'name','short_description'}
   )
   # RegMod(model=Category)
}


slug_context = {}
base_models = []
for regmodel in registered_models:
   # insert at the end of the file to maintain order of registered_models
   base_models.insert(-1, regmodel.model.__name__)
   # add to slug_context
   slug_context[f"{regmodel.model.__name__}"] = regmodel.model
base_context = {"models": base_models}



def defaultView(request):
   template_name = 'heistadmin/dashboard.djhtml'
   context = base_context
   for regmodel in registered_models:
      # add model to context
      context[f"{regmodel.model.__name__}"] = regmodel.model
      # insert at the end of the file to maintain order of registered_models

   return render(request, template_name, context)


def listView(request, slug):
   template_name = 'heistadmin/list_base.djhtml'
   context = base_context
   for regmodel in registered_models:
      if regmodel.model.__name__ == slug:
         active_model = regmodel.model

   context["slug"] = active_model.__name__
   context["objects"] = active_model.objects.all()
   

   return render(request, template_name, context)


def updateView(request, slug, pk):
   template_name = 'heistadmin/update_base.djhtml'
   context = base_context
   for regmodel in registered_models:
      if regmodel.model.__name__ == slug:
         active_model = regmodel
   instance = active_model.model.objects.get(id=pk)

   if request.method == "POST":
      form = active_model.form_class(request.POST, instance=instance)
      if form.is_valid():
         form.save()
      instance = active_model.model.objects.get(id=pk)

   context["slug"] = active_model.model.__name__
   context["object"] = instance
   context["form"] = active_model.form_class(instance=instance)
   

   return render(request, template_name, context)