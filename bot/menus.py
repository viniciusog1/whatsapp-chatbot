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
    client.messages.create(
        from_=twilio_number,
        to=from_number,
        body="🏪 *MENU SCHIPPER*\n"
             "Selecione uma das opções digitando o número:\n\n"
             "*1* - Catálogo em PDF 📘\n"
             "*2* - Redes Sociais 🌎\n"
             "*3* - Site 🌐\n"
             "*4* - Ajuda e Suporte 🤝\n\n"
             "_Digite o número da opção desejada_"
    )
