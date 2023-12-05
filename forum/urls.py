from django.urls import path
from forum import views

app_name = "forum"
urlpatterns = [
    path('', views.ForumView.as_view(), name='index'),
    path('tag/<tag>', views.ForumView.as_view(), name='index_tagged'),
    path('<slug>', views.ThreadView.as_view(), name='thread'),
    path('respostas/<pk>/correta/', views.ReplyCorrectView.as_view(), name='reply_correct'),
    path('respostas/<pk>/incorreta/', views.ReplyCorrectView.as_view(correct=False), name='reply_incorrect'),
]