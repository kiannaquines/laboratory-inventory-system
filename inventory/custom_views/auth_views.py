from django.contrib.auth.views import LogoutView, LoginView
from django.views.generic import TemplateView

class LoginPage(LoginView):
    template_name = 'auth/login.html'

class RegisterPage(TemplateView):
    template_name = 'auth/register.html'

class LogoutPage(LogoutView):
    next_page = '/'