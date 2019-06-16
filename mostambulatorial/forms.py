from django import forms

from .models import Ambulatorio

class PostForm(forms.ModelForm):

    class Meta:
        model = Ambulatorio
        fields = ('title', 'nome_do_paciente', 'nome_do_pai', 'nome_da_mae', 'nome_do_medico_responsavel', 'nome_do_enfermeiro_responsavel', 'idade', 'doenca', 'data_de_nascimento', 'alergias', 'data_de_atendimento', 'setor_Ambulatorio', 'medico', 'evolucao', 'encaminhamentos', 'exames', 'tipo_de_atendimento', 'prescricao')