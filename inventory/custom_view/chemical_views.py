from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from inventory.models import *
from django.urls import reverse_lazy
from inventory.forms import *
from typing import Any
from django.contrib import messages
from django.utils.decorators import method_decorator
from inventory.decorator import *

@method_decorator(not_loggedin, name="dispatch")
class ChemicalListView(ListView):
    template_name = 'chemical.html'
    model = Chemicals
    context_object_name = 'chemicals'
@method_decorator(not_loggedin, name="dispatch")    
class ChemicalCategoryView(ListView):
    template_name = 'chemical_category.html'
    model = ChemicalCategory
    context_object_name = 'chemical_categories' 

@method_decorator(not_loggedin, name="dispatch")
class ChemicalReportView(ListView):
    template_name = 'chemical_report.html'
    model = Chemicals
    context_object_name = 'chemicals'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['header_title'] = 'Chemical Report List'
        context['form_filter'] = FilterReportForm()
        context['button_name'] = 'Generate PDF'
        return context
    
@method_decorator(not_loggedin, name="dispatch")
class AddChemicalCategoryView(CreateView):
    template_name = 'forms/add_form.html'
    model = ChemicalCategory
    success_url = reverse_lazy('inventory:chemical_category')
    form_class = ChemicalCategoryForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().form_valid(form)
        messages.success(self.request, 'Yahooo! Chemical Category added successfully.',extra_tags='success')
        return response
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['header_title'] = 'Add Chemical Category'
        context['button_name'] = 'Save Chemical Category'
        context['back_button'] = 'Back to Chemical Category List'
        return context
    
@method_decorator(not_loggedin, name="dispatch")
class AddChemicalView(CreateView):
    template_name = 'forms/add_form.html'
    model = Chemicals
    success_url = reverse_lazy('inventory:chemicals')
    form_class = ChemicalForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().form_valid(form)
        messages.success(self.request, 'Yahooo! Chemical added successfully.',extra_tags='success')
        return response
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['header_title'] = 'Add Chemical'
        context['button_name'] = 'Save Chemical'
        context['back_button'] = 'Back to Chemical List'
        return context

@method_decorator(not_loggedin, name="dispatch")
class UpdateChemicalView(UpdateView):
    model = Chemicals
    form_class = ChemicalForm
    template_name = 'forms/update_form.html'
    success_url = reverse_lazy('inventory:chemicals')
    pk_url_kwarg = 'chemical_id'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['header_title'] = 'Update Chemical'
        context['button_name'] = 'Update Chemical'
        context['back_button'] = 'Back to Chemical List'
        return context
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().form_valid(form)
        messages.success(self.request, 'Yahooo! Chemical updated successfully.',extra_tags='success')
        return response

@method_decorator(not_loggedin, name="dispatch")
class DeleteChemicalView(DeleteView):
    model = Chemicals
    template_name = 'forms/delete_form.html'
    pk_url_kwarg = 'chemical_id'
    success_url = reverse_lazy('inventory:chemicals')


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['header_title'] = 'Delete Chemical'
        context['button_name'] = 'Delete Chemical'
        context['back_button'] = 'Back to Chemical List'
        return context
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().form_valid(form)
        messages.success(self.request, 'Chemical removed successfully.',extra_tags='success')
        return response

@method_decorator(not_loggedin, name="dispatch")
class UpdateChemicalCategoryView(UpdateView):
    model = ChemicalCategory
    form_class = ChemicalCategoryForm
    template_name = 'forms/update_form.html'
    success_url = reverse_lazy('inventory:chemical_category')
    pk_url_kwarg = 'chemical_category_id'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['header_title'] = 'Update Chemical Category'
        context['button_name'] = 'Update Chemical Category'
        context['back_button'] = 'Back to Chemical Categories'
        return context
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().form_valid(form)
        messages.success(self.request, 'Chemical Category updated successfully.',extra_tags='success')
        return response

@method_decorator(not_loggedin, name="dispatch")
class DeleteChemicalCategoryView(DeleteView):
    model = ChemicalCategory
    template_name = 'forms/delete_form.html'
    pk_url_kwarg = 'chemical_category_id'
    success_url = reverse_lazy('inventory:chemical_category')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['header_title'] = 'Delete Chemical Category'
        context['button_name'] = 'Delete Chemical Category'
        context['back_button'] = 'Back to Chemical Categories'
        return context
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().form_valid(form)
        messages.success(self.request, 'Chemical Category removed successfully.',extra_tags='success')
        return response