import os
from twilio.rest import Client
from bot.menus import termos_de_uso_menu, menu_principal

# Config Twilio
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
twilio_number = "whatsapp:+14155238886"  # Número sandbox Twilio
client = Client(account_sid, auth_token)

# 🔹 URL do catálogo hospedado (suba em Render, S3, etc.)
CATALOGO_URL = "https://schipperbrasil.com.br/downloads/catalogo_schipper/Cat_Schipper_low.pdf"


def handle_message(user_message, from_number):
    # Mapeamento dinâmico de opções

    atendimento_opcoes = {
        "a1": "Devolução",
        "devolucao": "Devolução",
        "devolução": "Devolução",
        "a2": "Acompanhamento de Devolução",
        "acompanhamento": "Acompanhamento de Devolução",
        "a3": "Garantia de Produtos",
        "garantia": "Garantia de Produtos"
    }

    if not user_message:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="❌ Erro: mensagem inválida."
        )
        return

    text = user_message.lower().strip()

    # Saudações iniciais
    if any(palavra in text for palavra in ["oi", "olá", "ola", "hello", "iniciar", "começar"]):
        termos_de_uso_menu(client, twilio_number, from_number)

    # Catálogo direto
    elif "catalogo" in text:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body=f"📘 Aqui está nosso catálogo completo da Schipper:\n\n"
                 f"{CATALOGO_URL}\n\n"
                 "Digite *menu* para voltar."
        )

    # Menu principal
    elif "menu" in text:
        menu_principal(client, twilio_number, from_number)

    # Opções do menu
    elif text in ["1"]:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body=f"📘 Aqui está nosso catálogo completo da Schipper:\n\n"
                 f"{CATALOGO_URL}\n\n"
                 "Digite *menu* para voltar."
        )

    elif text in ["2", "redes sociais"]:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="🌎 *REDES SOCIAIS — SCHIPPER*\n\n"
                 "Siga a Schipper nas redes sociais!\n\n"
                 "🟧 *Instagram:* https://instagram.com/schipperbrasil\n\n"
                 "🟦 *Facebook:* https://facebook.com/schipperbrasil\n\n"
                 "🟥 *YouTube:* https://youtube.com/@schipperbrasil\n\n"
                 "⬛ *LinkedIn:* https://linkedin.com/company/schipperbrasil\n\n"
                 "Digite *menu* para voltar."
        )

    elif text in ["3", "site"]:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="🌐 *CONFIRA NOSSO SITE*\n\n"
                 "Site da Schipper!\n"
                 "https://schipperbrasil.com.br/\n\n"
                 "Digite *menu* para voltar."
        )

    elif text in ["4", "atendimento"]:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="🕵️‍♀️ *ATENDIMENTO SCHIPPER*\n\n"
                 "Digite o tipo de atendimento desejado\n\n"
                 "*A1* - Devolução \n"
                 "*A2* - Acompanhamento de Devolução\n"
                 "*A3* - Garantia de Produtos\n\n"
                 "Digite *menu* para voltar."
        )

    elif text in atendimento_opcoes:
        atendimento_escolhido = atendimento_opcoes[text]
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body=f"Tipo de atendimento solicitado: *{atendimento_escolhido}*\n\n"
                 "Digite *menu* para voltar."
        )

    else:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="❓ Não entendi sua mensagem.\n\n"
                 "Digite *menu* para acessar as opções ou *catalogo* para receber o PDF."
        )
