from django import forms

from .models import Medico

class PostForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['title', 'nome_do_medico','idade', 'formacao', 'especializacao', 'tempo_de_trabalho', 'setor_de_trabalho', 'status']

