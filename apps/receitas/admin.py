from django.contrib import admin
from .models import Receita


class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'publicada')
    list_display_links = ('id', 'nome_receita') # Faz o item virar um link
    search_fields = ('nome_receita',) # Cria um filtro com campos
    list_filter = ('categoria',) #Cria um filtro com categorias
    list_editable = ('publicada',)
    list_per_page = 20
admin.site.register(Receita, ListandoReceitas)
