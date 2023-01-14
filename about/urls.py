from django.urls import path

from about.views import AboutView


app_name = 'about'

urlpatterns = [
   path('', AboutView, name='main-page')
]