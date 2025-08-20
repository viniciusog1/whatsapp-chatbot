def termos_de_uso_menu(msg):
    msg.payload({
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {"text": "Você concorda com nossos termos de uso?"},
            "action": {
                "buttons": [
                    {"type": "reply", "reply": {"id": "concordo", "title": "Concordo"}},
                    {"type": "reply", "reply": {"id": "nao_concordo", "title": "Não concordo"}}
                ]
            }
        }
    })

def menu_principal(msg):
    msg.payload({
        "type": "interactive",
        "interactive": {
            "type": "list",
            "header": {"type": "text", "text": "Escolha aqui"},
            "body": {"text": "Selecione uma das opções abaixo 👇"},
            "footer": {"text": "Assistente Virtual"},
            "action": {
                "button": "Ver opções",
                "sections": [
                    {
                        "title": "Menu Principal",
                        "rows": [
                            {"id": "promo", "title": "Promo Retornável ✨", "description": "Veja promoções"},
                            {"id": "loja", "title": "Loja 🛍️", "description": "Compre online"},
                            {"id": "ajuda", "title": "Ajuda 🤝", "description": "Suporte rápido"},
                            {"id": "trabalhar", "title": "Trabalhar 👨‍💻", "description": "Veja vagas disponíveis"},
                            {"id": "info", "title": "Informações ℹ️", "description": "Saiba mais"},
                            {"id": "reclamacao", "title": "Reclamação ⚠️", "description": "Abrir chamado"},
                            {"id": "opiniao", "title": "Opinião ✍️", "description": "Envie seu feedback"}
                        ]
                    }
                ]
            }
        }
    })
