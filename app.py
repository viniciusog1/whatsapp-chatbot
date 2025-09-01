from flask import Flask, request, jsonify
from bot.handlers import handle_message
import json

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
# def whatsapp_reply():
#     user_message = request.form.get("Body")
#     from_number = request.form.get("From")  # número do usuário
#     handle_message(user_message, from_number)
#     return "ok"  # sempre responder 200 ao Twilio


def whatsapp_reply():
    try:
        # Processa tanto mensagens de texto quanto botões interativos
        user_message = request.form.get("Body")  # Mensagem de texto normal
        button_payload = request.form.get("ButtonPayload")  # ID do botão clicado
        from_number = request.form.get("From")

        # Se for um botão clicado, usa o ID do botão como mensagem
        if button_payload:
            user_message = button_payload

        print(f"Mensagem recebida: {user_message} de {from_number}")

        handle_message(user_message, from_number)

        return "ok", 200

    except Exception as e:
        print(f"Erro no webhook: {e}")
        return "error", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
