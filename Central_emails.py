from pathlib import Path
import streamlit as st

from utilidades import *

from paginas_templates import templates, pag_novo_adicionar_novo_template
from paginas_lista_email import lista_emails, pag_adiconar_nova_lista
from paginas_configuracoes import configuracao, _le_email_usuario, _le_chave_usuario

if not 'pagina_central_emails' in st.session_state:
    st.session_state.pagina_central_email = 'home'

# ============================= HOME =============================
def home():
    destinatario_atual = st.session_state.destinatarios_atual
    titulo_atual = st.session_state.titulo_atual
    corpo_atual = st.session_state.corpo_atual

    st.markdown('# Central de Emails')
    destinatarios = st.text_input('Destinatários do email:', value = destinatario_atual)
    titulo = st.text_input('Titulo do email:', value = titulo_atual)
    corpo = st.text_area('Digite o email:', height = 400, value = corpo_atual)
    col1, col2, col3 = st.columns(3)

    col1.button('Enviar email', 
                use_container_width=True,
                on_click = _enviar_email,
                args = (destinatarios, titulo, corpo))
    col3.button('Limpar', use_container_width=True, on_click = _limpar)

    st.session_state.destinatarios_atual = destinatarios
    st.session_state.titulo_atual = titulo
    st.session_state.corpo_atual = corpo

def _limpar():
    st.session_state.destinatarios_atual = ''
    st.session_state.titulo_atual = ''
    st.session_state.corpo_atual = ''

def _enviar_email(destinatarios, titulo, corpo):
    destinatarios = destinatarios.replace(' ', '').spli(',')

    email_usuario = _le_email_usuario()
    chave = _le_chave_usuario()

    if email_usuario == '':
        st.error("Adicione um email na página de configurações")

    elif chave == '':
        st.error("Adicione uma chave de email na página de configurações")

    else:
        enviar_email(email_usuario,
                    destinatarios = destinatarios,
                    titulo = titulo,
                    corpo = corpo,
                    senha_app = chave)
# ============================= TEMPLATES =============================

def main():
    inicializacao()

    st.sidebar.button('Central de Emails', use_container_width = True, on_click = mudar_pagina, args = ('home',))
    st.sidebar.button('Templates', use_container_width = True, on_click = mudar_pagina, args = ('templates',))
    st.sidebar.button('Lista de Emails', use_container_width = True, on_click = mudar_pagina, args = ('lista_emails',))
    st.sidebar.button('Configuração', use_container_width = True, on_click = mudar_pagina, args = ('configuracao',))

    if st.session_state.pagina_central_emails == 'home':
        home()
    elif st.session_state.pagina_central_emails == 'templates':
        templates()
    elif st.session_state.pagina_central_emails == 'adiconar_novo_template':
        pag_novo_adicionar_novo_template()
    elif st.session_state.pagina_central_emails == 'editar_template':
        nome_template_editar = st.session_state.nome_template_editar
        texto_template_editar = st.session_state.texto_template_editar
        pag_novo_adicionar_novo_template(nome_template_editar, texto_template_editar)
    elif st.session_state.pagina_central_emails == 'lista_emails':
        lista_emails()
    elif st.session_state.pagina_central_emails == 'adiconar_nova_lista':
        pag_adiconar_nova_lista()   
    elif st.session_state.pagina_central_emails == 'editar_lista_email':
        nome_lista_editar = st.session_state.nome_lista_editar
        texto_lista_editar = st.session_state.texto_lista_editar
        pag_adiconar_nova_lista(nome_lista_editar, texto_lista_editar)
    elif st.session_state.pagina_central_emails == 'configuracao':
        configuracao()

main()