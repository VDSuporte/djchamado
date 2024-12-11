from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from .models import Carretas, Acessorios

# Create your views here.

def acessorios_carreta(request, carreta_id):
    carreta = get_object_or_404(Carretas, pk=carreta_id)
    acessorios = Acessorios.objects.filter(carreta=carreta)
    return render(request, 'acessorios.html', {'carreta': carreta, 'acessorios': acessorios})


class CarretasCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('error')
    model = Carretas
    fields = ['frota', 'placa', 'motorista', 'renavam', 'anomod', 'cor', 'chassi', 'crlv', 'marca', 'modelo', 'eixos', 'pneus',
              'suspensao', 'altura', 'pbt', 'toneladas', 'litros', 'tipo', 'tara', 'suspensor',
              'bolsa', 'mola', 'locada', 'transportadora', 'notafiscal', 'status']
    template_name = 'form-carretas.html'
    success_url = reverse_lazy('cadastrar-acessorios')


class CarretasUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('error')
    model = Carretas
    fields = ['frota', 'placa', 'motorista', 'renavam', 'anomod', 'cor', 'chassi', 'crlv', 'marca', 'modelo', 'eixos', 'pneus',
              'suspensao', 'altura', 'pbt', 'toneladas', 'litros', 'tipo', 'tara', 'suspensor',
              'bolsa', 'mola', 'locada', 'transportadora', 'notafiscal', 'status']
    template_name = 'form-carretas.html'
    success_url = reverse_lazy('listar-cadastros-carretas')


class CarretasDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('error')
    model = Carretas
    template_name = 'form-carretas-excluir.html'
    success_url = reverse_lazy('listar-cadastros-carretas')


class CarretasList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('error')
    model = Carretas
    template_name = 'lista/carretas-list.html'


class AcessoriosCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('error')
    model = Acessorios
    fields = ['placaacc', 'bottomclaro', 'bottomescuro', 'bottomtepar', 'api', 'descarga', 'dreno', 'graudbolt',
              'olhodegato', 'mangote', 'macarico']
    template_name = 'form-acessorios.html'
    success_url = reverse_lazy('listar-cadastros-acessorios')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carreta_id'] = self.kwargs.get('carreta_id') or self.request.GET.get('carreta_id') or self.request.POST.get('carreta_id')
        return context

    def form_valid(self, form):
        carreta_id = self.request.POST.get('carreta_id')
        if carreta_id:
            try:
                form.instance.carreta_id = int(carreta_id)
            except ValueError:
                form.add_error(None, "Invalid carreta_id value.")
                return self.form_invalid(form)
        else:
            form.add_error(None, "No carreta_id provided.")
            return self.form_invalid(form)
        return super().form_valid(form)

    def acessorios_carreta(request, carreta_id):
        carreta = get_object_or_404(Carretas, pk=carreta_id)
        acessorios = Acessorios.objects.filter(carreta=carreta)
        return render(request, 'acessorios.html',
                      {'carreta': carreta, 'acessorios': acessorios, 'carreta_id': carreta_id})


class AcessoriosUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('error')
    model = Acessorios
    fields = ['placaacc', 'bottomclaro', 'bottomescuro', 'bottomtepar', 'api', 'descarga', 'dreno', 'graudbolt',
              'olhodegato', 'mangote', 'macarico']
    template_name = 'form-acessorios.html'
    success_url = reverse_lazy('listar-cadastros-acessorios')


class AcessoriosDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('error')
    model = Acessorios
    template_name = 'form-acessorios-excluir.html'
    success_url = reverse_lazy('listar-cadastros-carretas')


class AcessoriosList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('error')
    model = Acessorios
    template_name = 'lista/acessorios-list.html'


