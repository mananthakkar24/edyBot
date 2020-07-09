from flask import Flask, render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer as cbt
from chatterbot_corpus import *
app = Flask(__name__) #creating the Flask class object 
eb = ChatBot("Chatterbot",storage_adapter="chatterbot.storage.SQLStorageAdapter")  
trainer = cbt(eb)
trainer.train("chatterbot.corpus.english")
trainer.train("data/data.yml")

@app.route('/') #decorator drfines the   
def home():  
    return render_template("index.html")  

@app.route("/get")
def get_resp():
    userText = request.args.get('msg')
    return str(eb.get_response(userText))
  
if __name__ =='__main__':  
    app.run(debug = True)  