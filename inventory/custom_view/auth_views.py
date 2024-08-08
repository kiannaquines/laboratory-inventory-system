from typing import Any
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User as DefaultUser
from inventory.forms import RegisterForm
from django.urls import reverse_lazy

class LoginPage(LoginView):
    template_name = 'registration/login.html'

class RegisterPage(CreateView):
    template_name = 'registration/register.html'
    model = DefaultUser
    form_class = RegisterForm
    success_url = reverse_lazy('inventory:login')


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
    
    def form_valid(self, form: Any) -> HttpResponseRedirect:
        response = super().form_valid(form)
        return response
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')