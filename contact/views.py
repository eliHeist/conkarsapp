from django.shortcuts import render

# Create your views here.
def ContactView(request):
   context = {}
   template_name = 'contact/contact-page.html'
   return render(request, template_name, context)