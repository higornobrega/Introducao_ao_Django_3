from django.contrib import admin
from .models import Receita
@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
   list_display =  ('nome_receita', 'ingredientes', 'modo_preparo', 'tempo_preparo', 'rendimento', 'categoria', 'date_receita', )
