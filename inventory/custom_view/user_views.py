from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, ListView
from inventory.models import *
from django.urls import reverse_lazy
from inventory.forms import *
from typing import Any
from django.contrib.auth.models import User as DefaultUser

class UserList(ListView):
    template_name = 'user.html'
    model = DefaultUser