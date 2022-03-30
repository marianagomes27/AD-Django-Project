from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

import csv
# Create your models here.
class Utente(models.Model):
    idu = models.AutoField(primary_key=True)
    utente_nome = models.CharField(max_length=200, unique=True)
    utente_cc = models.IntegerField(unique=True)
    utente_nif = models.IntegerField()
    utente_morada = models.CharField(max_length=200)
    utente_cp = models.CharField(max_length=50)

    def __str__(self):
        return "\n Utente: {0}\n ID: {1}".format(str(self.utente_nome), str(
            self.pk))  # self.pk chama o verdadeiro nome do utente em vez de chamar o adresso de memoria onde está


class Secretaria(models.Model):
    ids = models.AutoField(primary_key=True)
    sec_nome = models.CharField(max_length=200, unique=True)

    # sec_login = models.CharField(max_length= 100 )

    def __str__(self):
        return "\n Secretária: {0}\n ID: {1}".format(str(self.sec_nome), str(self.pk))


class Medico(models.Model):
    idm = models.AutoField(primary_key=True)
    med_nome = models.CharField(max_length=200, unique=True)
    med_nif = models.IntegerField()
    med_ced = models.IntegerField(unique=True)
    med_cc = models.IntegerField(unique=True)

    def __str__(self):
        return "\n Médico: {0}\n ID: {1}".format(str(self.med_nome), str(self.pk))


class Gestor(models.Model):
    idg = models.AutoField(primary_key=True)
    gestor_nome = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return "\n Gestor: {0}\n : ID: {1}".format(str(self.gestor_nome), str(self.pk))


class Medicamento(models.Model):
    cod_med = models.AutoField(primary_key=True)
    medicamento_dci = models.CharField(max_length=200)
    medicamento_nome = models.CharField(max_length=200)
    medicamento_dosagem = models.CharField(max_length=200)
    medicamento_estadoauth = models.CharField(max_length=100)
    medicamento_generico = models.CharField(max_length=100)
    medicamento_titular = models.CharField(max_length=200)
    medicamento_formafarmaceutica = models.CharField(max_length=200)

    def __str__(self):
        return "\n : Medicamento: {0}\n Codigo: {1}".format(str(self.medicamento_nome), str(self.pk))




class Exame(models.Model):
    ide = models.AutoField(primary_key=True)
    exame_data = models.DateField()
    exame_hora = models.TimeField()
    exame_tipo = models.CharField(max_length=200)
    exame_local = models.CharField(max_length=2000)
    idm = models.ForeignKey(Medico, on_delete=models.CASCADE)
    idu = models.ForeignKey(Utente, on_delete=models.CASCADE)
    exame_duracao = models.FloatField()
    exame_preco = models.FloatField()

    def __str__(self):
        self.ide, self.idm, self.idu


class Prescricao(models.Model):
    prescricao_codigo = models.AutoField(primary_key=True)
    prescricao_data = models.DateField()
    prescricao_hora = models.TimeField()
    prescricao_aviada = models.BooleanField(default=False)
    idm = models.ForeignKey(Medico, on_delete=models.CASCADE) #many-to-one relation
    idu = models.ForeignKey(Utente, on_delete=models.CASCADE)
    medprescrito = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    quantidade = models.IntegerField()


    def __str__(self):
        return self.prescricao_codigo, self.idm, self.idu



