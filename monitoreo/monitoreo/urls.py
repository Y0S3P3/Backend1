
from django.contrib import admin
from django.urls import path
from dispositivos.views import inicio
from dispositivos.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio),
]

# accounts/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm

urlpatterns = [
    path("login/", LoginView.as_view(
        template_name="accounts/login.html",
        authentication_form=LoginForm,
        redirect_authenticated_user=True
    ), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]

urlpatterns = [
        path("", dashboard, name="dashboard"),
]

