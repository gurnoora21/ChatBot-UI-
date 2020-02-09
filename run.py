from flask import Flask, render_template
import os
from flask_socketio import SocketIO, send, emit
from form import Userinput
import json
import requests

app = Flask(__name__)
app.config['SECRET_KEY']= "NFJDKSBFJKSAD"

class config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
socketio = SocketIO(app)



@app.route("/")
@app.route("/home")
def home():
    form = Userinput()


    return render_template('home.html', form=form)base_url = "http://api.leapos.ca/obp/v4.0.0/banks/15fa44fc932d4b4cae9d2f28ec7b5cf/balances"
    API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyIiOiIifQ.De81eP_3gmHmmxJmRA92knXWiVqTGls2RLHc6Swh4Ic"
    headers = {
        'Authorization': 'DirectLogin token=%s' %(API_KEY)
    }

    r = requests.get(base_url, headers=headers)
    print("CONTENT \n", r.content)
    print("HEADER \n", r.headers)
    print("STATUS \n", r.status_code)

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

# RECEIVE MESSAGE
@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)









if __name__ == "__main__":
    app.run(debug=True)