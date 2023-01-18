from django.shortcuts import render

# Create your views here.
def defaultView(request):
   template_name = 'heistadmin_base.html'
   context = {}
   return render(request, template_name, context)