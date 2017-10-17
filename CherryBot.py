import telepot , random
from Queue import Queue
from flask import Flask , request
from modules.greet import *
from modules.jokes import *
from modules.feedback import *
from modules.url import *
from modules.news import *
from modules.wiki import *
from modules.quotes import *
from telepot.namedtuple import *
import os


app = Flask(__name__)


def handle(msg):
    print(msg)
    txt = msg.text.split(' ',1)
    fin_resp = ''
    if txt[0] == '/start':
        fin_resp = welcome()
    elif txt[0] == '/jokes':
        fin_resp = get_jokes()
    elif txt[0] == '/bugs':
        if len(txt) != 1:
            bug(txt[1])
            bot.sendMessage(chat_id=447553922, text=txt[1])
            fin_resp="Thanks for the help"
        else:
            fin_resp = "Please use following format\n/bugs Bug-Issue"
    elif txt[0] == '/suggestions':
        if(len(txt) != 1):
            suggestions(txt[1])
            bot.sendMessage(chat_id=447553922, text=txt[1])
            fin_resp = "Thanks for the input"
        else:
            fin_resp= "Please use following format\n/suggestions Yout-Suggestion"
    elif txt[0] == '/memes':
        resp = get_memes()
        if resp=="done":
            file = open("meme.jpg", 'rb')
            bot.sendPhoto(msg.chat.id, file)
            file.close()
    elif txt[0] == '/bugdata':
        fin_resp = getBugData()
    elif txt[0] == '/sugdata':
        fin_resp= getSuggestionData()
    elif txt[0] == '/short':
        if len(txt) != 1:
            fin_resp= "Shortened URL : "+shorten_url(txt[1])
        else:
            fin_resp= "Please use following format\n/short LONGURL"
    elif txt[0] == '/news':
        fin_resp= get_news()
        for i in range(3):
            bot.sendMessage(msg.chat.id, fin_resp[i])
        keyboardNews = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='More News', callback_data="morenews")]
        ])
        bot.sendMessage(msg.chat.id, 'Load More', reply_markup=keyboardNews)
        fin_resp = "Press Above To Load More News"
    elif txt[0] == '/wiki':
        if len(txt) != 1:
            fin_resp=get_wiki(txt[1])
        else:
            fin_resp = "Please use following format\n/wiki Query"
    elif txt[0] == '/quotes':
        fin_resp = get_quotes()
    bot.sendMessage(chat_id=msg.chat.id, text=fin_resp)
    return "Ok"


def callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    if query_data == "morenews":
        bot.answerCallbackQuery(query_id, text='Loading More News')
        response = get_news()
        bot.sendMessage(from_id, random.choice(response).text)

        keyboardNews = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='More News', callback_data="norenews")]
        ])
        bot.sendMessage(from_id, 'Load More', reply_markup=keyboardNews)


TOKEN = os.environ['TOKEN']#"452803545:AAGRrJpayYMIHqam7F9fXV7bnYR4TvfDe88" #
URL = os.environ['URL']
bot = telepot.Bot(token=TOKEN)

inc_upd_queue = Queue() #queue to handle all incoming updates
bot.message_loop({'chat': handle, 'callback_query': callback_query}, source=inc_upd_queue)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/work',methods=['POST','GET'])
def work():
    if request.method == 'POST':
        inc_upd_queue.put(request.data)
    return "Ok"


if __name__ == '__main__':
    bot.setWebhook(URL)
    app.run(host='0.0.0.0' , debug = True)
