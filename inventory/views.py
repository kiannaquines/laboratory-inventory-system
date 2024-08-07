from django.views.generic import TemplateView, UpdateView, DeleteView, DetailView, CreateView, ListView
from django.contrib.auth.views import LoginView, LogoutView

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
 