"""
Configuração de URLs do projeto Móveis Planejados.

Este arquivo define os padrões de URL para o projeto inteiro, incluindo:
- URLs administrativas
- URLs da aplicação principal (website)
- URLs da API
- Configuração para servir arquivos de mídia em desenvolvimento
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Interface de administração do Django
    path('admin/', admin.site.urls),
    
    # URLs da aplicação principal (website)
    path('', include('website.urls')),
    
    # URLs da API FastAPI
    path('api/', include('api.urls')),
    
# Configuração para servir arquivos de mídia em ambiente de desenvolvimento
# IMPORTANTE: Em produção, os arquivos de mídia devem ser servidos por um servidor web como Nginx
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
