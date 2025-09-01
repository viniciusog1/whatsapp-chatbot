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


# def menu_principal(client, twilio_number, from_number):
#     client.messages.create(
#         from_=twilio_number,
#         to=from_number,
#         body="🏪 *MENU SCHIPPER*\n"
#              "Selecione uma das opções digitando o número:\n\n"
#              "*1* - Catálogo em PDF 📘\n"
#              "*2* - Redes Sociais 🌎\n"
#              "*3* - Site 🌐\n"
#              "*4* - Solicitar Atendimento 🕵️‍♀️\n"
#              "*5* - Ajuda e Suporte 🤝\n\n"
#              "_Digite o número da opção desejada_"
#     )


def menu_principal(client, twilio_number, from_number):
    client.messages.create(
        from_=twilio_number,
        to=from_number,
        interactive={
            "type": "button",
            "body": {
                "text": "🏪 *MENU SCHIPPER*\n\nSelecione uma das opções abaixo:"
            },
            "action": {
                "buttons": [
                    {
                        "type": "reply",
                        "reply": {"id": "catalogo", "title": "📘 Catálogo em PDF"}
                    },
                    {
                        "type": "reply",
                        "reply": {"id": "redes", "title": "🌎 Redes Sociais"}
                    },
                    {
                        "type": "reply",
                        "reply": {"id": "site", "title": "🌐 Site"}
                    },
                    {
                        "type": "reply",
                        "reply": {"id": "atendimento", "title": "🕵️ Atendimento"}
                    }
                ]
            }
        }
    )

