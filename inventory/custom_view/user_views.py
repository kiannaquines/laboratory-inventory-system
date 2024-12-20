from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from inventory.models import *
from django.urls import reverse_lazy
from inventory.forms import *
from typing import Any
from django.contrib.auth.models import User as DefaultUser
from django.contrib import messages
from django.utils.decorators import method_decorator
from inventory.decorator import *

@method_decorator(not_loggedin, name="dispatch")
class UserList(ListView):
    template_name = 'user.html'
    model = DefaultUser
    context_object_name = 'users'

    def get_queryset(self):
        return DefaultUser.objects.filter(is_active=True)
    
class InactiveUserList(ListView):
    template_name = 'archive.html'
    model = DefaultUser
    context_object_name = 'users'

    def get_queryset(self):
        return DefaultUser.objects.filter(is_active=False)

@method_decorator(not_loggedin, name="dispatch")
class UpdateUserView(UpdateView):
    model = DefaultUser
    form_class = UserUpdateForm
    template_name = 'forms/update_form.html'
    success_url = reverse_lazy('inventory:users')
    pk_url_kwarg = 'user_id'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['header_title'] = 'Update User'
        context['button_name'] = 'Update User'
        context['back_button'] = 'Back to Users'
        return context
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().form_valid(form)
        messages.success(self.request, 'Yahooo! User updated successfully.',extra_tags='success')
        return response

@method_decorator(not_loggedin, name="dispatch")
class DeleteUserView(DeleteView):
    model = DefaultUser
    template_name = 'forms/delete_form.html'
    pk_url_kwarg = 'user_id'
    success_url = reverse_lazy('inventory:users')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['header_title'] = 'Delete User'
        context['button_name'] = 'Delete User'
        context['back_button'] = 'Back to Users'
        return context
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().form_valid(form)
        messages.success(self.request, 'User removed successfully.',extra_tags='success')
        return response

@method_decorator(not_loggedin, name="dispatch")
class AddUserView(CreateView):
    template_name = 'forms/add_form.html'
    model = DefaultUser
    form_class = UserForm
    success_url = reverse_lazy('inventory:users')

    def forms_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().forms_valid(form)
        messages.success(self.request, 'Yahooo! User added successfully.',extra_tags='success')
        return response
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['header_title'] = 'Add User'
        context['button_name'] = 'Save User'
        context['back_button'] = 'Back to Users'
        return context