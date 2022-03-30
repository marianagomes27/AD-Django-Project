from django import forms
from django.contrib.auth import authenticate

from .models import *




class FormularioMedico(forms.ModelForm):
    class Meta:
        model = Medico
        fields = [
            "idm",
            "med_nome",
            "med_nif",
            "med_ced",
            "med_cc"
        ]

class FormularioExame(forms.ModelForm):
    class Meta:
        model = Exame
        fields = [
            "ide",
            "exame_data",
            "exame_hora",
            "exame_tipo",
            "exame_local",
            "idm",
            "idu",
            "exame_duracao",
            "exame_preco",
        ]


class FormularioUtente(forms.ModelForm):
    class Meta:
        model = Utente
        fields = [
            "idu",
            "utente_nome",
            "utente_nif",
            "utente_cc",
            "utente_morada",
            "utente_cp",

        ]

class FormularioPrescricao(forms.ModelForm):
    class Meta:
        model = Prescricao
        fields = [
            "prescricao_codigo",
            "prescricao_data",
            "prescricao_hora",

            "prescricao_aviada",
            "idm",
            "idu",
            "quantidade",
            "medprescrito",
        ]

class FormularioSec(forms.ModelForm):
    class Meta:
        model = Secretaria
        fields = [
            "ids",
            "sec_nome",
        ]



class FormularioMed(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = [
            "cod_med",
            "medicamento_dci" ,
            "medicamento_nome",
            "medicamento_dosagem",
            "medicamento_estadoauth",
            "medicamento_generico",
            "medicamento_titular",
            "medicamento_formafarmaceutica",
        ]


class FormularioProcurarUtente(forms.Form):
    utente_cc = forms.IntegerField()




class FormularioProcurarExame(forms.Form):
    exame_tipo = forms.CharField()

class FormularioProcurarMedicamento(forms.Form):
    medicamento_dci = forms.CharField()

class FormularioProcurarSecretaria(forms.Form):
    sec_nome = forms.CharField()

class FormularioProcurarMedico(forms.Form):
    med_ced = forms.IntegerField()





