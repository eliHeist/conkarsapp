from django.urls import path

from services.views import ServicesView

app_name = 'services'

urlpatterns = [
   path('', ServicesView, name='main-page')
]