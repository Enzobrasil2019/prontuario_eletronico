class Pacientes():
    
    self.nome = models.charfield(max_length=150, default='')
    self.idade = models.charfield(max_length=3, default='')
    self.mae = models.charfield(max_length=150, default='')
    self.pai = models.charfield(max_length=150, default='')
    self.data_de_nascimento = models.charfield(max_length=11, default='')
    self.doenca = models.charfield(max_length=500, default='')
    self.alergia = models.charfield(max_length=500, default='')
    self.tipo_de_atendimento = models.charfield(max_length=15, default='')










class Ambulatorio(Pacientes):
    
    self.Data_de_atendimento = models.charfield(max_length=11, default='')
    self.Setor_ambulatorial = models.charfield(max_length=8, default='')
    self.Medico = models.charfield(max_length=150, default='')
    self.Encaminhamentos = models.charfield(max_length=500, default='')
    self.Evolucao = models.charfield(max_length=500, default='')
    self.Exames = models.charfield(max_length=500, default='')
    self.Prescricao = models.charfield(max_length=500, default='')


class Internacao(Pacientes):
    
    self.Data_de_internacao = models.charfield(max_length=11, default='')
    self.Setor_da_internacao = models.charfield(max_length=8, default='')
    self.Medico_responsavel = models.charfield(max_length=150, default='')
    self.Emfermeira_responsavel = models.charfield(max_length=150, default='')
    self.Evolucao = models.charfield(max_length=500, default='')
    self.Medicamentos = models.charfield(max_length=500, default='')
    

class adicionar_pacientes():
    def Registrar_paciente(self, nome, idade, mae, pai, data_de_nascimento, doenca, alergia, tipo_de_atendimento):
        self.pacientes.append(nome, idade, mae, pai, data_de_nascimento, doenca, alergia, tipo_de_atendimento)

    def Registrar_local_de_internacao(Data_de_atendimento, Setor_ambulatorial, Medico, Encaminhamentos, Evolucao, Exames, Prescricao, Data_de_internacao, Medico_responsavel, Emfermeira_responsavel, Evolucao, Medicamentos) 
        if (tipo_de_atendimento = 'ambulatorial'):
            self.pacientes.append(Data_de_atendimento, Setor_ambulatorial, Medico, Encaminhamentos, Evolucao, Exames, Prescricao)

        elif (tipo_de_atendimento = 'internação'):
            self.pacientes.append(Data_de_internacao, Medico_responsavel, Emfermeira_responsavel, Evolucao, Medicamentos)
            
            
