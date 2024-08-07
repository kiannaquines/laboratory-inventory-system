from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from inventory.models import *
from django.urls import reverse_lazy
from inventory.forms import *
from typing import Any

class LoginPage(LoginView):
    template_name = 'registration/login.html'

class RegisterPage(TemplateView):
    template_name = 'registration/register.html'

class LogoutPage(LogoutView):
    next_page_url = '/'

class DashboardPage(TemplateView):
    template_name = 'dashboard.html'

class EquipmentList(TemplateView):
    template_name = 'equipment.html'

class UserList(TemplateView):
    template_name = 'user.html'

class ChemicalList(TemplateView):
    template_name = 'chemical.html'

class ChemicalCategory(TemplateView):
    template_name = 'chemical_category.html'

class EquipmentCategory(TemplateView):
    template_name = 'equipment_category.html'

class EquipmentReport(TemplateView):
    template_name = 'equipment_report.html'

class ChemicalReport(TemplateView):
    template_name = 'chemical_report.html'

class AddEquipmentCategoryView(CreateView):
    template_name = 'forms/add_form.html'
    model = Equipment
    success_url = reverse_lazy('equipment_category')
    form_class = EquipmentForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().form_valid(form)
        return response
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['header_title'] = 'Add Equipment Category'
        context['button_name'] = 'Save Equipment Category'
        return context

class AddEquipmentView(CreateView):
    template_name = 'forms/add_form.html'
    model = Equipment
    success_url = reverse_lazy('equipments')
    form_class = EquipmentForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().form_valid(form)
        return response
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['header_title'] = 'Add Equipment'
        context['button_name'] = 'Save Equipment'
        return context
    
class AddChemicalCategoryView(CreateView):
    template_name = 'forms/add_form.html'
    model = ChemicalCategory
    success_url = reverse_lazy('chemical_category')
    form_class = ChemicalCategoryForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().form_valid(form)
        return response
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['header_title'] = 'Add Chemical Category'
        context['button_name'] = 'Save Chemical Category'
        return context
    
class AddChemicalView(CreateView):
    template_name = 'forms/add_form.html'
    model = Chemicals
    success_url = reverse_lazy('chemicals')
    form_class = ChemicalForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().form_valid(form)
        return response
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['header_title'] = 'Add Chemical'
        context['button_name'] = 'Save Chemical'
        return context
 