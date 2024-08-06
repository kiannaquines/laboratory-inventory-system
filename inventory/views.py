from django.views.generic import TemplateView, UpdateView, DeleteView, DetailView, CreateView, ListView

class DashboardPage(TemplateView):
    template_name = 'dashboard.html'

class EquipmentList(TemplateView):
    template_name = 'equipment.html'

class UserList(TemplateView):
    template_name = 'user.html'

class ChemicalList(TemplateView):
    template_name = 'chemical.html'
 