from flask import Flask, render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer as cbt
from chatterbot_corpus import *
from webscrap import web_scraping

app = Flask(__name__)
eb = ChatBot("Chatterbot",storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = cbt(eb)
#trainer.train("chatterbot.corpus.english")
trainer.train("data/data.yml")

@app.route('/')  
def home():  
    return render_template("index.html")

@app.route("/get")
def get_resp():
    userText = request.args.get('msg')
    if eb==Null
    #ea = web_scraping(userText)
    #return str(eb.get_response(userText))
    return str(web_scraping(userText))

if __name__ =='__main__':  
    app.run(debug = True)