import telepot
try:
    from queue import Queue
except ImportError:
    from Queue import Queue
from flask import Flask , request
from modules.greet import *
from modules.jokes import *
from modules.feedback import *
from modules.url import *
from modules.news import *
from modules.wiki import *
from modules.quotes import *
from modules.media import *
from telepot.namedtuple import *
import os


app = Flask(__name__)


def handle(msg):
    print(msg)
    txt = msg['text'].split(' ',1)
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
            fin_resp= "Please use following format\n/suggestions Your-Suggestion"
    elif txt[0] == '/memes':
        resp = get_memes()
        if resp=="done":
            file = open("meme.jpg", 'rb')
            bot.sendPhoto(msg['chat']['id'], file)
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
            bot.sendMessage(msg['chat']['id'], fin_resp[i])
        keyboardNews = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='More News', callback_data="morenews")]
        ])
        bot.sendMessage(msg['chat']['id'],text="Click below for more", reply_markup=keyboardNews)
        fin_resp=''
    elif txt[0] == '/wiki':
        if len(txt) != 1:
            fin_resp=get_wiki(txt[1])
        else:
            fin_resp = "Please use following format\n/wiki Query"
    elif txt[0] == '/quotes':
        fin_resp = get_quotes()
    elif txt[0] == '/contact':
        if len(txt)!=1:
            bot.sendMessage(chat_id=447553922, text="Contact message from "+msg['from'].get('username')+" :\n"+txt[1])
            fin_resp = "You will be contacted soon"
        else:
            fin_resp = "No message provided"
    elif txt[0].lower() in ['hi','hello','hey']:
        fin_resp = "Hi "+msg['from'].get('username')+'\nLets have fun :D'
    elif txt[0].lower() in ['thanks','bye','love']:
        fin_resp = "Glad to be of help\n/rate to show your appreciation for the bot"
    elif txt[0] == '/rate':
        fin_resp = rate_msg
    elif txt[0] == '/song':
        if len(txt)!=1:
            fin_resp = find_song(txt[1])
            for i in fin_resp[:3]:
                bot.sendMessage(chat_id=msg['chat']['id'], text=i)

            keyboardMusic = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Download 1st option', callback_data=str(0)+" dwn_song")],
                [InlineKeyboardButton(text='Download 2nd option', callback_data=str(1)+" dwn_song")],
                [InlineKeyboardButton(text='Download 3rd option', callback_data=str(2)+" dwn_song")]
            ])
            bot.sendMessage(msg['chat']['id'],text='Select song to download', reply_markup=keyboardMusic)
        fin_resp=''
    else:
        fin_resp = "Please provide songname"
    if fin_resp != '':
        bot.sendMessage(chat_id=msg['chat']['id'], text=fin_resp)
    return "Ok"


def callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print(str(query_id)+" "+str(from_id)+" "+str(query_data))

    if query_data == "morenews":
        bot.answerCallbackQuery(callback_query_id=query_id, text='Loading More News')
        response = get_news()[2:]
        bot.sendMessage(from_id, random.choice(response))

        keyboardNews = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='More News', callback_data="morenews")]
        ])
        bot.sendMessage(chat_id= from_id ,text="Click below for more", reply_markup=keyboardNews)
    else:
        bot.answerCallbackQuery(callback_query_id=query_id, text="Donwloading your song")
        name = download_song(query_data.split(' ')[0])
        song = open(name,'rb')
        bot.sendAudio(chat_id= from_id, audio= song)
        song.close()


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
