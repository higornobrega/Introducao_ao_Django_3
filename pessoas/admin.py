from django.contrib import admin
from .models import Pessoa

@admin.register(Pessoa)

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', )
    list_display_links = ('nome', 'email', )
    search_fields = ('nome',)
    list_per_page = 2
