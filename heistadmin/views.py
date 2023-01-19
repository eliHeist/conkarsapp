from django.shortcuts import render

from projects.models import Category, Project

# Create your views here.
registered_models = {Project,Category}
# create a base context containing slugs for registered models
base_context = {}
base_models = []
for model in registered_models:
   # insert at the end of the file to maintain order of registered_models
   base_models.insert(-1, model.__name__)
# add models list to context
base_context["models"] = base_models

def registerModels():
   pass

def defaultView(request):
   template_name = 'heistadmin/dashboard.djhtml'
   context = base_context
   for model in registered_models:
      # add model to context
      context[f"{model.__name__}"] = model
      # insert at the end of the file to maintain order of registered_models

   return render(request, template_name, context)


def listView(request, slug):
   template_name = 'heistadmin/list_base.html'
   context = base_context
   

   return render(request, template_name, context)
