from flask import Flask , request
from modules.greet import *
import telepot
import os
import sys
from telepot.loop import MessageLoop

app = Flask(__name__)

TOKEN = sys.argv[1]
PORT = int(sys.argv[2])
URL =  os.environ['URL']

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id,"Yo")


bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/work',methods=['POST','GET'])
def work():
    handle(request.data)
    return "Ok"

if __name__ == '__main__':
    app.run(port = PORT , debug = True)
