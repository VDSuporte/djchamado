from django import forms
from .models import Justificativa

class JustificativaForm(forms.ModelForm):
    class Meta:
        model = Justificativa
        fields = ['nome', 'email', 'titulo', 'descricao', 'status', 'data']
