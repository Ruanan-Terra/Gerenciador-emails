from pathlib import Path
import streamlit as st

from utilidades import *
from paginas_templates import *
from paginas_configuracoes import *

def lista_emails():
    st.markdown('# Lista de Emails')
    st.divider()
    for arquivo in PASTA_LISTA_EMAIL.glob('*.txt'):
        nome_arquivo = arquivo.stem.replace('_', " ").upper()
        col1, col2, col3 = st.columns([0.6, 0.2, 0.2])
        col1.button(nome_arquivo, 
                    key = f'{nome_arquivo}', 
                    use_container_width = True,
                    on_click=_usar_lista,
                    args = (nome_arquivo,))

        col2.button('EDITAR', 
                    key = f'editar_{nome_arquivo}', 
                    use_container_width = True,
                    on_click = editar_lista,
                    args = (nome_arquivo,))
        
        col3.button('REMOVER', 
                    key = f'remover_{nome_arquivo}', 
                    use_container_width = True, 
                    on_click = remove_lista, 
                    args = (nome_arquivo,))
    st.divider()
    st.button('Adicionar lista de emails', on_click= mudar_pagina, args = ('adiconar_nova_lista',))

def pag_adiconar_nova_lista(nome_lista = '', texto_lista = ''):
    nome_lista = st.text_input('Nome da lista:', value = nome_lista)
    emails_lista = st.text_area('Escreva os emails separados por virgula:', value = texto_lista, height=600)
    st.button('Salvar', on_click = _salvar_lista, args = (nome_lista, emails_lista))

def _usar_lista(nome):
    nome_arquivo = str(nome).replace(' ', '_').lower() + ".txt"
    with open(PASTA_LISTA_EMAIL/nome_arquivo, 'r') as f:
        texto_arquivo = f.read()
    st.session_state.destinatarios_atual = texto_arquivo
    mudar_pagina('home')

def _salvar_lista(nome, texto):
    PASTA_LISTA_EMAIL.mkdir(exist_ok = True)
    nome_arquivo = str(nome).replace(' ', '_').lower() + ".txt"
    with open(PASTA_LISTA_EMAIL/nome_arquivo, 'w') as f:
        f.write(texto)
    mudar_pagina('lista_emails')

def remove_lista(nome):
    nome_arquivo = str(nome).replace(' ', '_').lower() + ".txt"
    (PASTA_LISTA_EMAIL/nome_arquivo).unlink()

def editar_lista(nome):
    nome_arquivo = str(nome).replace(' ', '_').lower() + ".txt"
    with open(PASTA_LISTA_EMAIL/nome_arquivo, 'r') as f:
        texto_arquivo = f.read()
    st.session_state.nome_lista_editar = nome
    st.session_state.texto_lista_editar = texto_arquivo
    mudar_pagina('editar_lista_email')
