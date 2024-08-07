from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from inventory.models import *
from django.urls import reverse_lazy
from inventory.forms import *
from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin

class ChemicalListView(LoginRequiredMixin, ListView):
    template_name = 'chemical.html'
    model = Chemicals
    context_object_name = 'chemicals'
    
class ChemicalCategoryView(LoginRequiredMixin, ListView):
    template_name = 'chemical_category.html'
    model = ChemicalCategory
    context_object_name = 'chemical_categories'    

class ChemicalReportView(LoginRequiredMixin, TemplateView):
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

class UpdateChemicalView(LoginRequiredMixin, UpdateView):
    model = Chemicals
    form_class = ChemicalForm
    template_name = 'forms/update_form.html'
    success_url = reverse_lazy('inventory:chemicals')
    pk_url_kwarg = 'chemical_id'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['header_title'] = 'Update Chemical'
        context['button_name'] = 'Update Chemical'
        return context
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().form_valid(form)
        return response

class DeleteChemicalView(LoginRequiredMixin, DeleteView):
    model = Chemicals
    template_name = 'forms/delete_form.html'
    pk_url_kwarg = 'chemical_id'
    success_url = reverse_lazy('inventory:chemicals')


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['header_title'] = 'Delete Chemical'
        context['button_name'] = 'Delete Chemical'
        context['back_button'] = 'Back'
        return context


class UpdateChemicalCategoryView(LoginRequiredMixin, UpdateView):
    model = ChemicalCategory
    form_class = ChemicalCategoryForm
    template_name = 'forms/update_form.html'
    success_url = reverse_lazy('inventory:chemical_category')
    pk_url_kwarg = 'chemical_category_id'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['header_title'] = 'Update Chemical Category'
        context['button_name'] = 'Update Chemical Category'
        return context
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().form_valid(form)
        return response
    
class DeleteChemicalCategoryView(LoginRequiredMixin, DeleteView):
    model = ChemicalCategory
    template_name = 'forms/delete_form.html'
    pk_url_kwarg = 'chemical_category_id'
    success_url = reverse_lazy('inventory:chemical_category')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['header_title'] = 'Delete Chemical Category'
        context['button_name'] = 'Delete Chemical Category'
        context['back_button'] = 'Back'
        return context
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().form_valid(form)
        return response