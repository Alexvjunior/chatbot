import logging
import os

import openai
from dotenv import load_dotenv

import config

load_dotenv()
logging.basicConfig(level=logging.INFO)
openai.api_key = os.getenv("OPENAI_API_KEY")


def enviar_mensagem(
        mensagem: str,
        lista_mensagens: list = [],
) -> None:
    """
    Envia uma mensagem para o modelo de chat e retorna a resposta.

    Args:
        mensagem (str): A mensagem do usuário.
        lista_mensagens (list): Lista de mensagens de conversa.

    Returns:
        str: A resposta do modelo.
    """

    lista_mensagens.append(
        {"role": "user", "content": mensagem}
    )

    try:
        resposta = openai.ChatCompletion.create(
            model=config.MODELO,
            messages=[{"role": "user", "content": mensagem}],
            temperature=config.TEMPERATURE,
            max_tokens=config.MAX_TOKENS,
            top_p=config.TOP_P,
            frequency_penalty=config.FREQUENCY_PENALTY,
            presence_penalty=config.PRESENCE_PENALTY
        )
        return resposta["choices"][0]["message"]
    except Exception as e:
        logging.error(f"Erro ao chamar a API: {e}")
        return "Desculpe, ocorreu um erro na comunicação com o servidor."


if __name__ == "__main__":

    print("Olá, seja bem-vindo ao chatbot...")

    lista_mensagens = []
    while True:
        mensagem = input("Mensagem: ")
        if mensagem.lower() == "sair":
            print("Obrigado por conversar! Até logo.")
            break

        resposta = enviar_mensagem(mensagem, lista_mensagens)
        lista_mensagens.append(
            {"role": "system", "content": resposta['content']})
        print(f"Chatbot: {resposta['content']}")
