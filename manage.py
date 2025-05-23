#!/usr/bin/env python
"""
Utilitário de linha de comando do Django para tarefas administrativas.

Este arquivo é o ponto de entrada para comandos administrativos do Django,
como runserver, makemigrations, migrate, etc.
"""
import os
import sys


def main():
    """
    Função principal que executa tarefas administrativas.
    
    Configura o ambiente e executa o comando Django especificado.
    """
    # Define o módulo de configurações do Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moveis_planejados.settings')
    try:
        # Importa a função de execução de comandos do Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Mensagem de erro amigável se o Django não estiver instalado
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Executa o comando especificado na linha de comando
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # Executa a função principal se este arquivo for executado diretamente
    main()
