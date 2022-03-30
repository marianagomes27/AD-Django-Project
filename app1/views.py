from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.db.models import Count
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User

from .models import *
from .forms import *



def index(request):
    return render(request, "index.html", {})

def medicos(request):
    return render(request, "medicos.html", {})

def gestor(request):
    return render(request, "gestor.html", {})

def secretaria(request):
    return render(request, "secretaria.html", {})

def users(request):
    return render(request, "users.html", {})



def adicionarmedico(request):
    f = FormularioMedico(request.POST or None)
    if f.is_valid():
        i=f.save(commit=False)
        i.save()
        messages.success(request, "Médico inserido com sucesso!")
    context = {"form": f}
    return render(request, "adicionarmedico.html", context)

def addexame(request):
    f = FormularioExame(request.POST or None)
    if f.is_valid(): #se o formulario for valido o exame é guardado na base de dados
        i = f.save(commit=False)
        i.save()
        messages.success(request, "Exame inserido com sucesso!")
    context = {"form": f}
    return render(request, "addexame.html", context)

def addutente(request):
    f = FormularioUtente(request.POST or None)
    if f.is_valid():
        i = f.save(commit=False)
        i.save()
        messages.success(request, "Utente inserido com sucesso!")
    context = {
        "form": f,
    }
    return render(request, "addutente.html", context)

def addprescricao(request):
    form= FormularioPrescricao(request.POST or None)

    if form.is_valid():
        i = form.save(commit=False)
        i.save()
        messages.success(request, "Prescrição adicionada com sucesso!")

    context = {
        "form": form
    }
    return render(request, "addprescricao.html", context)

def addsecretaria(request):
    form= FormularioSec(request.POST or None)

    if form.is_valid():
        i = form.save(commit=False)
        i.save()
        messages.success(request, "Secretária adicionada com sucesso!")

    context = {
        "form": form
    }
    return render(request, "addsecretaria.html", context)

def procurarutente(request):
    form = FormularioProcurarUtente(request.POST or None)
    if form.is_valid():
        i = form.cleaned_data.get('utente_cc')
        utente = get_object_or_404(Utente, utente_cc=i)

        context1 = {
            "u": utente,

        }
        return render(request, "info_utente.html", context1)
    context2 = {
        "form": form
    }
    return render(request, "procurarutente.html", context2)




def adicionarmedicamento(request):
    f = FormularioMed(request.POST or None)
    if f.is_valid():
        i = f.save(commit=False)
        i.save()
        messages.success(request, "Medicamento inserido com sucesso!")
    context = {
        "form": f
    }
    return render(request, "adicionarmedicamento.html", context)

def procurarexame(request):
    form = FormularioProcurarExame(request.POST or None)

    if form.is_valid():
        i = form.cleaned_data.get('exame_tipo')
        exame = Exame.objects.filter(exame_tipo=i)
        context3 = {
            "exame": exame,
        }
        return render(request, "info_exame.html", context3)

    context2 = {
        "form": form

    }
    return render(request, "procurarexame.html", context2)


def procurarmedicamento(request):
    form = FormularioProcurarMedicamento(request.POST or None)
    if form.is_valid():
        i = form.cleaned_data.get('medicamento_dci')
        medicamento = get_object_or_404(Medicamento, medicamento_dci=i)


        context1 = {

            "m": medicamento}

        return render(request, "info_medicamento.html", context1)

    context2 = {
        "form": form

    }
    return render(request, "procurarmedicamento.html", context2)



def procurarsecretaria(request):
    form = FormularioProcurarSecretaria(request.POST or None)
    if form.is_valid():
        i = form.cleaned_data.get('sec_nome')
        sec = get_object_or_404(Secretaria, sec_nome=i)

        context1 = {

            "s": sec}

        return render(request, "info_secretaria.html", context1)

    context2 = {
        "form": form

    }
    return render(request, "procurarsecretaria.html", context2)

def procurarmedico(request):
    form = FormularioProcurarMedico(request.POST or None)
    if form.is_valid():
        i = form.cleaned_data.get('med_ced')
        medico = get_object_or_404(Medico, med_ced=i)

        context1 = {

            "m1": medico}

        return render(request, "info_medico.html", context1)

    context2 = {
        "form": form

    }
    return render(request, "procurarmedico.html", context2)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)


                return redirect('users')
            else:
                messages.error(request, "Username ou password inválidos!")
        else:
            messages.error(request, "Username ou password inválidos!")
    form = AuthenticationForm()
    return render(request = request,
                  template_name ="login.html",
                  context={"form":form})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, "Utilizador registado com sucesso!")

            username = form.cleaned_data.get('username')
            login(request, user)


        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "register.html",
                          context={"form":form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "register.html",
                  context={"form":form})


def logout_request(request):
    logout(request)
    return redirect("index")


