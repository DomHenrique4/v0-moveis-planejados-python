"""
Schemas Pydantic para a API FastAPI.

Este arquivo define os modelos de dados para serialização/deserialização
na API, garantindo validação de tipos e documentação automática.
"""

from pydantic import BaseModel
from typing import List, Optional

class CategoriaBase(BaseModel):
    """Schema base para categorias com campos comuns."""
    nome: str
    slug: str

class Categoria(CategoriaBase):
    """
    Schema completo para categorias, incluindo ID e campos adicionais.
    
    Usado para respostas da API.
    """
    id: int
    descricao: str
    imagem: str
    
    class Config:
        """Configuração para permitir conversão de modelos ORM para schemas."""
        orm_mode = True

class AmbienteBase(BaseModel):
    """Schema base para ambientes."""
    nome: str
    slug: str

class Ambiente(AmbienteBase):
    """Schema completo para ambientes, incluindo ID."""
    id: int
    
    class Config:
        orm_mode = True

class TipoMovelBase(BaseModel):
    """Schema base para tipos de móveis."""
    nome: str
    slug: str

class TipoMovel(TipoMovelBase):
    """Schema completo para tipos de móveis, incluindo ID."""
    id: int
    
    class Config:
        orm_mode = True

class ImagemProduto(BaseModel):
    """Schema para imagens de produtos."""
    id: int
    imagem: str
    
    class Config:
        orm_mode = True

class ProdutoBase(BaseModel):
    """Schema base para produtos com campos comuns."""
    nome: str
    descricao: str
    imagem_principal: str
    slug: str

class Produto(ProdutoBase):
    """
    Schema para produtos com informações básicas.
    
    Usado para listagens de produtos.
    """
    id: int
    categoria_id: int
    destaque: bool
    
    class Config:
        orm_mode = True

class ProdutoDetalhado(Produto):
    """
    Schema para detalhes completos de um produto.
    
    Inclui relacionamentos com categoria, ambientes, tipos e imagens.
    Usado para a visualização detalhada de um produto.
    """
    categoria: Categoria
    ambientes: List[Ambiente]
    tipos: List[TipoMovel]
    imagens: List[ImagemProduto]
    
    class Config:
        orm_mode = True
