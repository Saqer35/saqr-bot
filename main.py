from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get("Body", "").strip().lower()
    resp = MessagingResponse()
    msg = resp.message()

    msg.body("هلا! معك صقر، السكرتير التنفيذي لعبدالمحسن الحرفش. شرايك نبدأ؟")
    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)