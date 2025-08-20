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
            body="📘 Aqui está nosso catálogo completo da Schipper:",
            media_url=CATALOGO_URL
        )

    # Menu principal
    elif "menu" in text:
        menu_principal(client, twilio_number, from_number)

    # Opções do menu
    elif text in ["1"]:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="📘 Aqui está nosso catálogo completo:",
            media_url=CATALOGO_URL
        )

    elif text in ["2", "talheres"]:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="🍴 *TALHERES SCHIPPER*\n\n"
                 "Trabalhamos com linhas completas de inox e prata:\n"
                 "• Tramontina 🇧🇷\n"
                 "• WMF (Alemanha) 🇩🇪\n\n"
                 "Digite *menu* para voltar."
        )

    elif text in ["3", "copos", "taças"]:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="🍷 *COPOS E TAÇAS SCHIPPER*\n\n"
                 "Opções em cristal, vidro e policarbonato.\n"
                 "Fornecedores:\n"
                 "• Schott Zwiesel 🇩🇪\n"
                 "• Nacionais variados 🇧🇷\n\n"
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
                 "📞 Telefone: (11) 3333-3333\n"
                 "📧 Email: suporte@schipper.com.br\n"
                 "Digite *menu* para voltar."
        )

    else:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="❓ Não entendi sua mensagem.\n\n"
                 "Digite *menu* para acessar as opções ou *catalogo* para receber o PDF."
        )
