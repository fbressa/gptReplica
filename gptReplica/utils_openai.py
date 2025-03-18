import openai

# API OPENAI ================================================
def retorna_resposta_modelo(mensagens,
                            chave,
                             model="gpt-3.5-turbo-0125",
                            temperature=0.0,
                            stream=False):
    openai.api_key = chave
    response = openai.chat.completions.create(
        model=model,
        messages=mensagens,
        temperature=temperature,
        stream=stream
    )
    return response