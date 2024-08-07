from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, ListView
from inventory.models import *
from django.urls import reverse_lazy
from inventory.forms import *
from typing import Any


class EquipmentListView(ListView):
    template_name = 'equipment.html'
    model = Equipment
    context_object_name = 'chemicals'

class EquipmentCategoryView(ListView):
    template_name = 'equipment_category.html'
    model = EquipmentCategory
    context_object_name = 'equipment_categories'

class EquipmentReportView(TemplateView):
    template_name = 'equipment_report.html'

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