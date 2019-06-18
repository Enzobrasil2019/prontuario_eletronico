from django import forms

class Postlogin(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nome_do_medico', 'senha']

