import os
from flask import *
from flask import Flask,url_for
from wtforms import *
app = Flask(__name__)
app.SECRET_KEY = '?\xbf,\xb4\x8d\xa3"<\x9c\xb0@\x0f5\xab,w\xee\x8d$0\x13\x8b83'
from twilio.rest import TwilioRestClient
account = "ACf6e95480e5da0a5657925cae4de5e240"
token = "baea43633a77ee03e8a83616be56dd7f"
client = TwilioRestClient(account, token)

###################################
# Upload settings
###################################

###################################
# Forms
###################################
class TextForm(Form):
    tmessage = TextField('text_message', [validators.Length(min=4, max=254)])
    
    
UPLOADS_DEFAULT_DEST = '/home/dan/media'

@app.route('/', methods=['GET', 'POST'])
def home():
    tform = TextForm(request.form,csrf_enabled=False)
    out_mess = {} 
    if request.method == 'POST':
        out_mess['tform'] = request.form['tmessage']
        message = client.sms.messages.create(to="+12699086688", from_="+16167654790", body=out_mess["tform"])
        flash('Message sent')
        return render_template('base.html',tform=tform)    
    return render_template('base.html',tform=tform)

@app.route('/music', methods=['GET', 'POST'])
def music():
    return render_template('music.html')

@app.route('/movies', methods=['GET', 'POST'])
def movies():
    return render_template('movies.html')

@app.route('/photos', methods=['GET', 'POST'])
def photos():
    return render_template('photos.html')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
