from django.views.generic import DetailView, CreateView, ListView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import CustomModel
from .forms import CustomModelForm, RegistrationForm


class CustomModelDetailView(DetailView):
    model = CustomModel
    template_name = 'core/custommodel_detail.html'


class CustomModelListView(ListView):
    model = CustomModel
    template_name = 'core/custommodel_list.html'
    paginate_by = 10


class CustomModelCreateView(CreateView):
    model = CustomModel
    form_class = CustomModelForm
    template_name = 'core/custommodel_form.html'
    success_url = reverse_lazy('core:custommodel_list')


class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'core/register.html'
    success_url = reverse_lazy('login')


def home(request):
    return render(request, 'core/home.html')
