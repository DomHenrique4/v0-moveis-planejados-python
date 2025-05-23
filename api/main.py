"""
API FastAPI para a aplicação de Móveis Planejados.

Este arquivo define os endpoints da API RESTful que permite
acesso programático aos dados da aplicação.
"""

from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional
from . import schemas, database, models

# Inicialização da aplicação FastAPI
app = FastAPI(title="Móveis Planejados API")

# Configuração de CORS para permitir acesso de outros domínios
# IMPORTANTE: Em produção, restrinja as origens permitidas
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique os domínios permitidos
    allow_credentials=True,
    allow_methods=["*"],  # Em produção, restrinja aos métodos necessários
    allow_headers=["*"],  # Em produção, restrinja aos cabeçalhos necessários
)

# Dependência para obter a sessão do banco de dados
def get_db():
    """
    Função de dependência para obter uma sessão do banco de dados.
    
    Cria uma nova sessão para cada requisição e garante que ela seja fechada
    após o processamento, mesmo em caso de exceção.
    
    Yields:
        Session: Sessão do SQLAlchemy para interagir com o banco de dados
    """
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/produtos/", response_model=List[schemas.Produto])
def listar_produtos(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    categoria: Optional[str] = None,
    ambiente: Optional[str] = None,
    tipo: Optional[str] = None
):
    """
    Endpoint para listar produtos com opções de filtro.
    
    Args:
        db: Sessão do banco de dados (injetada pela dependência)
        skip: Número de registros para pular (paginação)
        limit: Número máximo de registros a retornar
        categoria: Filtro opcional por slug da categoria
        ambiente: Filtro opcional por slug do ambiente
        tipo: Filtro opcional por slug do tipo de móvel
        
    Returns:
        Lista de produtos que correspondem aos filtros
    """
    # Inicia com todos os produtos
    query = db.query(models.Produto)
    
    # Aplica filtros se fornecidos
    if categoria:
        query = query.filter(models.Produto.categoria.has(slug=categoria))
    
    if ambiente:
        query = query.filter(models.Produto.ambientes.any(slug=ambiente))
    
    if tipo:
        query = query.filter(models.Produto.tipos.any(slug=tipo))
    
    # Aplica paginação e retorna resultados
    return query.offset(skip).limit(limit).all()

@app.get("/categorias/", response_model=List[schemas.Categoria])
def listar_categorias(db: Session = Depends(get_db)):
    """
    Endpoint para listar todas as categorias.
    
    Args:
        db: Sessão do banco de dados (injetada pela dependência)
        
    Returns:
        Lista de todas as categorias
    """
    return db.query(models.Categoria).all()

@app.get("/ambientes/", response_model=List[schemas.Ambiente])
def listar_ambientes(db: Session = Depends(get_db)):
    """
    Endpoint para listar todos os ambientes.
    
    Args:
        db: Sessão do banco de dados (injetada pela dependência)
        
    Returns:
        Lista de todos os ambientes
    """
    return db.query(models.Ambiente).all()

@app.get("/tipos/", response_model=List[schemas.TipoMovel])
def listar_tipos(db: Session = Depends(get_db)):
    """
    Endpoint para listar todos os tipos de móveis.
    
    Args:
        db: Sessão do banco de dados (injetada pela dependência)
        
    Returns:
        Lista de todos os tipos de móveis
    """
    return db.query(models.TipoMovel).all()

@app.get("/produtos/{produto_id}", response_model=schemas.ProdutoDetalhado)
def detalhe_produto(produto_id: int, db: Session = Depends(get_db)):
    """
    Endpoint para obter detalhes de um produto específico.
    
    Args:
        produto_id: ID do produto a ser consultado
        db: Sessão do banco de dados (injetada pela dependência)
        
    Returns:
        Detalhes do produto solicitado
        
    Raises:
        HTTPException: Se o produto não for encontrado (404)
    """
    produto = db.query(models.Produto).filter(models.Produto.id == produto_id).first()
    if produto is None:
        # Retorna erro 404 se o produto não for encontrado
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto
