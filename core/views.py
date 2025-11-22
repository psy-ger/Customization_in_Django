"""Views for the `core` app (class-based and simple function view)."""

from typing import Any

from django.http import HttpRequest, HttpResponse
from django.views.generic import DetailView, CreateView, ListView
from django.urls import reverse_lazy
from django.shortcuts import render

from .models import CustomModel
from .forms import CustomModelForm, RegistrationForm


class CustomModelDetailView(DetailView):
    """Detail view for a single `CustomModel` instance."""

    model = CustomModel
    template_name = 'core/custommodel_detail.html'


class CustomModelListView(ListView):
    """List view for `CustomModel` objects."""

    model = CustomModel
    template_name = 'core/custommodel_list.html'
    paginate_by = 10


class CustomModelCreateView(CreateView):
    """Create view for `CustomModel` using `CustomModelForm`."""

    model = CustomModel
    form_class = CustomModelForm
    template_name = 'core/custommodel_form.html'
    success_url = reverse_lazy('core:custommodel_list')


class RegisterView(CreateView):
    """User registration view using `RegistrationForm`."""

    form_class = RegistrationForm
    template_name = 'core/register.html'
    success_url = reverse_lazy('login')


def home(request: HttpRequest) -> HttpResponse:
    """Render a small home page.

    This simple view demonstrates usage of the context processor and
    template tags included with the project.
    """
    return render(request, 'core/home.html')
