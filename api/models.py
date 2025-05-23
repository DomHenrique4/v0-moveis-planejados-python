"""
Modelos SQLAlchemy para a API FastAPI.

Este arquivo define os modelos SQLAlchemy que mapeiam para as
mesmas tabelas do banco de dados usadas pelo Django.
"""

from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship
from .database import Base

# Tabelas de relacionamento para relações muitos-para-muitos
# Mapeia para a tabela de relacionamento entre produtos e ambientes criada pelo Django
produto_ambiente = Table(
    'website_produto_ambientes',
    Base.metadata,
    Column('produto_id', Integer, ForeignKey('website_produto.id')),
    Column('ambiente_id', Integer, ForeignKey('website_ambiente.id'))
)

# Mapeia para a tabela de relacionamento entre produtos e tipos de móveis criada pelo Django
produto_tipo = Table(
    'website_produto_tipos',
    Base.metadata,
    Column('produto_id', Integer, ForeignKey('website_produto.id')),
    Column('tipomove_id', Integer, ForeignKey('website_tipomovel.id'))
)

class Categoria(Base):
    """
    Modelo SQLAlchemy para categorias.
    
    Mapeia para a tabela 'website_categoria' criada pelo Django.
    """
    __tablename__ = "website_categoria"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(Text)
    imagem = Column(String)
    slug = Column(String, unique=True, index=True)
    
    # Relacionamento com produtos (um para muitos)
    produtos = relationship("Produto", back_populates="categoria")

class Ambiente(Base):
    """
    Modelo SQLAlchemy para ambientes.
    
    Mapeia para a tabela 'website_ambiente' criada pelo Django.
    """
    __tablename__ = "website_ambiente"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    slug = Column(String, unique=True, index=True)
    
    # Relacionamento com produtos (muitos para muitos)
    produtos = relationship("Produto", secondary=produto_ambiente, back_populates="ambientes")

class TipoMovel(Base):
    """
    Modelo SQLAlchemy para tipos de móveis.
    
    Mapeia para a tabela 'website_tipomovel' criada pelo Django.
    """
    __tablename__ = "website_tipomovel"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    slug = Column(String, unique=True, index=True)
    
    # Relacionamento com produtos (muitos para muitos)
    produtos = relationship("Produto", secondary=produto_tipo, back_populates="tipos")

class Produto(Base):
    """
    Modelo SQLAlchemy para produtos.
    
    Mapeia para a tabela 'website_produto' criada pelo Django.
    """
    __tablename__ = "website_produto"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(Text)
    imagem_principal = Column(String)
    categoria_id = Column(Integer, ForeignKey("website_categoria.id"))
    destaque = Column(Boolean, default=False)
    slug = Column(String, unique=True, index=True)
    
    # Relacionamentos
    categoria = relationship("Categoria", back_populates="produtos")
    ambientes = relationship("Ambiente", secondary=produto_ambiente, back_populates="produtos")
    tipos = relationship("TipoMovel", secondary=produto_tipo, back_populates="produtos")
    imagens = relationship("ImagemProduto", back_populates="produto")

class ImagemProduto(Base):
    """
    Modelo SQLAlchemy para imagens de produtos.
    
    Mapeia para a tabela 'website_imagemproduto' criada pelo Django.
    """
    __tablename__ = "website_imagemproduto"

    id = Column(Integer, primary_key=True, index=True)
    produto_id = Column(Integer, ForeignKey("website_produto.id"))
    imagem = Column(String)
    
    # Relacionamento com produto (muitos para um)
    produto = relationship("Produto", back_populates="imagens")
