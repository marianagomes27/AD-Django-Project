import csv, sys, os

project_dir = "C:/Users/Mariana/PycharmProjects/ADTP2/lista_infomed.csv"

sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from app1.models import Medicamento
def run():
    r = csv.reader(open("C:/Users/Mariana/PycharmProjects/ADTP2/lista_infomed.csv", encoding="utf8"), delimiter=";")
    for row in r:
        if row[0] != 'dci':
            medicamentos = Medicamento()
            medicamentos.medicamento_dci = row[0]
            medicamentos.medicamento_nome = row[1]
            medicamentos.medicamento_formafarmaceutica = row[2]
            medicamentos.medicamento_dosagem = row[3]
            medicamentos.medicamento_estadoauth = row[4]
            medicamentos.medicamento_generico= row[5]
            medicamentos.medicamento_titular = row[6]
            medicamentos.save()



