from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Clientes
from django.urls import reverse_lazy
from django import forms


# Create your views here.


class ClientesCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('error')
    model = Clientes
    fields = ['codigo', 'cliente', 'cliente_fantasia', 'observacao']
    template_name = 'clientes-form.html'
    success_url = reverse_lazy('menu')


class ClientesUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('error')
    model = Clientes
    fields = ['codigo', 'cliente', 'cliente_fantasia', 'observacao']
    template_name = 'clientes-form.html'
    success_url = reverse_lazy('menu')


class ClientesDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('error')
    model = Clientes
    template_name = 'clientes-form-excluir.html'
    success_url = reverse_lazy('menu')


class ClientesList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('error')
    model = Clientes
    template_name = 'lista/clientes-listas.html'
