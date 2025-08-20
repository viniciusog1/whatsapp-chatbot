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
            body="❌ Erro: mensagem inválida."
        )
        return

    text = user_message.lower().strip()

    # Saudações iniciais
    if any(palavra in text for palavra in ["oi", "olá", "ola", "hello", "iniciar", "começar"]):
        termos_de_uso_menu(client, twilio_number, from_number)

    # Termos de uso
    elif "concordo" in text:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="✅ Obrigado por aceitar nossos termos!\n\n"
                 "Agora você pode acessar todos os recursos:"
        )
        menu_principal(client, twilio_number, from_number)

    elif "não concordo" in text or "nao concordo" in text:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="❌ Sem problemas! \n\n"
                 "Você pode retornar quando quiser digitando *oi*.\n"
                 "Tenha um ótimo dia! 👋"
        )

    # Opções do menu principal
    elif text in ["1", "promo", "promocao", "promoção"]:
        handle_promocoes(client, twilio_number, from_number)

    elif text in ["2", "loja", "comprar"]:
        handle_loja(client, twilio_number, from_number)

    elif text in ["3", "ajuda", "suporte", "help"]:
        handle_ajuda(client, twilio_number, from_number)

    elif text in ["4", "trabalhar", "vagas", "emprego"]:
        handle_trabalho(client, twilio_number, from_number)

    elif text in ["5", "info", "informações", "informacoes"]:
        handle_informacoes(client, twilio_number, from_number)

    elif text in ["6", "reclamacao", "reclamação", "problema"]:
        handle_reclamacao(client, twilio_number, from_number)

    elif text in ["7", "opiniao", "opinião", "feedback"]:
        handle_opiniao(client, twilio_number, from_number)

    elif text in ["menu", "voltar", "inicio"]:
        menu_principal(client, twilio_number, from_number)

    else:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="❓ Desculpe, não entendi sua mensagem.\n\n"
                 "Digite:\n"
                 "• *oi* - para começar\n"
                 "• *menu* - para ver as opções\n"
                 "• *ajuda* - para suporte"
        )


# Funções para cada opção do menu
def handle_promocoes(client, twilio_number, from_number):
    client.messages.create(
        from_=twilio_number,
        to=from_number,
        body="✨ *PROMOÇÕES ESPECIAIS*\n\n"
             "🔥 Confira nossas ofertas imperdíveis:\n\n"
             "• Produto A - 30% OFF\n"
             "• Produto B - Frete Grátis\n"
             "• Produto C - Leve 3 Pague 2\n\n"
             "Digite *menu* para voltar ou *loja* para comprar"
    )


def handle_loja(client, twilio_number, from_number):
    client.messages.create(
        from_=twilio_number,
        to=from_number,
        body="🛍️ *NOSSA LOJA VIRTUAL*\n\n"
             "Acesse nossa loja em:\n"
             "🔗 www.sualojaonline.com.br\n\n"
             "Ou fale com um consultor:\n"
             "📱 (11) 99999-9999\n\n"
             "Digite *menu* para voltar"
    )


def handle_ajuda(client, twilio_number, from_number):
    client.messages.create(
        from_=twilio_number,
        to=from_number,
        body="🤝 *CENTRAL DE AJUDA*\n\n"
             "Como posso te ajudar?\n\n"
             "• Dúvidas sobre produtos\n"
             "• Status do pedido\n"
             "• Trocas e devoluções\n"
             "• Suporte técnico\n\n"
             "📞 Atendimento: (11) 3333-3333\n"
             "📧 Email: suporte@empresa.com\n\n"
             "Digite *menu* para voltar"
    )


def handle_trabalho(client, twilio_number, from_number):
    client.messages.create(
        from_=twilio_number,
        to=from_number,
        body="👨‍💻 *TRABALHE CONOSCO*\n\n"
             "Vagas disponíveis:\n\n"
             "• Desenvolvedor Python\n"
             "• Analista de Marketing\n"
             "• Atendente de Chat\n\n"
             "📄 Envie seu currículo para:\n"
             "rh@empresa.com\n\n"
             "Digite *menu* para voltar"
    )


def handle_informacoes(client, twilio_number, from_number):
    client.messages.create(
        from_=twilio_number,
        to=from_number,
        body="ℹ️ *INFORMAÇÕES DA EMPRESA*\n\n"
             "🏢 Sobre nós:\n"
             "Empresa líder em soluções digitais\n\n"
             "📍 Endereço:\n"
             "Rua das Flores, 123 - São Paulo/SP\n\n"
             "🕒 Horário de funcionamento:\n"
             "Segunda a Sexta: 8h às 18h\n\n"
             "Digite *menu* para voltar"
    )


def handle_reclamacao(client, twilio_number, from_number):
    client.messages.create(
        from_=twilio_number,
        to=from_number,
        body="⚠️ *CANAL DE RECLAMAÇÕES*\n\n"
             "Lamentamos pelos problemas!\n\n"
             "Para abrir um chamado:\n"
             "📧 reclamacoes@empresa.com\n"
             "📱 WhatsApp: (11) 8888-8888\n\n"
             "Ou acesse:\n"
             "🔗 www.empresa.com.br/suporte\n\n"
             "Digite *menu* para voltar"
    )


def handle_opiniao(client, twilio_number, from_number):
    client.messages.create(
        from_=twilio_number,
        to=from_number,
        body="✍️ *SUA OPINIÃO É IMPORTANTE*\n\n"
             "Deixe seu feedback:\n\n"
             "📝 Formulário online:\n"
             "www.empresa.com.br/feedback\n\n"
             "⭐ Avalie-nos no Google:\n"
             "Link: bit.ly/avaliar-empresa\n\n"
             "📧 Email: feedback@empresa.com\n\n"
             "Digite *menu* para voltar"
    )