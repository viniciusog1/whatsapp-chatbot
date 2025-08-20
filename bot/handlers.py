from twilio.twiml.messaging_response import MessagingResponse
from bot.menus import termos_de_uso_menu, menu_principal


def handle_message(user_message):
    resp = MessagingResponse()

    if user_message is None:
        resp.message("Erro: mensagem inválida.")
        return resp

    text = user_message.lower()

    if "oi" in text:
        msg = resp.message("Oi! Eu sou seu assistente virtual 😊")
        termos_de_uso_menu(msg)  # chama menu de aceite
    elif "concordo" in text:
        msg = resp.message("Obrigado por aceitar! Agora escolha uma opção:")
        menu_principal(msg)
    elif "não concordo" in text or "nao concordo" in text:
        resp.message("Sem problemas! Você pode sair a qualquer momento 👍")
    else:
        resp.message("Desculpe, não entendi. Digite 'oi' para começar.")

    return resp
