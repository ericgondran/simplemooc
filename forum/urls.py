from django.urls import path
from forum import views

app_name = "forum"
urlpatterns = [
    path('', views.ForumView.as_view(), name='index'),
    path('tag/<tag>', views.ForumView.as_view(), name='index_tagged'),
]