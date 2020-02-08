from flask import Flask, render_template
import os
from flask_socketio import SocketIO, send, emit
from form import Userinput
import json

app = Flask(__name__)
app.config['SECRET_KEY']= "NFJDKSBFJKSAD"

class config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
socketio = SocketIO(app)




@app.route("/")
@app.route("/home")
def home():
    form = Userinput()
    return render_template('homepage.html', form=form)

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

# RECEIVE MESSAGE
@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)









if __name__ == "__main__":
    app.run(debug=True)