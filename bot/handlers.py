import os
from twilio.rest import Client
from bot.menus import termos_de_uso_menu, menu_principal, menu_atendimento

# Config Twilio
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
twilio_number = "whatsapp:+14155238886"  # Número sandbox Twilio
client = Client(account_sid, auth_token)

CATALOGO_URL = "https://schipperbrasil.com.br/downloads/catalogo_schipper/Cat_Schipper_low.pdf"

def handle_message(user_message, from_number):
    if not user_message:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="⚠️ Erro: mensagem inválida."
        )
        return

    text = user_message.lower().strip()

    # Saudações iniciais
    if any(palavra in text for palavra in ["oi", "olá", "ola", "hello", "iniciar", "começar"]):
        termos_de_uso_menu(client, twilio_number, from_number)

    # Respostas dos botões interativos (IDs dos botões)
    elif text == "catalogo":
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body=f"📘 Aqui está nosso catálogo completo da Schipper:\n\n"
                 f"{CATALOGO_URL}\n\nDigite *menu* para voltar."
        )

    elif text == "redes":
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="🌎 *REDES SOCIAIS — SCHIPPER*\n\n"
                 "🟧 Instagram: https://instagram.com/schipperbrasil\n"
                 "🟦 Facebook: https://facebook.com/schipperbrasil\n"
                 "🟥 YouTube: https://youtube.com/@schipperbrasil\n"
                 "⬛ LinkedIn: https://linkedin.com/company/schipperbrasil\n\n"
                 "Digite *menu* para voltar."
        )

    elif text == "site":
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="🌐 *CONFIRA NOSSO SITE*\nhttps://schipperbrasil.com.br/\n\nDigite *menu* para voltar."
        )

    elif text == "atendimento":
        menu_atendimento(client, twilio_number, from_number)

    # Submenus de atendimento
    elif text == "devolucao":
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="📦 *DEVOLUÇÃO DE PRODUTOS*\n\n"
                 "Para solicitar uma devolução, entre em contato:\n"
                 "📞 *Telefone:* (11) 1234-5678\n"
                 "📧 *Email:* devolucoes@schipper.com.br\n\n"
                 "Digite *menu* para voltar."
        )

    elif text == "acompanhamento":
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="🔍 *ACOMPANHAMENTO DE DEVOLUÇÃO*\n\n"
                 "Para acompanhar sua devolução:\n"
                 "📞 *Telefone:* (11) 1234-5678\n"
                 "📧 *Email:* atendimento@schipper.com.br\n\n"
                 "Digite *menu* para voltar."
        )

    elif text == "garantia":
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="🛡️ *GARANTIA DE PRODUTOS*\n\n"
                 "Nossos produtos têm garantia de 12 meses.\n"
                 "Para acionar a garantia:\n"
                 "📞 *Telefone:* (11) 1234-5678\n"
                 "📧 *Email:* garantia@schipper.com.br\n\n"
                 "Digite *menu* para voltar."
        )

    # Menu principal
    elif "menu" in text:
        menu_principal(client, twilio_number, from_number)

    # Fallback
    else:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="❓ Não entendi sua mensagem.\n\nDigite *menu* para acessar as opções."
        )
