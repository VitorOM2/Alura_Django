from django.contrib import admin
from .models import Pessoas


class ListandoPessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'email')
    list_per_page: int = 50

admin.site.register(Pessoas, ListandoPessoas)
