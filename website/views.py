"""
Views para a aplicação de Móveis Planejados.

Este arquivo contém as views (controladores) que processam as requisições
e retornam as respostas para o usuário, renderizando os templates apropriados.
"""

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Categoria, Produto, Ambiente, TipoMovel, Contato
from .forms import ContatoForm

def home(request):
    """
    View para a página inicial (home).
    
    Exibe as categorias e produtos em destaque, com meta tags otimizadas para SEO.
    
    Args:
        request: Objeto HttpRequest
        
    Returns:
        HttpResponse com o template renderizado
    """
    # Busca até 6 categorias para exibir na seção de categorias
    categorias = Categoria.objects.all()[:6]
    
    # Busca até 3 produtos marcados como destaque para a seção "Design que Inspira"
    produtos_destaque = Produto.objects.filter(destaque=True)[:3]
    
    # Contexto com dados para o template e meta tags para SEO
    context = {
        'categorias': categorias,
        'produtos_destaque': produtos_destaque,
        'meta_title': 'Móveis Planejados de Alta Qualidade | Design Personalizado',
        'meta_description': 'Transforme sua casa com móveis planejados de alta qualidade. Designs exclusivos e personalizados para cada ambiente. Solicite um orçamento hoje!',
    }
    return render(request, 'website/home.html', context)

class CatalogoListView(ListView):
    """
    View baseada em classe para listar produtos no catálogo.
    
    Permite filtrar produtos por categoria, ambiente e tipo de móvel.
    Implementa paginação para melhor experiência do usuário.
    """
    model = Produto
    template_name = 'website/catalogo.html'
    context_object_name = 'produtos'
    paginate_by = 12  # Número de produtos por página
    
    def get_queryset(self):
        """
        Sobrescreve o método para aplicar filtros à consulta.
        
        Filtra produtos com base nos parâmetros da URL (GET).
        
        Returns:
            QuerySet filtrado de produtos
        """
        queryset = Produto.objects.all()
        
        # Obtém parâmetros de filtro da URL
        categoria_slug = self.request.GET.get('categoria')
        ambiente_slug = self.request.GET.get('ambiente')
        tipo_slug = self.request.GET.get('tipo')
        
        # Aplica filtros se os parâmetros estiverem presentes
        if categoria_slug:
            queryset = queryset.filter(categoria__slug=categoria_slug)
        
        if ambiente_slug:
            queryset = queryset.filter(ambientes__slug=ambiente_slug)
            
        if tipo_slug:
            queryset = queryset.filter(tipos__slug=tipo_slug)
            
        return queryset
    
    def get_context_data(self, **kwargs):
        """
        Adiciona dados adicionais ao contexto do template.
        
        Inclui listas de ambientes, tipos e categorias para os filtros,
        além de meta tags para SEO.
        
        Returns:
            Dicionário de contexto enriquecido
        """
        context = super().get_context_data(**kwargs)
        
        # Adiciona listas para os filtros
        context['ambientes'] = Ambiente.objects.all()
        context['tipos'] = TipoMovel.objects.all()
        context['categorias'] = Categoria.objects.all()
        
        # Meta tags para SEO
        context['meta_title'] = 'Catálogo de Móveis Planejados | Diversos Estilos e Ambientes'
        context['meta_description'] = 'Explore nosso catálogo completo de móveis planejados para todos os ambientes. Filtros por tipo de móvel e ambiente para facilitar sua busca.'
        
        return context

class ProdutoDetailView(DetailView):
    """
    View baseada em classe para exibir detalhes de um produto específico.
    
    Exibe informações detalhadas do produto e produtos relacionados da mesma categoria.
    """
    model = Produto
    template_name = 'website/produto_detalhe.html'
    context_object_name = 'produto'
    
    def get_context_data(self, **kwargs):
        """
        Adiciona produtos relacionados e meta tags ao contexto.
        
        Returns:
            Dicionário de contexto enriquecido
        """
        context = super().get_context_data(**kwargs)
        produto = self.get_object()
        
        # Busca produtos da mesma categoria, excluindo o produto atual
        context['produtos_relacionados'] = Produto.objects.filter(
            categoria=produto.categoria
        ).exclude(id=produto.id)[:4]
        
        # Meta tags para SEO
        context['meta_title'] = f'{produto.nome} | Móveis Planejados'
        context['meta_description'] = produto.descricao[:160]  # Limita a 160 caracteres para SEO
        
        return context

class CategoriaDetailView(DetailView):
    """
    View baseada em classe para exibir detalhes de uma categoria.
    
    Exibe informações da categoria e lista os produtos pertencentes a ela.
    """
    model = Categoria
    template_name = 'website/categoria_detalhe.html'
    context_object_name = 'categoria'
    
    def get_context_data(self, **kwargs):
        """
        Adiciona produtos da categoria e meta tags ao contexto.
        
        Returns:
            Dicionário de contexto enriquecido
        """
        context = super().get_context_data(**kwargs)
        categoria = self.get_object()
        
        # Busca produtos da categoria
        context['produtos'] = Produto.objects.filter(categoria=categoria)
        
        # Meta tags para SEO
        context['meta_title'] = f'{categoria.nome} | Móveis Planejados'
        context['meta_description'] = f'Conheça nossa linha de {categoria.nome.lower()}. Móveis planejados com design exclusivo e alta qualidade para transformar seu ambiente.'
        
        return context

class ContatoCreateView(CreateView):
    """
    View baseada em classe para o formulário de contato.
    
    Permite aos usuários enviar mensagens através do formulário de contato.
    """
    model = Contato
    form_class = ContatoForm
    template_name = 'website/contato.html'
    success_url = reverse_lazy('contato_sucesso')  # Redireciona após envio bem-sucedido
    
    def get_context_data(self, **kwargs):
        """
        Adiciona meta tags ao contexto.
        
        Returns:
            Dicionário de contexto enriquecido
        """
        context = super().get_context_data(**kwargs)
        
        # Meta tags para SEO
        context['meta_title'] = 'Fale Conosco | Móveis Planejados'
        context['meta_description'] = 'Entre em contato conosco para orçamentos, dúvidas ou sugestões sobre nossos móveis planejados. Estamos prontos para atendê-lo!'
        
        return context

def contato_sucesso(request):
    """
    View simples para exibir página de sucesso após envio do formulário de contato.
    
    Args:
        request: Objeto HttpRequest
        
    Returns:
        HttpResponse com o template renderizado
    """
    return render(request, 'website/contato_sucesso.html')
