# Generated by Django 2.2.1 on 2019-06-14 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Internacao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('nome_do_paciente', models.CharField(max_length=200)),
                ('nome_do_pai', models.CharField(max_length=200)),
                ('nome_da_mae', models.CharField(max_length=200)),
                ('nome_do_medico_responsavel', models.CharField(max_length=200)),
                ('nome_do_enfermeiro_responsavel', models.CharField(max_length=200)),
                ('idade', models.CharField(max_length=200)),
                ('doenca', models.CharField(max_length=200)),
                ('data_de_nascimento', models.CharField(max_length=200)),
                ('alergias', models.CharField(max_length=200)),
                ('data_de_Internacao', models.CharField(max_length=200)),
                ('setor_Internacao', models.CharField(max_length=200)),
                ('evolucao', models.CharField(max_length=200)),
                ('encaminhamentos', models.CharField(max_length=200)),
                ('medicamentos', models.CharField(max_length=200)),
                ('exames', models.CharField(max_length=200)),
                ('prescricao', models.TextField()),
                ('tipo_de_atendimento', models.CharField(max_length=200)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
