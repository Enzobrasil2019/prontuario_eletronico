from django.db import models
from django.utils import timezone


class Medico(models.Model):
    user = 'user'
    superuser = 'superuser'


    status = [(user, 'User'), (superuser, 'Superuser')]


    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    nome_do_medico = models.CharField(max_length=200)
    idade = models.CharField(max_length=200)
    formacao = models.CharField(max_length=200)
    especializacao = models.CharField(max_length=200)
    tempo_de_trabalho = models.CharField(max_length=200)
    setor_de_trabalho  = models.CharField(max_length=200)
    status = models.CharField(max_length=9,choices=status, default='user')
    senha = models.CharField(max_length=8, default=12345678)
    published_date = models.DateTimeField(
            blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Create your models here.


