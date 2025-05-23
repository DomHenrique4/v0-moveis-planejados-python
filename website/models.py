"""
Modelos de dados para a aplicação de Móveis Planejados.

Este arquivo define a estrutura do banco de dados para a aplicação,
incluindo categorias, produtos, ambientes, tipos de móveis e contatos.
"""

from django.db import models
from django.utils.text import slugify

class Categoria(models.Model):
    """
    Modelo para categorias de produtos.
    
    Cada categoria pode conter múltiplos produtos e possui uma imagem representativa.
    O slug é gerado automaticamente a partir do nome para URLs amigáveis.
    """
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='categorias/')
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        """
        Sobrescreve o método save para gerar automaticamente o slug
        a partir do nome da categoria, caso não seja fornecido.
        """
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)
    
    def __str__(self):
        """Representação em string do objeto para exibição no admin e debugs."""
        return self.nome

class Ambiente(models.Model):
    """
    Modelo para ambientes (ex: sala, cozinha, quarto).
    
    Usado para categorizar produtos por tipo de ambiente.
    """
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        """Gera slug automaticamente a partir do nome."""
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nome

class TipoMovel(models.Model):
    """
    Modelo para tipos de móveis (ex: armário, mesa, cadeira).
    
    Usado para categorizar produtos por tipo de móvel.
    """
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        """Gera slug automaticamente a partir do nome."""
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nome

class Produto(models.Model):
    """
    Modelo principal para produtos (móveis planejados).
    
    Cada produto pertence a uma categoria e pode estar associado a
    múltiplos ambientes e tipos de móveis. Pode ter múltiplas imagens
    associadas através do modelo ImagemProduto.
    """
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem_principal = models.ImageField(upload_to='produtos/')
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE,  # Se a categoria for excluída, exclui os produtos
        related_name='produtos'    # Permite acessar produtos a partir da categoria
    )
    ambientes = models.ManyToManyField(
        Ambiente, 
        related_name='produtos'    # Relação muitos-para-muitos com ambientes
    )
    tipos = models.ManyToManyField(
        TipoMovel, 
        related_name='produtos'    # Relação muitos-para-muitos com tipos de móveis
    )
    destaque = models.BooleanField(default=False)  # Indica se o produto deve ser destacado na home
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        """Gera slug automaticamente a partir do nome."""
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nome

class ImagemProduto(models.Model):
    """
    Modelo para imagens adicionais de produtos.
    
    Permite associar múltiplas imagens a um produto para criar uma galeria.
    """
    produto = models.ForeignKey(
        Produto, 
        on_delete=models.CASCADE,  # Se o produto for excluído, exclui as imagens
        related_name='imagens'     # Permite acessar imagens a partir do produto
    )
    imagem = models.ImageField(upload_to='produtos/galerias/')
    
    def __str__(self):
        return f"Imagem de {self.produto.nome}"

class Contato(models.Model):
    """
    Modelo para armazenar mensagens de contato enviadas pelos usuários.
    
    Armazena informações básicas de contato e a mensagem enviada.
    """
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)  # Data de envio automática
    
    def __str__(self):
        return f"Contato de {self.nome} em {self.data_envio.strftime('%d/%m/%Y')}"
