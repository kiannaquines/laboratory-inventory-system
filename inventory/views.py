from typing import Any
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from inventory.models import Chemicals,ChemicalCategory
from inventory.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User as DefaultUser
from django.db.models import Q
from django.contrib import messages
from weasyprint import HTML
from django.template.loader import render_to_string
from datetime import datetime

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

def is_empty(value):
    return value is None or value == "" or value.strip() == ""

def generate_report(request):
    context = {}

    if request.method == 'POST':

        expiration_from = request.POST.get('expiration_date_from')
        expiration_to = request.POST.get('expiration_date_to')

        if is_empty(expiration_from) != is_empty(expiration_to) or is_empty(expiration_to) != is_empty(expiration_from):
            messages.error(request,'Both date filters must be provided. Please enter both a start and end date.',extra_tags="error")
            return HttpResponseRedirect('/chemicals/report')
        
        elif is_empty(expiration_from) and is_empty(expiration_to):
            generate_report_form = FilterReportForm(request.POST)
            if generate_report_form.is_valid():
                chemical_category = generate_report_form.cleaned_data['chemical_category']
                chemical_units = generate_report_form.cleaned_data['chemical_units']

                chemicals = Chemicals.objects.filter(
                    Q(chemical_category=chemical_category) &
                    Q(chemical_units=chemical_units)
                )

                if chemicals.count() == 0:
                    messages.error(request,'No chemicals found matching the selected criteria.',extra_tags="error")
                    return HttpResponseRedirect('/chemicals/report')
                
                context['chemicals'] = chemicals
                context['date'] = f'Date: {datetime.now().strftime("%Y-%m-%d")}'
                template_string = render_to_string('pdfs/template_pdf.html',context)
                html = HTML(string=template_string, base_url=request.build_absolute_uri())
                pdf_file = html.write_pdf()
                response = HttpResponse(pdf_file, content_type='application/pdf')
                response['Content-Disposition'] = 'inline; filename="output.pdf"'
                return response
        else:
            generate_report_form = FilterReportForm(request.POST)
            if generate_report_form.is_valid():
                chemical_category = generate_report_form.cleaned_data['chemical_category']
                chemical_units = generate_report_form.cleaned_data['chemical_units']
                date_from = generate_report_form.cleaned_data['expiration_date_from']
                date_to = generate_report_form.cleaned_data['expiration_date_to']

                chemicals = Chemicals.objects.filter(
                    Q(chemical_category=chemical_category) &
                    Q(chemical_units=chemical_units) &
                    Q(expiration_date__range=(date_from, date_to))
                )

                if chemicals.count() == 0:
                    messages.error(request,'No chemicals found matching the selected criteria.',extra_tags="error")
                    return HttpResponseRedirect('/chemicals/report')
                
                context['chemicals'] = chemicals
                context['date'] = f'Date: {date_from} - {date_to}'
                template_string = render_to_string('pdfs/template_pdf.html',context)
                html = HTML(string=template_string, base_url=request.build_absolute_uri())
                pdf_file = html.write_pdf()
                response = HttpResponse(pdf_file, content_type='application/pdf')
                response['Content-Disposition'] = 'inline; filename="output.pdf"'
                return response
            
    else:
        context['chemicals'] = Chemicals.objects.all()
        context['header_title'] = 'Chemical Report List'
        context['button_name'] = 'Generate Report'
        context['form_filter'] = generate_report_form
        return render(request, 'chemical_report.html',context)
    



