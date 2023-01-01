from django.shortcuts import render

# Create your views here.
def AboutView(request):
   context = {}
   template_name = 'about/about-page.html'
   return render(request, template_name, context)