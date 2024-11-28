import os
from typing import Any
from core.settings import MEDIA_ROOT
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, View
from inventory.models import Chemicals, ChemicalCategory
from inventory.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User as DefaultUser
from django.db.models import Q
from django.contrib import messages
from weasyprint import HTML
from django.template.loader import render_to_string
from datetime import datetime
from django.utils.decorators import method_decorator
from inventory.decorator import *


class RequestChemicalView(LoginRequiredMixin, View):
    template_name = "chemical_request.html"

    def get(self, request):
        context = {}
        context["requests"] = RequestChemical.objects.all()
        return render(request, self.template_name, context)


class RequestChemicalGenerateReportView(LoginRequiredMixin, View):
    template_name = "chemical_requested_report.html"

    def get(self, request):
        context = {}
        context["form"] = FilterRequestedReportForm()
        context["button_name"] = "Generate"
        context["requests"] = RequestChemical.objects.all()
        return render(request, self.template_name, context)


@method_decorator(not_loggedin, name="dispatch")
class DashboardPage(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["total_chemical_category"] = ChemicalCategory.objects.count()
        context["total_chemicals"] = Chemicals.objects.count()
        context["total_users"] = DefaultUser.objects.count()
        context["latest_chemicals"] = Chemicals.objects.all()[:10]
        context["available_chemicals"] = Chemicals.objects.filter(
            availability=True
        ).count()
        context["header_title"] = "10 Latest Chemicals"
        return self.render_to_response(context)


@not_loggedin
def generate_report(request):
    context = {}

    if request.method == "POST":
        generate_report_form = FilterReportForm(request.POST)

        if generate_report_form.is_valid():
            chemical_category = generate_report_form.cleaned_data["chemical_category"]
            chemical_units = generate_report_form.cleaned_data["chemical_units"]

            chemicals = Chemicals.objects.filter(
                Q(chemical_category=chemical_category)
                & Q(chemical_units=chemical_units)
                & Q(availability=True)
            ).all()

            if chemicals.count() == 0:
                messages.error(
                    request,
                    "No chemicals found matching the selected criteria.",
                    extra_tags="error",
                )
                return HttpResponseRedirect("/chemicals/report")

            context["chemicals"] = chemicals
            context["date"] = f'{datetime.now().strftime("%B %d, %Y")}'
            template_string = render_to_string("pdfs/template_pdf.html", context)
            html = HTML(string=template_string, base_url=request.build_absolute_uri())
            pdf_file = html.write_pdf()

            output_filename = os.path.join(MEDIA_ROOT, "output.pdf")
            with open(output_filename, "wb") as f:
                f.write(pdf_file)

            context["chemicals"] = Chemicals.objects.all()
            context["header_title"] = "Chemical Report List"
            context["button_name"] = "View PDF"
            context["pdf_link"] = "/media/output.pdf"
            context["form_filter"] = generate_report_form
            return render(request, "chemical_report.html", context)

    else:
        context["chemicals"] = Chemicals.objects.all()
        context["header_title"] = "Chemical Report List"
        context["button_name"] = "Generate"
        context["form_filter"] = generate_report_form
        return render(request, "chemical_report.html", context)


@not_loggedin
def generate_report_requested(request):
    context = {}
    if request.method == "POST":
        generate_report_form = FilterRequestedReportForm(request.POST)

        range_date_start = request.POST.get("expiration_date_from")
        range_date_end = request.POST.get("expiration_date_to")

        if generate_report_form.is_valid():
            chemical_category = generate_report_form.cleaned_data["chemical_category"]
            chemical_units = generate_report_form.cleaned_data["chemical_units"]

            chemicals = RequestChemical.objects.filter(
                Q(chemical_requested__chemical_category=chemical_category)
                & Q(chemical_requested__chemical_units=chemical_units)
            )

            if range_date_start and range_date_end:
                chemicals = chemicals.filter(
                    Q(date_requested__range=(range_date_start, range_date_end))
                )

            if chemicals.count() == 0:
                messages.error(
                    request,
                    "No request found matching the selected criteria.",
                    extra_tags="error",
                )
                return HttpResponseRedirect("chemicals/request/report")

            context["chemicals"] = chemicals
            context["date"] = f'{datetime.now().strftime("%B %d, %Y")}'
            template_string = render_to_string(
                "pdfs/requested_template_pdf.html", context
            )
            html = HTML(string=template_string, base_url=request.build_absolute_uri())
            pdf_file = html.write_pdf()

            output_filename = os.path.join(MEDIA_ROOT, "output.pdf")
            with open(output_filename, "wb") as f:
                f.write(pdf_file)

            context["chemicals"] = Chemicals.objects.all()
            context["header_title"] = "Chemical Report List"
            context["button_name"] = "View PDF"
            context["pdf_link"] = "/media/output.pdf"
            context["form"] = generate_report_form
            return render(request, "chemical_requested_report.html", context)

    else:
        context["chemicals"] = Chemicals.objects.all()
        context["header_title"] = "Chemical Request Report List"
        context["button_name"] = "Generate"
        context["form"] = generate_report_form
        return render(request, "chemical_requested_report.html", context)
