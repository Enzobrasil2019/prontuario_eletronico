from django import forms

from .models import Internacao

class PostForm(forms.ModelForm):

    class Meta:
        model = Internacao
        fields = ('title', 'nome_do_paciente', 'nome_do_pai', 'nome_da_mae', 'nome_do_medico_responsavel', 'nome_do_enfermeiro_responsavel', 'idade', 'doenca', 'data_de_nascimento', 'alergias', 'data_de_Internacao', 'setor_Internacao', 'evolucao', 'encaminhamentos', 'medicamentos', 'exames', 'prescricao', 'tipo_de_atendimento')