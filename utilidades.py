from email.message import EmailMessage
import smtplib
import ssl
from pathlib import Path
import streamlit as st

PASTA_ATUAL = Path(__file__).parent
PASTA_TEMPLATES = PASTA_ATUAL / 'templates'
PASTA_LISTA_EMAIL = PASTA_ATUAL / 'lista_email'
PASTA_CONFIGURACOES = PASTA_ATUAL / 'configuracoes'

# if not 'pagina_central_emails' in st.session_state:
#     st.session_state.pagina_central_email = 'home'

def inicializacao():
    if 'pagina_central_emails' not in st.session_state:
        st.session_state.pagina_central_emails = 'home'
    if 'destinatarios_atual' not in st.session_state:
        st.session_state.destinatarios_atual = ''
    if 'titulo_atual' not in st.session_state:
        st.session_state.titulo_atual = ''
    if 'corpo_atual' not in st.session_state:
        st.session_state.corpo_atual = ''

def mudar_pagina(nome_pagina):
    st.session_state.pagina_central_emails = nome_pagina

def enviar_email(email_usuario, destinatario, titulo, corpo, senha_app):
    message_email = EmailMessage()
    message_email['From'] = email_usuario
    message_email['To'] = destinatario
    message_email['Subject'] = titulo

    message_email.set_content(corpo)

    safe = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = safe) as smtp:
        smtp.login(email_usuario, senha_app)
        smtp.sendmail(email_usuario, destinatario, message_email.as_string())
