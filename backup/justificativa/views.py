from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from .models import Justificativa
import logging

logger = logging.getLogger(__name__)


class JustificativaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('error')
    model = Justificativa
    fields = ['nome', 'email', 'descricao', 'titulo', 'status', 'data']
    template_name = 'justificativa.html'
    success_url = reverse_lazy('justificativa-lista')

    def form_valid(self, form):
        response = super().form_valid(form)

        justificativa = form.save()

        mensagem_administrador = f"""
        Nova justificativa enviada

        Detalhes da justificativa:
        Nome: {justificativa.nome}
        Email: {justificativa.email}
        Titulo: {justificativa.titulo}
        Descrição: {justificativa.descricao}
        Status: {justificativa.status}
        Data: {justificativa.data}
        """

        mensagem_usuario = f"""
        Olá {justificativa.nome},

        Recebemos sua justificativa. Aqui estão os detalhes:

        Nome: {justificativa.nome}
        Email: {justificativa.email}
        Titulo: {justificativa.titulo}
        Descrição: {justificativa.descricao}
        Status: {justificativa.status}
        Data: {justificativa.data}

        Aguarde até receber uma resposta!

        Atenciosamente,
        Via Dupla Transportes
        """

        try:
            send_mail(
                'Nova justificativa aberta',
                mensagem_administrador,
                settings.DEFAULT_FROM_EMAIL,
                ['aprendiz.bi@viadupla.com'],
                fail_silently=False,
            )
            send_mail(
                'Confirmação de Solicitação da justificativa',
                mensagem_usuario,
                settings.DEFAULT_FROM_EMAIL,
                [justificativa.email],
                fail_silently=False,
            )
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        except Exception as e:
            logger.error(f'Error sending email: {e}')

        return response

class JustificativaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('error')
    model = Justificativa
    fields = ['nome', 'email', 'descricao', 'titulo', 'status', 'data']
    template_name = 'justificativa.html'
    success_url = reverse_lazy('justificativa-lista')

class JustificativaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('error')
    model = Justificativa
    template_name = 'justificativa-excluir.html'
    success_url = reverse_lazy('justificativa-lista')

class JustificativaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('error')
    model = Justificativa
    template_name = 'lista/justificativa-listas.html'  # Template diferente para a listagem

