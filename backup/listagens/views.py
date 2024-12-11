from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ListagemView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('error')
    template_name = "listagens.html"
    success_url = reverse_lazy('listagens')