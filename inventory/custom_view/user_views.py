from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import CreateView, ListView
from inventory.models import *
from django.urls import reverse_lazy
from inventory.forms import *
from typing import Any
from django.contrib.auth.models import User as DefaultUser
from django.contrib.auth.mixins import LoginRequiredMixin

class UserList(LoginRequiredMixin, ListView):
    template_name = 'user.html'
    model = DefaultUser
    context_object_name = 'users'

class AddUserView(LoginRequiredMixin, CreateView):
    template_name = 'forms/add_form.html'
    model = DefaultUser
    form_class = UserForm
    success_url = reverse_lazy('inventory:users')

    def forms_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().forms_valid(form)
        return response
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['header_title'] = 'Add User'
        context['button_name'] = 'Save User'
        return context