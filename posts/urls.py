from django.urls import path

from posts.views import ArticleDetailView, ArticleListView

app_name = "posts"

urlpatterns = [
   path('', ArticleListView.as_view(), name='list'),
   path('<int:pk>/', ArticleDetailView.as_view(), name='detail')
]