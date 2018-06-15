from django.contrib import admin
from .models import Categoria, Imovel

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug']
    prepopulated_fields = {'slug': ('nome',)}
admin.site.register(Categoria, CategoriaAdmin)

class ImovelAdmin(admin.ModelAdmin):
    list_display = ['rua', 'slug', 'categoria', 'cep', 'preco', 'disponivel','endereco','descricao' ,'data_cadastramento', 'data_atualizacao']
    list_filter = ['disponivel', 'data_cadastramento', 'categoria', 'cep']
    list_editable = ['preco', 'descricao', 'disponivel','endereco']
    prepopulated_fields = {'slug': ('numero','rua','cep')}
admin.site.register(Imovel, ImovelAdmin)

# Register your models here.
