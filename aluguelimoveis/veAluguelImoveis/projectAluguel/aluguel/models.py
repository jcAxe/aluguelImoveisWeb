from django.db import models
import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse
import PIL


class Categoria(models.Model):
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nome

    def get_absolute_path(self):
        return reverse('aluguel:lista_imoveis_por_categoria', args=[self.slug])

class Imovel(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='imoveis')
    #nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    imagem = models.ImageField(upload_to='imoveis', blank=True)
    #imagem = models.TextField(upload_to='imoveis', blank=True)
    descricao = models.TextField(blank=True)
    dono = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    numero = models.PositiveIntegerField()
    rua = models.CharField(max_length=200, db_index=True)
    bairro = models.CharField(max_length=200, db_index=True)
    cidade = models.CharField(max_length=200, db_index=True)
    estado = models.CharField(max_length=200, db_index=True)
    pais = models.CharField(max_length=200, db_index=True)
    cep = models.CharField(max_length=200, db_index=True)
    disponivel = models.BooleanField(default=True)
    data_cadastramento = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    endereco = models.TextField(blank=True)

    class Meta:
        ordering = ('cidade',)
        verbose_name = 'imovel'
        verbose_name_plural = 'imoveis'

    def cadastrado_recentemente(self):
        return self.data_cadastramento >= timezone.now() - datetime.timedelta(days=1)

    def get_absolute_path(self):
        return reverse('aluguel:exibe_imovel', args=[self.id, self.slug])

    def __str__(self):
        return self.endereco