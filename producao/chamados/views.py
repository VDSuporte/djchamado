from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Chamados
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import ChamadoForm
from django.conf import settings
import mimetypes
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect


class ChamadosCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('error')
    model = Chamados
    fields = ['nome', 'email', 'descricao', 'departamento', 'status', 'data', 'anexo']  # Campo 'status' adicionado
    template_name = 'chamado.html'
    success_url = reverse_lazy('listar-chamados')


class ChamadosUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('error')
    model = Chamados
    fields = ['nome', 'email', 'descricao', 'departamento', 'status', 'data', 'anexo']
    template_name = 'chamado.html'
    success_url = reverse_lazy('listar-chamados')


class ChamadosDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('error')
    model = Chamados
    template_name = 'chamado-excluir.html'
    success_url = reverse_lazy('listar-chamados')


class ChamadosList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('error')
    model = Chamados
    template_name = 'lista/chamados-list.html'

def reverter_status(request, pk):
    chamado = get_object_or_404(Chamados, pk=pk)
    # Reverter o status
    chamado.status = 'P' if chamado.status == 'M' else 'M'
    chamado.save()
    return redirect('listar-chamados')    


def solicitar_chamado(request):
    if request.method == 'POST':
        form = ChamadoForm(request.POST, request.FILES)
        if form.is_valid():
            chamado = form.save()

            # Criar mensagem para o administrador
            mensagem_administrador = f"""
            Novo Chamado Solicitado

            Detalhes do chamado:
            Nome: {chamado.nome}
            Email: {chamado.email}
            Departamento: {chamado.departamento}
            Descrição: {chamado.descricao}
            Status: {chamado.status}
            Data: {chamado.data}
            """

            email_administrador = EmailMessage(
                'Novo Chamado Solicitado',
                mensagem_administrador,
                settings.EMAIL_HOST_USER,
                ['aprendiz.bi@viadupla.com'],
            )

            # Anexar arquivo se existir
            if chamado.anexo:
                # Obter o tipo MIME do arquivo
                content_type, encoding = mimetypes.guess_type(chamado.anexo.name)
                content_type = content_type or 'application/octet-stream'
                email_administrador.attach(chamado.anexo.name, chamado.anexo.read(), content_type)

            email_administrador.send(fail_silently=False)

            # Criar mensagem para o usuário
            mensagem_usuario = f"""
            Olá {chamado.nome},

            Recebemos sua solicitação de chamado. Aqui estão os detalhes:

            Nome: {chamado.nome}
            Email: {chamado.email}
            Departamento: {chamado.departamento}
            Descrição: {chamado.descricao}
            Status: {chamado.status}
            Data: {chamado.data}

            Aguarde até receber uma resposta!

            Atenciosamente:
            Via Dupla Transportes
            """

            email_usuario = EmailMessage(
                'Confirmação de Solicitação de Chamado',
                mensagem_usuario,
                settings.EMAIL_HOST_USER,
                [chamado.email],
            )

            # Anexar arquivo se existir
            if chamado.anexo:
                # Obter o tipo MIME do arquivo
                content_type, encoding = mimetypes.guess_type(chamado.anexo.name)
                content_type = content_type or 'application/octet-stream'
                email_usuario.attach(chamado.anexo.name, chamado.anexo.read(), content_type)

            email_usuario.send(fail_silently=False)

            return redirect('listar-chamados')
    else:
        form = ChamadoForm()

    return render(request, 'chamado.html', {'form': form})