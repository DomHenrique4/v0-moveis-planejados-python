"""
Configuração do banco de dados para a API FastAPI.

Este arquivo configura a conexão com o banco de dados SQLite
usando SQLAlchemy, reutilizando o mesmo banco de dados do Django.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Usando o mesmo banco de dados do Django para evitar duplicação de dados
# IMPORTANTE: Em produção, considere usar um banco de dados mais robusto como PostgreSQL
DATABASE_URL = f"sqlite:///{os.path.join(os.path.dirname(os.path.dirname(__file__)), 'db.sqlite3')}"

# Criação do engine SQLAlchemy
engine = create_engine(DATABASE_URL)

# Fábrica de sessões para criar sessões de banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base para modelos declarativos
Base = declarative_base()
