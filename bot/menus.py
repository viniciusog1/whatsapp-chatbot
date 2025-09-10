def termos_de_uso_menu(client, twilio_number, from_number):
    client.messages.create(
        from_=twilio_number,
        to=from_number,
        body="🤖 *Bem-vindo ao assistente virtual da Schipper!*\n\n"
             "Fornecemos produtos de alto padrão para hotéis, bares e restaurantes 🍽️\n"
             "Eleita, pelo 12º ano consecutivo, a melhor fornecedora de utensílios (A&B) para hotelaria do Brasil.\n"
             "Transforme sua cozinha com a excelência do universo Schipper"
             ",produtos de alta qualidade e design excepcional para momentos memoráveis.\n\n"
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
             "*4* - Solicitar Atendimento 🕵️‍♀️\n"
             "*5* - Ajuda e Suporte 🤝\n"
             "*6* - Conhecer a história da Schipper 📰\n"
             "*7* - Pesquisar uma referência 🔎\n\n"
             "_Digite o número da opção desejada_"
    )
