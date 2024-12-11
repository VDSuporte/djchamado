from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cavalos
from django.urls import reverse_lazy
from django import forms


# Create your views here.


class CavalosCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('error')
    model = Cavalos
    fields = ['frota', 'placa', 'motorista', 'renavam', 'anomod', 'cor', 'chassi', 'crlv', 'marca', 'modelo', 'suspensao', 'tracao',
              'altura', 'capdiesel', 'pbt', 'tara', 'locado', 'macaricoele', 'bombadeasfalto', 'bombahidraulica', 'esperatforca',
              'placasolar', 'status', 'bloqueador', 'transportadora', 'notafiscal', 'velocidade', 'fimdegarantia',
              'dataentregatecnica']
    template_name = 'form-cavalos.html'
    success_url = reverse_lazy('cadastrar-cavalos')


class CavalosUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('error')
    model = Cavalos
    fields = ['frota', 'placa', 'motorista', 'renavam', 'anomod', 'cor', 'chassi', 'crlv', 'marca', 'modelo', 'suspensao', 'tracao',
              'altura', 'capdiesel', 'pbt', 'tara', 'locado', 'macaricoele', 'bombadeasfalto', 'bombahidraulica', 'esperatforca',
              'placasolar', 'status', 'bloqueador', 'transportadora', 'notafiscal', 'velocidade', 'fimdegarantia',
              'dataentregatecnica']
    template_name = 'form-cavalos.html'
    success_url = reverse_lazy('listar-cadastros-cavalos')


class CavalosDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('error')
    model = Cavalos
    template_name = 'form-cavalos-excluir.html'
    success_url = reverse_lazy('listar-cadastros-cavalos')


class CavalosList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('error')
    model = Cavalos
    template_name = 'lista/cavalos-listas.html'