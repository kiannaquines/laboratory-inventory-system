from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView,CreateView
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User as DefaultUser
from inventory.forms import RegisterForm
class LoginPage(LoginView):
    template_name = 'registration/login.html'

class RegisterPage(CreateView):
    template_name = 'registration/register.html'
    model = DefaultUser
    form_class = RegisterForm

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')