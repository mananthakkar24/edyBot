import nltk
import warnings
warnings.filterwarnings("ignore")
# nltk.download() # for downloading packages
#import tensorflow as tf
import numpy as np
import random
import string # to process standard python strings

f=open('./data/nlp python answer finals.txt','r',errors = 'ignore')
m=open('./data/modules pythons.txt','r',errors = 'ignore')
checkpoint = "./chatbot_weights.ckpt"
#session = tf.InteractiveSession()
#session.run(tf.global_variables_initializer())
#saver = tf.train.Saver()
#saver.restore(session, checkpoint)

raw=f.read()
rawone=m.read()
raw=raw.lower()# converts to lowercase
rawone=rawone.lower()# converts to lowercase
#nltk.download('punkt') # first-time use only
#nltk.download('wordnet') # first-time use only
sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)# converts to list of words
sent_tokensone = nltk.sent_tokenize(rawone)# converts to list of sentences 
word_tokensone = nltk.word_tokenize(rawone)# converts to list of words


sent_tokens[:2]
sent_tokensone[:2]

word_tokens[:5]
word_tokensone[:5]

lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
#Introduce_Ans = ["My name is EdyBot.","My name is EdyBot you can call me Edy.","Im EdyBot :) ","My name is EdyBot. and my nickname is Edy and i am happy to solve your queries :) "]
GREETING_INPUTS = ("hello", "hi","hiii","hii","hiiii","hiiii", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["Hi", "Hey", "Hi there", "hi there", "hello"]
Basic_Q = ("what is NLP","what is Natural Language processing","what is Natural Language Processing?","tell me something about NLP")
Basic_Ans = "Natural language processing (NLP) is a subfield of linguistics, computer science, information engineering, and artificial intelligence concerned with the interactions between computers and human (natural) languages, in particular how to program computers to process and analyze large amounts of natural language data."
Basic_Om = ("who are you?" ,"what is your name" , "who are you")
Basic_AnsM = ["My name is EdyBot.","My name is EdyBot you can call me Edy.","I am EdyBot :) ","My name is EdyBot. and my nickname is Edy and i am happy to solve your queries :) "]
task = ("what can you do?","tell me something about yourself","what can you do")
taskans = "Edy can help you in knowing about Natural Language Processing , Tell me what are you looking for today?"
# Checking for greetings
def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# Checking for Basic_Q
def basic(sentence):
    for word in Basic_Q:
        if sentence.lower() == word:
            return Basic_Ans


# Checking for Basic_QM
def basicM(sentence):
    for word in Basic_Om:
        if sentence.lower() == word:
            return random.choice(Basic_AnsM)
    for word in task:
        if sentence.lower() == word:
            return taskans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Generating response
def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return (robo_response)
    else:
        robo_response = robo_response+sent_tokens[idx]
        return (robo_response)    
# Generating response
def responseone(user_response):
    robo_response=''
    sent_tokensone.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokensone)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return (robo_response)
    else:
        robo_response = robo_response+sent_tokensone[idx]
        return (robo_response)


def chat(user_response):
    user_response=user_response.lower()
    keyword = "module "
    keywordone = " module"
    keywordsecond = " module "
    
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' or user_response=='thanks edy' ):
            flag=False
            return( "My Pleasure!")
        
        else:
            if(user_response.find(keyword) != -1 or user_response.find(keywordone) != -1 or user_response.find(keywordsecond) != -1):
                return( responseone(user_response))
                sent_tokensone.remove(user_response)
            elif(greeting(user_response)!=None):
                return( greeting(user_response))
            
            elif(basic(user_response)!=None):
                return( basic(user_response))
            elif(basicM(user_response)!=None):
                return( basicM(user_response))  
            else:
                return( response(user_response))
                sent_tokens.remove(user_response)
                
    else:
        flag=False
        return("Bye! take care..")
chat("What is Python ?")