from django.urls import path

from heistadmin.views import defaultView

app_name = "heistadmin"

urlpatterns = [
   path('', defaultView, name='default')
]