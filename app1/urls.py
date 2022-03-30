from django.urls import path
from . import views
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^gestor', views.gestor, name='gestor'),
    url(r'^adicionarmedico', views.adicionarmedico, name='adicionarmedico'),
    url(r'^secretaria', views.secretaria, name='secretaria'),
    url(r'^addexame', views.addexame, name='addexame'),
    url(r'^medicos', views.medicos, name='medicos'),
    url(r'^addutente', views.addutente, name='addutente'),
    url(r'^addprescricao', views.addprescricao, name='addprescricao'),
    url(r'^adicionarmedicamento', views.adicionarmedicamento, name='adicionarmedicamento'),
    url(r'^addsecretaria', views.addsecretaria, name='addsecretaria'),
    url(r'^procurarutente', views.procurarutente, name='procurarutente'),
    url(r'^procurarexame', views.procurarexame, name='procurarexame'),
    url(r'^procurarmedicamento', views.procurarmedicamento, name='procurarmedicamento'),
    url(r'^procurarmedico', views.procurarmedico, name='procurarmedico'),
    url(r'^procurarsecretaria', views.procurarsecretaria, name='procurarsecretaria'),


url(r'^login', views.login_view, name='login'),
url(r'^logout', views.logout_request, name='logout'),

url(r'^users', views.users, name='users'),
url(r'^register', views.register, name='register'),










]