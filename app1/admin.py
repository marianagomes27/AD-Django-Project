from django.contrib import admin

# Register your models here.

from app1.models import *

# Register your models here.
admin.site.register(Medicamento)
admin.site.register(Medico)
admin.site.register(Utente)

admin.site.register(Prescricao)
admin.site.register(Exame)
admin.site.register(Secretaria)
admin.site.register(Gestor)


