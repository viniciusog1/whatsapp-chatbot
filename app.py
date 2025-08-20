from flask import Flask, request
from bot.handlers import handle_message

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    user_message = request.form.get("Body")
    from_number = request.form.get("From")  # número do usuário
    handle_message(user_message, from_number)
    return "ok"  # sempre responder 200 ao Twilio

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
