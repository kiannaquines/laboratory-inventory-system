from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import TemplateView
from inventory.models import *
from inventory.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User as DefaultUser

class DashboardPage(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['total_equipments'] = Equipment.objects.count()
        context['total_chemicals'] = Chemicals.objects.count()
        context['total_users'] = DefaultUser.objects.count()
        context['latest_equipments'] = Equipment.objects.all()[:10]
        return self.render_to_response(context)



