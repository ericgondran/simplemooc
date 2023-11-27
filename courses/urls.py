from django.urls import path
from courses import views

app_name = "courses"
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug>/', views.details, name='details'),
    path('<slug>/inscricao/', views.enrollment, name='enrollment'),
    path('<slug>/cancelar-inscricao/', views.undo_enrollment, name='undo_enrollment'),
    path('<slug>/anuncios/', views.announcements, name='announcements'),
    path('<slug>/anuncios/<pk>', views.show_announcement, name='show_announcement'),
    path('<slug>/aulas/', views.lessons, name='lessons'),
    path('<slug>/aulas/<pk>', views.lesson, name='lesson'),
    path('<slug>/materiais/<pk>', views.material, name='material'),
]