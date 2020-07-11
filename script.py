from flask import Flask, render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer as cbt
from chatterbot_corpus import *
from webscrap import web_scraping
from advanceBOT import chat

app = Flask(__name__)
#eb = ChatBot("Chatterbot",storage_adapter="chatterbot.storage.SQLStorageAdapter")
#trainer = cbt(eb)
#trainer.train("chatterbot.corpus.english")
#trainer.train("data/data.yml")

@app.route('/')  
def home():  
    return render_template("index.html")

@app.route("/get")
def get_resp():
    userText = request.args.get('msg')
    chat_output = chat(userText)
    #return str(chat_output)
    if chat_output==" Sorry, Can't Find":
        return str(web_scraping(userText))
    else:
        return str(chat(userText))
    #return str(eb.get_response(userText))
if __name__ =='__main__':  
    app.run(debug = True)