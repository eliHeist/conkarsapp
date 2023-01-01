from django.shortcuts import render

# Create your views here.
def ServicesView(request):
   context = {}
   template_name = 'services/services-page.html'
   return render(request, template_name, context)