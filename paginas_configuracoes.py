from pathlib import Path
import streamlit as st

from utilidades import *
from paginas_templates import *
from paginas_lista_email import *

def configuracao():
    st.markdown('# Configurações')

    email = st.text_input('Adicione seu email:')
    st.button('Salvar', 
              key = 'salvar_email',
              on_click=_salvar_email,
              args = (email, ))
    
    chave = st.text_input('Digite a chave de email:')
    st.button('Salvar', key = 'salvar_chave',
              on_click= _salvar_chave,
              args = (chave,))

def _salvar_email(email):
    PASTA_CONFIGURACOES.mkdir(exist_ok = True)
    with open(PASTA_CONFIGURACOES/'email_usuario.txt', 'w') as f:
        f.write(email)
    
def _salvar_chave(chave):
    PASTA_CONFIGURACOES.mkdir(exist_ok = True)
    with open(PASTA_CONFIGURACOES/'chave_usuario.txt', 'w') as f:
        f.write(chave)

def _le_email_usuario():
    PASTA_CONFIGURACOES.mkdir(exist_ok = True)
    if (PASTA_CONFIGURACOES/'email_usuario.txt').exists():
        with open(PASTA_CONFIGURACOES/'email_usuario.txt', 'r') as f:
            return f.read()
    return ''

def _le_chave_usuario():
    PASTA_CONFIGURACOES.mkdir(exist_ok = True)
    if (PASTA_CONFIGURACOES/'chave_usuario.txt').exists():
        with open(PASTA_CONFIGURACOES/'chave_usuario.txt', 'r') as f:
            return f.read()
    return ''
