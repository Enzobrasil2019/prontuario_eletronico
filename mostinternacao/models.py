from django.db import models
from django.utils import timezone


class Internacao(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    nome_do_paciente = models.CharField(max_length=200)
    nome_do_pai = models.CharField(max_length=200)
    nome_da_mae = models.CharField(max_length=200)
    nome_do_medico_responsavel = models.CharField(max_length=200)
    nome_do_enfermeiro_responsavel = models.CharField(max_length=200)
    idade = models.CharField(max_length=200)
    doenca = models.CharField(max_length=200)
    data_de_nascimento = models.CharField(max_length=200)
    alergias = models.CharField(max_length=200)
    data_de_Internacao = models.CharField(max_length=200)
    setor_Internacao  = models.CharField(max_length=200)
    evolucao = models.CharField(max_length=200)
    encaminhamentos = models.CharField(max_length=200)
    medicamentos = models.CharField(max_length=200)
    exames = models.CharField(max_length=200)
    prescricao = models.TextField()
    tipo_de_atendimento = models.CharField(max_length=200)
    published_date = models.DateTimeField(
            blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Create your models here.

