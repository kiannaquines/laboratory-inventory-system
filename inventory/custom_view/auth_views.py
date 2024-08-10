from typing import Any
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView,TemplateView, View
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User as DefaultUser
from inventory.forms import RegisterForm
from django.urls import reverse_lazy
from django.contrib import messages
from inventory.decorator import *
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

@method_decorator(already_loggedin, name="dispatch")
class LoginPage(View):
    template_name = 'registration/login.html'
    form_class = AuthenticationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print(f'User {user} logged in.')

                if user.is_superuser or user.is_staff:
                    return redirect(reverse_lazy('inventory:dashboard'))
                
                return redirect(reverse_lazy('inventory:chemicals'))
            
        return render(request, self.template_name, {'form': form})

@method_decorator(already_loggedin, name="dispatch")
class RegisterPage(CreateView):
    template_name = 'registration/register.html'
    model = DefaultUser
    form_class = RegisterForm
    success_url = reverse_lazy('login')


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
    
    def form_valid(self, form: Any) -> HttpResponseRedirect:
        response = super().form_valid(form)
        messages.success(self.request, 'Yahooo! User registered successfully.',extra_tags='success')
        return response
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')