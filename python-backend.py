from flask import Flask, request, Response
from twilio.rest import TwilioRestClient
from twilio import twiml
 
app = Flask(__name__)
 
account = 'AC1ea915e8d2fb79d9efd01c53b94cdc75'
token   = 'c72fde4d7af307c610aaa0e5f3c3c9e2'
client  = TwilioRestClient(account, token)
 
@app.route("/")
def base():
    call = client.calls.create(to='+447729837696',
                               from_='+441543624251',
                               url='http://logomache.in:5000/xml?username=%s' %
                                    request.args['username'])
    return ''
 
@app.route("/xml", methods=['POST'])
def xml():
    r = twiml.Response()
    r.say("Yo! Can you let %s in, please?" % request.args['username'].lower(),
          voice='woman', language='en-gb')
    r.dial(callerId='+447729837696')
 
    return Response(str(r), mimetype='text/xml')
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
