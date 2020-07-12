from flask import Flask, render_template,request
from webscrap import web_scraping
from advanceBOT import chat, articleFunction

app = Flask(__name__)


@app.route('/')  
def home():  
    return render_template("index.html")

@app.route("/get")
def get_resp():
    userURL = request.args.get('userURL')
    userText = request.args.get('msg')
    #print(userURL)
    if userURL == "":
        sentence_list = articleFunction("https://www.who.int/emergencies/diseases/novel-coronavirus-2019/question-and-answers-hub/q-a-detail/q-a-coronaviruses#:~:text=symptoms")
    else:
        sentence_list = articleFunction(userURL)
    
    #print(userText)
    chat_output = chat(userText,sentence_list)

    if chat_output==" Sorry, Can't Find":
        return str(web_scraping(userText))
    else:
        return str(chat(userText,sentence_list))

if __name__ =='__main__':  
    app.run(debug = True)