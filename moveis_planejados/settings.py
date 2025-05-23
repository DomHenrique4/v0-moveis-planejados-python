"""
Configurações do projeto Django para a aplicação de Móveis Planejados.

Este arquivo contém todas as configurações do Django, incluindo:
- Configurações de segurança
- Aplicações instaladas
- Middleware
- Banco de dados
- Internacionalização
- Arquivos estáticos e de mídia

Para mais informações sobre este arquivo, consulte:
https://docs.djangoproject.com/en/4.2/topics/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Define o diretório base do projeto para referência de caminhos relativos
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# IMPORTANTE: Em produção, esta chave deve ser armazenada em variáveis de ambiente
SECRET_KEY = 'django-insecure-h7d3f8j2k4l5m6n7o8p9q0r1s2t3u4v5'

# SECURITY WARNING: don't run with debug turned on in production!
# Em ambiente de produção, DEBUG deve ser definido como False
DEBUG = True

# Lista de hosts permitidos para acessar a aplicação
# Em produção, adicione os domínios específicos aqui
ALLOWED_HOSTS = []

# Application definition
# Lista de aplicações Django instaladas no projeto
INSTALLED_APPS = [
    # Aplicações padrão do Django
    'django.contrib.admin',  # Interface de administração
    'django.contrib.auth',   # Sistema de autenticação
    'django.contrib.contenttypes',  # Framework de tipos de conteúdo
    'django.contrib.sessions',  # Framework de sessões
    'django.contrib.messages',  # Framework de mensagens
    'django.contrib.staticfiles',  # Gerenciamento de arquivos estáticos
    
    # Aplicações personalizadas
    'website',  # Nossa aplicação principal para o site de móveis planejados
]

# Middleware - componentes que processam requisições/respostas
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Segurança
    'django.contrib.sessions.middleware.SessionMiddleware',  # Gerenciamento de sessões
    'django.middleware.common.CommonMiddleware',  # Funcionalidades comuns
    'django.middleware.csrf.CsrfViewMiddleware',  # Proteção contra CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Autenticação
    'django.contrib.messages.middleware.MessageMiddleware',  # Sistema de mensagens
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Proteção contra clickjacking
]

# Configuração de URLs raiz
ROOT_URLCONF = 'moveis_planejados.urls'

# Configuração de templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Diretório de templates personalizado
        'APP_DIRS': True,  # Buscar templates nas aplicações
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuração WSGI para deploy
WSGI_APPLICATION = 'moveis_planejados.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# Configuração do banco de dados (SQLite para desenvolvimento)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
# Validadores de senha para aumentar a segurança
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
# Configurações de internacionalização
LANGUAGE_CODE = 'pt-br'  # Idioma padrão: Português do Brasil
TIME_ZONE = 'America/Sao_Paulo'  # Fuso horário: São Paulo
USE_I18N = True  # Ativar internacionalização
USE_TZ = True  # Ativar suporte a fuso horário

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
# Configuração de arquivos estáticos
STATIC_URL = 'static/'  # URL para arquivos estáticos
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # Diretórios de arquivos estáticos
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Diretório para collectstatic

# Media files
# Configuração para arquivos de mídia (uploads de usuários)
MEDIA_URL = '/media/'  # URL para arquivos de mídia
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Diretório para armazenar arquivos de mídia

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Tipo padrão para chaves primárias
