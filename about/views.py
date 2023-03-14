from django.shortcuts import render

from team.models import Person

# Create your views here.
def AboutView(request):
   people = Person.objects.all()
   context = {
      'people': people
   }
   template_name = 'about/about-page.html'
   return render(request, template_name, context)