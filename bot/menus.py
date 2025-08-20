def termos_de_uso_menu(client, twilio_number, from_number):
    # Para botões interativos no WhatsApp, use o parâmetro 'body' com texto simples
    # O Twilio WhatsApp Business API requer aprovação para templates interativos
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
    # Menu usando texto formatado já que listas interativas requerem aprovação
    client.messages.create(
        from_=twilio_number,
        to=from_number,
        body="🏪 *MENU PRINCIPAL — SCHIPPER*\n"
             "Selecione uma das opções digitando o número:\n\n"
             "*1* - Catálogo em PDF ✨\n"
             "*2* - Fornecedores 🛍️\n"  
             "*3* - Ajuda e Suporte 🤝\n"
             "_Digite o número da opção desejada_"
    )

# Função alternativa usando templates aprovados (se você tiver)
def termos_de_uso_template(client, twilio_number, from_number):
    """
    Esta função só funcionará se você tiver templates aprovados pelo WhatsApp Business
    """
    try:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            content_sid='YOUR_APPROVED_TEMPLATE_SID',  # Substitua pelo SID do seu template
            content_variables={
                '1': 'Termos de Uso',
                '2': 'Concordo',
                '3': 'Não Concordo'
            }
        )
    except Exception as e:
        # Fallback para mensagem de texto simples
        termos_de_uso_menu(client, twilio_number, from_number)