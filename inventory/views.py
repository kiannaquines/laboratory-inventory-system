from django.views.generic import TemplateView
from inventory.models import *
from inventory.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin

class DashboardPage(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'



