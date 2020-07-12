from flask import Flask, render_template,request
from webscrap import web_scraping
from advanceBOT import chat

app = Flask(__name__)


@app.route('/')  
def home():  
    return render_template("index.html")

@app.route("/get")
def get_resp():
    userText = request.args.get('msg')
    chat_output = chat(userText)

    if chat_output==" Sorry, Can't Find":
        return str(web_scraping(userText))
    else:
        return str(chat(userText))

if __name__ =='__main__':  
    app.run(debug = True)