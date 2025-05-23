"""
Formulários para a aplicação de Móveis Planejados.

Este arquivo define os formulários utilizados na aplicação,
incluindo o formulário de contato.
"""

from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
    """
    Formulário para envio de mensagens de contato.
    
    Baseado no modelo Contato, com widgets personalizados para
    melhorar a aparência e usabilidade do formulário.
    """
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'telefone', 'mensagem']
        
        # Personalização dos widgets para melhorar a aparência do formulário
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',  # Classes Bootstrap
                'placeholder': 'Seu nome'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Seu e-mail'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Seu telefone'
            }),
            'mensagem': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Sua mensagem',
                'rows': 5
            }),
        }
