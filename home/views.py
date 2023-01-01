from django.shortcuts import render

from home.models import FeaturedProject

def home(request):
    projects = FeaturedProject.objects.all()
    context = {
        "projects": projects
    }
    return render(request, 'home/index.html', context)
