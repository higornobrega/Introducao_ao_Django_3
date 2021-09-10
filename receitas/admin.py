from django.contrib import admin
from .models import Receita
@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
   list_display =  ('nome_receita', 'ingredientes', 'modo_preparo', 'tempo_preparo', 'rendimento', 'categoria', 'date_receita', )
   list_display_links = ('nome_receita', 'ingredientes', ) #Linka para o abrir o editar
   #filtros
   search_fields = ('nome_receita',) #Buscar, por escrito
   list_filter = ('categoria',) #Mostra apenas os dados da categoria escolhida
   list_per_page = 2 #Limita o tanto de itens exibidos por tela
