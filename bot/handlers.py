import os
from twilio.rest import Client
from bot.menus import termos_de_uso_menu, menu_principal

# Config Twilio
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
twilio_number = "whatsapp:+14155238886"  # Número do sandbox do Twilio
client = Client(account_sid, auth_token)

def handle_message(user_message, from_number):
    if not user_message:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="Erro: mensagem inválida."
        )
        return

    text = user_message.lower()

    if "oi" in text:
        termos_de_uso_menu(client, twilio_number, from_number)

    elif "concordo" in text:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="Obrigado por aceitar! Agora escolha uma opção:"
        )
        menu_principal(client, twilio_number, from_number)

    elif "não concordo" in text or "nao concordo" in text:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="Sem problemas! Você pode sair a qualquer momento 👍"
        )

    else:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="Desculpe, não entendi. Digite 'oi' para começar."
        )
