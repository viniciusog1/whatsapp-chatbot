def termos_de_uso_menu(client, twilio_number, from_number):
    # Para botões interativos no WhatsApp, use o parâmetro 'body' com texto simples
    # O Twilio WhatsApp Business API requer aprovação para templates interativos
    client.messages.create(
        from_=twilio_number,
        to=from_number,
        body="🤖 *Bem-vindo ao nosso chatbot!*\n\n"
             "Antes de continuar, você concorda com nossos termos de uso?\n\n"
             "Digite:\n"
             "• *concordo* - para aceitar\n"
             "• *não concordo* - para recusar"
    )

def menu_principal(client, twilio_number, from_number):
    # Menu usando texto formatado já que listas interativas requerem aprovação
    client.messages.create(
        from_=twilio_number,
        to=from_number,
        body="🏪 *MENU PRINCIPAL*\n"
             "Selecione uma das opções digitando o número:\n\n"
             "*1* - Promoções Retornáveis ✨\n"
             "*2* - Loja Virtual 🛍️\n"  
             "*3* - Ajuda e Suporte 🤝\n"
             "*4* - Trabalhe Conosco 👨‍💻\n"
             "*5* - Informações ℹ️\n"
             "*6* - Reclamações ⚠️\n"
             "*7* - Deixar Opinião ✍️\n\n"
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