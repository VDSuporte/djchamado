from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
class IndexView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('error')
    template_name = "menu.html"

def my_view(request):
    return render(request, 'error.html')
@login_required
def home_view(request):
    return render(request, 'menu.html', {'user': request.user})