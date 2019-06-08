from flask import Flask, request
from twilio.twiml.messaging_response import Body,Media,Message,MessagingResponse
from utils import fetch_reply

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    print(request.form)
    msg = request.form.get('Body')
    sender = request.form.get('From')

    # Create reply
    resp = MessagingResponse()
    m=fetch_reply(msg,sender)
    if(type(m)==list):
        for item in m :
            s="/n/n{}/n/n{}".format(item['title'],item['link'])
            resp.message(str(s))
        return str(resp)

        
    else:
        resp.message(m).media("https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwi4gp2HztniAhUKb30KHVnxCiUQjRx6BAgBEAU&url=https%3A%2F%2Fwww.frostfireaudio.com.au%2Ftv-film%2F&psig=AOvVaw0W-S0zb08Vhsy_rH429JKV&ust=1560073789502944")
        return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
