"""
Configuração de URLs para a API FastAPI.

Este arquivo integra a API FastAPI com o Django, permitindo
que a API seja acessada através das URLs do Django.
"""

from django.urls import path
from django.http import HttpResponse
from fastapi.middleware.wsgi import WSGIMiddleware
from .main import app

def fastapi_view(request):
    """
    View Django que encaminha requisições para a aplicação FastAPI.
    
    Esta função permite que a API FastAPI seja acessada através das URLs do Django.
    
    Args:
        request: Objeto HttpRequest do Django
        
    Returns:
        HttpResponse contendo a resposta da API FastAPI
    """
    # Converte a requisição Django para WSGI e passa para o FastAPI
    return HttpResponse(WSGIMiddleware(app)(request._request))

urlpatterns = [
    # Todas as requisições para /api/ são encaminhadas para a aplicação FastAPI
    path('', fastapi_view, name='api-root'),
]
