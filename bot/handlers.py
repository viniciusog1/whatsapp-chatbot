import os
from twilio.rest import Client
from bot.menus import termos_de_uso_menu, menu_principal
import pandas as pd
# from bot.db import db_connection   # nova conexão com Oracle

# Config Twilio
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
twilio_number = "whatsapp:+14155238886"  # Número sandbox Twilio
client = Client(account_sid, auth_token)

# 🔹 URL do catálogo hospedado (suba em Render, S3, etc.)
CATALOGO_URL = "https://schipperbrasil.com.br/downloads/catalogo_schipper/Cat_Schipper_low.pdf"


# API Oracle exposta via Ngrok
API_URL = "https://6482a4ff78e9.ngrok-free.app"   # coloque aqui seu endpoint Ngrok atual
API_KEY = "minha-chave-super-secreta-2024"        # sua chave de autenticação

# Estado de usuários
user_state = {}

# 🔹 Carregar base CSV em memória
df = pd.read_csv("base10-09.csv", dtype=str)   # força tudo como string
produtos = {row["codprod"]: row["descricao7"] for _, row in df.iterrows()}

def handle_message(user_message, from_number):
    # Mapeamento dinâmico de opções
    # ------------------------
    # DICIONÁRIO DE ATENDIMENTO
    # ------------------------
    atendimento_opcoes = {
        "a1": "Devolução",
        "devolucao": "Devolução",
        "devolução": "Devolução",
        "a2": "Acompanhamento de Devolução",
        "acompanhamento": "Acompanhamento de Devolução",
        "a3": "Garantia de Produtos",
        "garantia": "Garantia de Produtos"
    }

    if not user_message:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="❌ Erro: mensagem inválida."
        )
        return

    text = user_message.lower().strip()

    # ------------------------
    # ETAPA: PESQUISA DE REFERÊNCIA
    # ------------------------
    if user_state.get(from_number) == "pesquisa_ref":
        ref = text.upper()
        try:
            response = requests.get(
                f"{API_URL}/produto/{ref}",
                headers={"Authorization": f"Bearer {API_KEY}"}
            )

            if response.status_code == 200:
                data = response.json()
                resposta = f"🔎 Código do produto *{ref}* encontrada:\n\n📌 {data['descricao7']}"
            elif response.status_code == 404:
                resposta = f"❌ Não encontrei nenhum produto com a código do produto *{ref}*."
            else:
                resposta = f"⚠ Erro ao consultar API: {response.status_code} - {response.text}"

        except Exception as e:
            resposta = f"⚠ Erro ao acessar API: {e}"

        # limpar estado
        user_state[from_number] = None
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body=resposta + "\n\nDigite *menu* para voltar."
        )
        return

    # Saudações iniciais
    if any(palavra in text for palavra in ["oi", "olá", "ola", "hello", "iniciar", "começar"]):
        termos_de_uso_menu(client, twilio_number, from_number)

    # Catálogo direto
    elif "catalogo" in text:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body=f"📘 Aqui está nosso catálogo completo da Schipper:\n\n"
                 f"{CATALOGO_URL}\n\n"
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
                 f"{CATALOGO_URL}\n\n"
                 "Digite *menu* para voltar."
        )

    elif text in ["2", "redes sociais"]:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="🌎 *REDES SOCIAIS — SCHIPPER*\n\n"
                 "Siga a Schipper nas redes sociais!\n\n"
                 "🟧 *Instagram:* https://instagram.com/schipperbrasil\n\n"
                 "🟦 *Facebook:* https://facebook.com/schipperbrasil\n\n"
                 "🟥 *YouTube:* https://youtube.com/@schipperbrasil\n\n"
                 "⬛ *LinkedIn:* https://linkedin.com/company/schipperbrasil\n\n"
                 "Digite *menu* para voltar."
        )

    elif text in ["3", "site"]:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="🌐 *CONFIRA NOSSO SITE*\n\n"
                 "Site da Schipper!\n"
                 "https://schipperbrasil.com.br/\n\n"
                 "Digite *menu* para voltar."
        )

    elif text in ["4", "atendimento"]:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="🕵️‍♀️ *ATENDIMENTO SCHIPPER*\n\n"
                 "Digite o tipo de atendimento desejado\n\n"
                 "*A1* - Devolução \n"
                 "*A2* - Acompanhamento de Devolução\n"
                 "*A3* - Garantia de Produtos\n\n"
                 "Digite *menu* para voltar."
        )

    elif text in ["5", "suporte"]:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="🤝 *SUPORTE SCHIPPER*\n\n"
                 "📞 Telefone: (61) 3251-8000\n"
                 "📧 Email: sac@schipperbrasil.com.br\n\n"
                 "Digite *menu* para voltar."
        )

    elif text in ["6", "schipper"]:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="📰 *HISTÓRIA DA SCHIPPER*\n\n"
                 "Fundada pelo austríaco Gerfried Schipper em 1992"
                 " a empresa atua como consultora, importadora e "
                 "distribuidora de utensílios e equipamentos profissionais,"
                 " nacionais e importados, para Restaurantes, Bares, Hotéis,"
                 " Hospitais e similares. Com exclusividade em dezenas de marcas mundiais,"
                 " mais de 6 mil itens em estoque, entregas para todo o Brasil, equipes"
                 " altamente qualificadas, inovação constante e serviços eficientes, a"
                 " empresa hoje é líder em seu segmento, tendo sido eleita pelo 12º ano"
                 " consecutivo a melhor do Brasil.\n\n"
                 "Digite *menu* para voltar."
        )

    elif text in ["7", "referência", 'referencia']:
        user_state[from_number] = "pesquisa_ref"
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="🔎 *PESQUISAR REFERÊNCIA*\n\n"
                 "Digite a *referência* desejada para receber a descrição do produto.\n\n"
                 "Digite *menu* para voltar."
        )

    elif text in atendimento_opcoes:
        atendimento_escolhido = atendimento_opcoes[text]
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body=f"Tipo de atendimento solicitado: *{atendimento_escolhido}*\n\n"
                 "Sua solictação foi encaminhada para um profissional,"
                 "por favor, aguarde um instante, nosso profissional já vai atender sua solicitação.\n"
                 "Digite *menu* para voltar."
        )

    else:
        client.messages.create(
            from_=twilio_number,
            to=from_number,
            body="❓ Não entendi sua mensagem.\n\n"
                 "Digite *menu* para acessar as opções ou *catalogo* para receber o PDF."
        )
