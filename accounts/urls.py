from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views

app_name = "accounts"
urlpatterns = [
    path("", views.dashboard, name='dashboard'),
    path("Entrar/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path("Sair/", auth_views.LogoutView.as_view(next_page="core:home"), name='logout'),
    path("Cadastre-se/", views.register, name='register'),
    path("Editar/", views.edit, name='edit'),
    path("Editar-senha/", views.edit_password, name='edit_password'),
    path("Nova-senha/", views.password_reset, name='password_reset'),
    path("Confirmar-nova-senha/<key>/", views.password_reset_confirm, name='password_reset_confirm'),
]