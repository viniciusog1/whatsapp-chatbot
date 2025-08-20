from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from bot.handlers import handle_message

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    user_message = request.form.get("Body")
    response = handle_message(user_message)
    return str(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
