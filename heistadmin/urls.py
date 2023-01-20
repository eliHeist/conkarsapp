from django.urls import path

from heistadmin.views import defaultView, updateView, listView

app_name = "heistadmin"

urlpatterns = [
   path('', defaultView, name='dashboard'),
   path('<str:slug>/', listView, name='list'),
   path('<str:slug>/create/', updateView, name='create'),
   path('<str:slug>/<int:pk>/update/', updateView, name='update'),
   path('<str:slug>/<int:pk>/delete/', updateView, name='delete'),
]