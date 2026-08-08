from django.contrib import admin
from .models import Pessoa, Avaliacao
# Register your models here.

class PessoaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    list_filter = ['id']
    
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'pessoa', 'peso', 'altura', 'calcular_imc']
    list_filter = ['id']
    
admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Avaliacao, AvaliacaoAdmin)