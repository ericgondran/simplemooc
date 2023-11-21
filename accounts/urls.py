from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views

app_name = "accounts"
urlpatterns = [
    path("Entrar/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path("Sair/", auth_views.LogoutView.as_view(next_page="core:home"), name='logout'),
    path("Cadastre-se/", views.register, name='register'),
]