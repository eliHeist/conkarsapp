from django.shortcuts import render
from django.views.generic import ListView, DetailView

from projects.models import Project

# Create your views here.
class ProjectListView(ListView):
   template_name = 'projects/project-list.html'
   queryset = Project.objects.filter(active=True)
   context_object_name = 'projects'


class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/project-detail.html"
