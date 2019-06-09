from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone



class Pacientes(models.Model):
    
    nome = models.CharField(max_length=150, default='')
    idade = models.CharField(max_length=3, default='')
    mae = models.CharField(max_length=150, default='')
    pai = models.CharField(max_length=150, default='')
    data_de_nascimento = models.CharField(max_length=11, default='')
    doenca = models.CharField(max_length=500, default='')
    alergia = models.CharField(max_length=500, default='')
    tipo_de_atendimento = models.CharField(max_length=15, default='')
    Data_de_atendimento = models.CharField(max_length=11, default='')
    Setor_ambulatorial = models.CharField(max_length=8, default='')
    Medico = models.CharField(max_length=150, default='')
    Encaminhamentos = models.CharField(max_length=500, default='')
    Evolucao = models.CharField(max_length=500, default='')
    Exames = models.CharField(max_length=500, default='')
    Prescricao = models.CharField(max_length=500, default='')

    def publish(self):
        self.published_date = timezone.now()
        self.save()



    def __str__(self):
        return self.nome
