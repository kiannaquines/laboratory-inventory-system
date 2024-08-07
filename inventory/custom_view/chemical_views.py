from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, ListView
from inventory.models import *
from django.urls import reverse_lazy
from inventory.forms import *
from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin

class ChemicalList(LoginRequiredMixin, ListView):
    template_name = 'chemical.html'
    model = Chemicals
    context_object_name = 'chemicals'
    
class ChemicalCategory(LoginRequiredMixin, ListView):
    template_name = 'chemical_category.html'
    model = ChemicalCategory
    context_object_name = 'chemical_categories'    


class ChemicalReport(LoginRequiredMixin, TemplateView):
    template_name = 'chemical_report.html'


class AddChemicalCategoryView(LoginRequiredMixin, CreateView):
    template_name = 'forms/add_form.html'
    model = ChemicalCategory
    success_url = reverse_lazy('inventory:chemical_category')
    form_class = ChemicalCategoryForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().form_valid(form)
        return response
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['header_title'] = 'Add Chemical Category'
        context['button_name'] = 'Save Chemical Category'
        return context
    
class AddChemicalView(LoginRequiredMixin, CreateView):
    template_name = 'forms/add_form.html'
    model = Chemicals
    success_url = reverse_lazy('inventory:chemicals')
    form_class = ChemicalForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().form_valid(form)
        return response
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['header_title'] = 'Add Chemical'
        context['button_name'] = 'Save Chemical'
        return context
 