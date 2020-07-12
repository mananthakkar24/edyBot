from newspaper import Article
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
import string
import nltk
import numpy as np
import warnings
warnings.filterwarnings("ignore")

#nltk.download("punkt",quiet=True)

article = Article("https://www.niituniversity.in/why-nu")
article.download()
article.parse()
article.nlp()
corpus = article.text

#print(corpus)

text = corpus
sentence_list = nltk.sent_tokenize(text)

def greeting(text):
    text=text.lower()
    bot_greet = ["Hi","Hello","Hey","Namestey","Jai Shree Krishna"]
    user_greet = ["Hi","Hello","Hey","hi","hello","hey"]
    
    for word in text.split():
        if word in user_greet:
            return random.choice(bot_greet)

def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0,length))
    
    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
    return list_index

def bot_response(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_response = ''
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1],cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort(similarity_scores_list)
    index = index[1:]
    response_flag = 0
    
    j = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.2:
            bot_response = bot_response+' '+sentence_list[index[i]]
            response_flag = 1
            j = j+1
        if j > 2:
            break
    if response_flag == 0:
        bot_response = bot_response+' '+"Sorry, Can't Find"
        
    sentence_list.remove(user_input)
    
    return bot_response

exit_list = ['bye','thanks bye','quit','break','Bye']
fictional_list = ["chintu",'mintu',"chintu mintu"]

#while(True):
def chat(userText):
    user_input = userText
    if user_input.lower() in exit_list:
        return("Phir Miltey Hain, Alvida")
        #break
    elif user_input.lower() in fictional_list:
        return("Chintu Mintu are the fictional characters created by Manish Hurkat Sir for educational purposes")
    else:
        if greeting(user_input) != None:
            #print("edyBot: ",greeting(user_input))
            return greeting(user_input)
        else:
            #print("edyBot: ",bot_response(user_input))
            return bot_response(user_input)