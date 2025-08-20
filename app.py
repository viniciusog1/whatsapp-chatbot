from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    user_message = request.form.get("Body")

    resp = MessagingResponse()
    msg = resp.message()

    if "oi" in user_message.lower():
        msg.body("Oi! 👋 Estou rodando na nuvem (Render).")
    elif "nome" in user_message.lower():
        msg.body("Sou um bot feito com Python, Twilio e Render.")
    else:
        msg.body("Desculpe, não entendi. Pode repetir?")

    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
