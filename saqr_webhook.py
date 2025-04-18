
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def reply_whatsapp():
    incoming_msg = request.values.get("Body", "").lower()
    resp = MessagingResponse()
    msg = resp.message()

    reply_text = "هلا! معك صقر، السكرتير التنفيذي لعبدالمحسن الحرفش. شرايك نبدأ؟"
    msg.body(reply_text)
    
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
