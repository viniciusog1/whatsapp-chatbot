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
                 f"{CATALOGO_URL}\n"
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
                 f"{CATALOGO_URL}\n"
                 "Digite *menu* para voltar."
        )

    elif text in ["2", "redes sociais"]:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="🌎 *REDES SOCIAIS — SCHIPPER*\n\n"
                 "Siga a Schipper nas redes sociais!\n"
                 "🟧 *Instagram:* https://www.instagram.com/schipperbrasil/\n\n"
                 "🟦 *Facebook:* https://www.facebook.com/schipperbrasil\n\n"
                 "🟥 *YouTube:* https://www.youtube.com/user/schipperbrasil\n\n"
                 "⬛ *LinkedIn:* https://www.linkedin.com/company/schipperbrasil/\n\n"
                 "Digite *menu* para voltar."
        )

    elif text in ["3", "site"]:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="🌐 *CONFIRA NOSSO SITE*\n\n"
                 "Site da Schipper!\n"
                 "https://schipperbrasil.com.br/\n"
                 "Digite *menu* para voltar."
        )

    elif text in ["4", "pratos", "travessas"]:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="🍽️ *PRATOS E TRAVESSAS SCHIPPER*\n\n"
                 "Coleções em porcelana e cerâmica:\n"
                 "• Bonna 🇹🇷\n"
                 "• Porto Brasil 🇧🇷\n\n"
                 "Digite *menu* para voltar."
        )

    elif text in ["5", "panelas", "utensilios"]:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="🍲 *PANELAS E UTENSÍLIOS SCHIPPER*\n\n"
                 "Linha profissional e doméstica de alta qualidade:\n"
                 "• Tramontina 🇧🇷\n"
                 "• WMF (Alemanha) 🇩🇪\n\n"
                 "Digite *menu* para voltar."
        )

    elif text in ["6", "fornecedores", "marcas"]:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="🏷️ *PRINCIPAIS FORNECEDORES SCHIPPER*\n\n"
                 "• Tramontina 🇧🇷\n"
                 "• Bonna 🇹🇷\n"
                 "• WMF 🇩🇪\n"
                 "• Porto Brasil 🇧🇷\n\n"
                 "Digite *menu* para voltar."
        )

    elif text in ["7", "ajuda", "suporte"]:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="🤝 *SUPORTE SCHIPPER*\n\n"
                 "📞 Telefone: (61) 3251-8000\n"
                 "📧 Email: sac@schipperbrasil.com.br\n"
                 "Digite *menu* para voltar."
        )

    else:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="❓ Não entendi sua mensagem.\n\n"
                 "Digite *menu* para acessar as opções ou *catalogo* para receber o PDF."
        )
