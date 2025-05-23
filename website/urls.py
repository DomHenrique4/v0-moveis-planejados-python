"""
Configuração de URLs para a aplicação principal (website).

Este arquivo define os padrões de URL para a aplicação website,
mapeando URLs para as views correspondentes.
"""

from django.urls import path
from . import views

urlpatterns = [
    # Página inicial
    path('', views.home, name='home'),
    
    # Catálogo de produtos
    path('catalogo/', views.CatalogoListView.as_view(), name='catalogo'),
    
    # Detalhes de um produto específico (usando slug para URLs amigáveis)
    path('produto/<slug:slug>/', views.ProdutoDetailView.as_view(), name='produto_detalhe'),
    
    # Detalhes de uma categoria específica
    path('categoria/<slug:slug>/', views.CategoriaDetailView.as_view(), name='categoria_detalhe'),
    
    # Formulário de contato
    path('contato/', views.ContatoCreateView.as_view(), name='contato'),
    
    # Página de sucesso após envio do formulário de contato
    path('contato/sucesso/', views.contato_sucesso, name='contato_sucesso'),
]
