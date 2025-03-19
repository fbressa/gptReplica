# Bressa GPT

Bressa GPT é um chatbot interativo desenvolvido com **Streamlit** e integrado à API da OpenAI para fornecer respostas inteligentes e contextuais.

## 🚀 Funcionalidades
- Interface intuitiva para conversas dinâmicas.
- Integração com a API da OpenAI.
- Suporte a diferentes modelos de IA, como **GPT-3.5-Turbo** e **GPT-4**.
- Armazenamento local das conversas.
- Possibilidade de configurar a chave da API diretamente na interface.

## 🛠️ Tecnologias Utilizadas
- **Python**
- **Streamlit**
- **OpenAI API**
- **Unidecode**
- **Pickle** (para armazenamento de conversas)

## 📦 Instalação
Para rodar o projeto localmente, siga os passos abaixo:

1. Clone este repositório:
   ```sh
   git clone https://github.com/seu-usuario/gptReplica.git
   cd gptReplica
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

4. Execute a aplicação:
   ```sh
   streamlit run gpt.py
   ```
   ou
   ```sh
   python -m streamlit run gpt.py
   ```

## ⚙️ Configuração
Antes de iniciar o chat, adicione sua chave da API OpenAI na aba **Configurações** da interface.

## 📄 Estrutura do Projeto
```
/
├── gpt.py      # Arquivo principal do projeto
├── utils_openai.py            # Integração com a API da OpenAI
├── utils_files.py             # Gerenciamento de mensagens e configurações
├── requirements.txt           # Dependências do projeto
├── configuracoes/             # Pasta para armazenamento da chave da API
├── mensagens/                 # Pasta para armazenamento das conversas
```

## 🤝 Contribuição
Se quiser contribuir, fique à vontade para abrir um **pull request** ou relatar **issues**.

## 📜 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usá-lo e modificá-lo.

---

**Desenvolvido por [fbressa](https://github.com/fbressa)**

