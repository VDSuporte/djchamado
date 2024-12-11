from django import forms
from .models import Chamados

class ChamadoForm(forms.ModelForm):
    class Meta:
        model = Chamados
        fields = ['nome', 'email', 'descricao', 'departamento', 'status', 'data', 'anexo']
        widgets = {
            'data': forms.HiddenInput(),
            'status': forms.HiddenInput(),
        }

    anexo = forms.FileField(required=False, label='Anexo')
