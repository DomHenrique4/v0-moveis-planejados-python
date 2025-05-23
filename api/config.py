"""
Configuração da aplicação FastAPI.

Este arquivo fornece uma função para criar e configurar
uma instância da aplicação FastAPI com as configurações apropriadas.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def create_app():
    """
    Cria e configura uma instância da aplicação FastAPI.
    
    Configura metadados da API e middleware CORS.
    
    Returns:
        FastAPI: Instância configurada da aplicação FastAPI
    """
    # Cria a aplicação com metadados para a documentação automática
    app = FastAPI(
        title="Móveis Planejados API",
        description="API para o sistema de móveis planejados",
        version="1.0.0",
    )
    
    # Configuração de CORS para permitir acesso de outros domínios
    # IMPORTANTE: Em produção, restrinja as origens permitidas
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Em produção, especifique os domínios permitidos
        allow_credentials=True,
        allow_methods=["*"],  # Em produção, restrinja aos métodos necessários
        allow_headers=["*"],  # Em produção, restrinja aos cabeçalhos necessários
    )
    
    return app
