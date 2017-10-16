from flask import Flask , request
from modules.greet import *
from modules.jokes import *
import telegram

app = Flask(__name__)

def handle(msg):
    print msg
    txt = msg.text
    if txt == '/start':
        bot.sendMessage(chat_id=msg.chat.id, text = welcome())
    elif txt == '/jokes':
        bot.sendMessage(chat_id=msg.chat.id, text = rand_jokes())
    return "Ok"

bot = telegram.Bot(token='452803545:AAGRrJpayYMIHqam7F9fXV7bnYR4TvfDe88')

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/work',methods=['POST','GET'])
def work():
    if request.method == 'POST':
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        if update is None:
            return "Show me your TOKEN please!"
        handle(update.message)
    return "Ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0' , debug = True)
