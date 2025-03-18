
import streamlit as st

from utils_openai import retorna_resposta_modelo
from utils_files import *

# INICIALIZAÇÃO ==================================================
def inicializacao():
    if not 'mensagens' in st.session_state:
        st.session_state.mensagens = []
    if not 'conversa_atual' in st.session_state:
        st.session_state.conversa_atual = ''
    if not 'modelo' in st.session_state:
        st.session_state.modelo = 'gpt-3.5-turbo-0125'
    if not 'chave' in st.session_state:
        st.session_state.chave = le_chave()

# TABS ==================================================
def tab_conversas(tab):
    tab.button('➕ Nova conversa',
              on_click=seleciona_conversa,
              args=('', ),
              use_container_width=True)
    
    tab.markdown('---')
    conversas = listar_conversas()

    for nome_arquivo in conversas:
        nome_mensagem = desconverte_nome_mensagem(nome_arquivo).capitalize()
        if len(nome_mensagem) > 30:
            nome_mensagem = nome_mensagem[:30] + '...'

        tab.button(nome_mensagem,
                    on_click=seleciona_conversa,
                    args=(nome_arquivo, ),
                    disabled=nome_arquivo == st.session_state['conversa_atual'],
                    use_container_width=True)
        
def seleciona_conversa(nome_arquivo):
    if nome_arquivo == '':
        st.session_state.mensagens = []
    else:
        mensagem = ler_mensagem_por_nome_arquivo(nome_arquivo)
        st.session_state.mensagens = mensagem
    st.session_state['conversa_atual'] = nome_arquivo

def tab_configuracoes(tab):
    modelo_escolhido = tab.selectbox('Selecione o Modelo',
                                     ['gpt-3.5-turbo-0125', 'gpt-4'])
    st.session_state['modelo'] = modelo_escolhido

    chave = tab.text_input('Chave da OpenAI',
                           type='password',
                           value=st.session_state['chave'])
    
    if chave != st.session_state['chave']:
        st.session_state['chave'] = chave
        salva_chave(chave)
        tab.success('Chave salva com sucesso!')

# PÁGINA PRINCIPAL ==================================================
def pagina_principal():

    mensagens = ler_mensagem(st.session_state['mensagens'])

    st.header("Bressa GPT v1.0", divider=True)

    for mensagem in mensagens:
        chat = st.chat_message(mensagem['role'])
        chat.markdown(mensagem['content'])
    
    prompt = st.chat_input('Fale com o chat')
    if prompt:
        if st.session_state['chave'] == '':
            st.error('Adicione a chave da OpenAI nas configurações')

        nova_mensagem = {'role': 'user',
                          'content': prompt}
        chat = st.chat_message(nova_mensagem['role'])
        chat.markdown(nova_mensagem['content'])
        mensagens.append(nova_mensagem)

        chat = st.chat_message('assistant')
        placeholder = chat.empty()
        placeholder.markdown('▌')
        resposta_completa = ''
        respostas = retorna_resposta_modelo(mensagens,
                                            st.session_state['chave'],
                                            model=st.session_state['modelo'],
                                            stream=True)
        
        for resposta in respostas:
            if resposta.choices[0].delta.content:  # Verifica se há conteúdo
                resposta_completa += resposta.choices[0].delta.content
                placeholder.markdown(resposta_completa + '▌')

        placeholder.markdown(resposta_completa)

        nova_mensagem = {'role': 'assistant',
                          'content': resposta_completa}
        
        mensagens.append(nova_mensagem)
        
        st.session_state['mensagens'] = mensagens
        salvar_mensagem(mensagens)

# MAIN ==================================================
def main():
    inicializacao()
    pagina_principal()
    tab1, tab2 = st.sidebar.tabs(['Conversas', 'Configurações'])
    tab_conversas(tab1)
    tab_configuracoes(tab2)

if __name__ == '__main__':
    main()