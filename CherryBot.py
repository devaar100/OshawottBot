from flask import Flask , request
from modules.greet import *
from modules.jokes import *
from modules.feedback import *
from modules.url import *
import telegram
import os

app = Flask(__name__)

def handle(msg):
    print(msg)
    txt = msg.text.split(' ',1)
    if txt[0] == '/start':
        bot.sendMessage(chat_id=msg.chat.id, text = welcome())
    elif txt[0] == '/jokes':
        bot.sendMessage(chat_id=msg.chat.id, text = rand_jokes())
    elif txt[0] == '/bugs':
        if (len(txt)!=1):
            bug(txt[1])
            bot.sendMessage(chat_id=447553922, text=txt[1])
            bot.sendMessage(chat_id=msg.chat.id, text="Thanks for the help")
        else:
            bot.sendMessage(chat_id=msg.chat.id, text="Please use following format\n/bugs Bug-Issue")
    elif txt[0] == '/suggestions':
        if(len(txt)!=1):
            suggestions(txt[1])
            bot.sendMessage(chat_id=447553922, text=txt[1])
            bot.sendMessage(chat_id=msg.chat.id,text= "Thanks for the input")
        else:
            bot.sendMessage(chat_id=msg.chat.id,text= "Please use following format\n/suggestions Yout-Suggestion")
    elif txt[0] == '/memes':
        resp = rand_memes()
        if resp=="done":
            file = open("meme.jpg", 'rb')
            bot.sendPhoto(msg.chat.id, file)
            file.close()
    elif txt[0] == '/bugdata':
        bot.sendMessage(chat_id=msg.chat.id, text= getBugData())
    elif txt[0] == '/sugdata':
        bot.sendMessage(chat_id=msg.chat.id, text= getSuggestionData())
    elif txt[0] == '/short':
        if len(txt) != 1:
            bot.sendMessage(chat_id=msg.chat.id, text= "Shortened URL : "+shorten_url(txt[1]))
        else:
            bot.sendMessage(chat_id=msg.chat.id, text= "Please use following format\n/short LONGURL")
    return "Ok"


TOKEN = os.environ['TOKEN'] #"452803545:AAGRrJpayYMIHqam7F9fXV7bnYR4TvfDe88" #
URL = os.environ['URL']
bot = telegram.Bot(token=TOKEN)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/work',methods=['POST','GET'])
def work():
    if request.method == 'POST':
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        handle(update.message)
    return "Ok"


if __name__ == '__main__':
    bot.setWebhook(URL)
    app.run(host='0.0.0.0' , debug = True)
