# Móveis Planejados - Aplicação Web

Esta é uma aplicação web para uma empresa de móveis planejados, desenvolvida com Python, Django e FastAPI.

## Características

- Página institucional com efeito parallax
- Catálogo de produtos com filtros
- Sistema de categorias e produtos
- Formulário de contato
- API REST com FastAPI

## Requisitos

- Python 3.8+
- Django 4.2+
- FastAPI 0.104+
- SQLAlchemy 2.0+
- Pillow 10.1+

## Instalação

1. Clone o repositório:
\`\`\`bash
git clone https://github.com/seu-usuario/moveis-planejados.git
cd moveis-planejados
\`\`\`

2. Crie um ambiente virtual e ative-o:
\`\`\`bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
\`\`\`

3. Instale as dependências:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

4. Execute as migrações:
\`\`\`bash
python manage.py migrate
\`\`\`

5. Crie um superusuário:
\`\`\`bash
python manage.py createsuperuser
\`\`\`

6. Execute o servidor:
\`\`\`bash
python manage.py runserver
\`\`\`

7. Acesse a aplicação em http://localhost:8000

## Estrutura do Projeto

- `moveis_planejados/`: Configurações do projeto Django
- `website/`: Aplicação principal com views, models e templates
- `api/`: API FastAPI integrada ao Django
- `static/`: Arquivos estáticos (CSS, JS, imagens)
- `templates/`: Templates HTML
- `media/`: Arquivos de mídia enviados pelos usuários

## Licença

Este projeto está licenciado sob a licença MIT.
\`\`\`

Vamos revisar o arquivo CSS:
