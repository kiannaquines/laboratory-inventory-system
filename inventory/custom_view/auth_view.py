from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

class LoginPage(LoginView):
    template_name = 'registration/login.html'

class RegisterPage(TemplateView):
    template_name = 'registration/register.html'

class LogoutPage(LogoutView):
    next_page_url = '/'