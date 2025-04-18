from django.shortcuts import render

# added here down Autos assignment stuffs
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Auto, Make
from .forms import MakeForm  # Only needed if using a custom form for Make

# --------------------------
# Auto Views
# --------------------------

class AutoListView(LoginRequiredMixin, ListView):
    model = Auto
    template_name = 'autos/auto_list.html'
    context_object_name = 'auto_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add the count of makes so that you can conditionally show the "Add Auto" link
        context['make_count'] = Make.objects.count()
        return context

class AutoCreateView(LoginRequiredMixin, CreateView):
    model = Auto
    # List the fields you want to include in the form.
    fields = ['nickname', 'mileage', 'comments', 'make']
    template_name = 'autos/auto_form.html'
    success_url = reverse_lazy('autos:auto_list')

class AutoUpdateView(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = ['nickname', 'mileage', 'comments', 'make']
    template_name = 'autos/auto_form.html'
    success_url = reverse_lazy('autos:auto_list')

class AutoDeleteView(LoginRequiredMixin, DeleteView):
    model = Auto
    template_name = 'autos/auto_confirm_delete.html'
    success_url = reverse_lazy('autos:auto_list')

# --------------------------
# Make Views
# --------------------------

class MakeListView(LoginRequiredMixin, ListView):
    model = Make
    template_name = 'autos/make_list.html'
    context_object_name = 'make_list'

class MakeCreateView(LoginRequiredMixin, CreateView):
    model = Make
    # If using a custom form, uncomment the following line:
    # form_class = MakeForm
    fields = ['name']
    template_name = 'autos/make_form.html'
    success_url = reverse_lazy('autos:make_list')

class MakeUpdateView(LoginRequiredMixin, UpdateView):
    model = Make
    fields = ['name']
    template_name = 'autos/make_form.html'
    success_url = reverse_lazy('autos:make_list')

class MakeDeleteView(LoginRequiredMixin, DeleteView):
    model = Make
    template_name = 'autos/make_confirm_delete.html'
    success_url = reverse_lazy('autos:make_list')