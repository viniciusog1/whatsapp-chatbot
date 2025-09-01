def termos_de_uso_menu(client, twilio_number, from_number):
    client.messages.create(
        from_=twilio_number,
        to=from_number,
        body="🤖 *Bem-vindo ao assistente virtual da Schipper!*\n\n"
             "Fornecemos produtos de alto padrão para hotéis, bares e restaurantes 🍽️\n\n"
             "Antes de continuar, digite:\n"
             "• *catalogo* → para receber nosso catálogo em PDF\n"
             "• *menu* → para acessar nosso menu interativo"
    )


def menu_principal(client, twilio_number, from_number):
    try:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            content_sid=None,  # Importante para mensagens interativas
            interactive={
                "type": "button",
                "body": {
                    "text": "🏪 *MENU SCHIPPER*\n\nSelecione uma das opções abaixo:"
                },
                "action": {
                    "buttons": [
                        {
                            "type": "reply",
                            "reply": {"id": "catalogo", "title": "📘 Catálogo PDF"}
                        },
                        {
                            "type": "reply",
                            "reply": {"id": "redes", "title": "🌎 Redes Sociais"}
                        },
                        {
                            "type": "reply",
                            "reply": {"id": "site", "title": "🌐 Site"}
                        }
                    ]
                }
            }
        )

        # Segunda mensagem com mais botões (WhatsApp limita a 3 botões por mensagem)
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            interactive={
                "type": "button",
                "body": {
                    "text": "Mais opções:"
                },
                "action": {
                    "buttons": [
                        {
                            "type": "reply",
                            "reply": {"id": "atendimento", "title": "🕵️ Atendimento"}
                        }
                    ]
                }
            }
        )
    except Exception as e:
        # Fallback para texto simples se botões não funcionarem
        print(f"Erro ao enviar botões: {e}")
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="🏪 *MENU SCHIPPER*\n"
                 "Digite:\n\n"
                 "*catalogo* - Catálogo em PDF 📘\n"
                 "*redes* - Redes Sociais 🌎\n"
                 "*site* - Site 🌐\n"
                 "*atendimento* - Solicitar Atendimento 🕵️‍♀️"
        )


def menu_atendimento(client, twilio_number, from_number):
    try:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            interactive={
                "type": "button",
                "body": {
                    "text": "🕵️‍♀️ *ATENDIMENTO SCHIPPER*\n\nSelecione o tipo de atendimento:"
                },
                "action": {
                    "buttons": [
                        {
                            "type": "reply",
                            "reply": {"id": "devolucao", "title": "📦 Devolução"}
                        },
                        {
                            "type": "reply",
                            "reply": {"id": "acompanhamento", "title": "🔍 Acompanhamento"}
                        },
                        {
                            "type": "reply",
                            "reply": {"id": "garantia", "title": "🛡️ Garantia"}
                        }
                    ]
                }
            }
        )
    except Exception as e:
        # Fallback para texto simples
        print(f"Erro ao enviar botões de atendimento: {e}")
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="🕵️‍♀️ *ATENDIMENTO SCHIPPER*\n\n"
                 "Digite:\n"
                 "*devolucao* - Devolução\n"
                 "*acompanhamento* - Acompanhamento\n"
                 "*garantia* - Garantia de Produtos\n\n"
                 "Digite *menu* para voltar."
        )
