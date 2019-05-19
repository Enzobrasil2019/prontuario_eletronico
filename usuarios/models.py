from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractUser)
# Create your models here.


class Usuario(AbstractBaseUser):
	Nome = models.CharField(max_length=150, default = '')
	Idade = models.CharField(max_length=4, default = '')
	CPF = models.CharField(max_length=11, default = '')
	Formacao = models.CharField(max_length=20, default = '')
	Tempo_de_trabalho = models.CharField(max_length=3, default = '')
	Especializacao = models.CharField(max_length=20, default = '')
	
	ativo = models(max_length=20, default = False)
	Admin = models(max_length=20, default = False)
	