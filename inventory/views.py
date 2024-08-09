from typing import Any
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import TemplateView
from inventory.models import Chemicals,ChemicalCategory
from inventory.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User as DefaultUser

class DashboardPage(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['total_chemical_category'] = ChemicalCategory.objects.count()
        context['total_chemicals'] = Chemicals.objects.count()
        context['total_users'] = DefaultUser.objects.count()
        context['latest_chemicals'] = Chemicals.objects.all()[:10]
        context['available_chemicals'] = Chemicals.objects.filter(availability=True).count()
        context['header_title'] = '10 Latest Chemicals'
        return self.render_to_response(context)



