import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import re
from nltk.stem.porter import PorterStemmer
import nltk
from nltk.tokenize import word_tokenize
import json

def word_by_word(wordbyword,url):
    dictionary={}
    for word in wordbyword:
        url_f = url+word
        response = requests.get(url_f)
        if response.status_code==200:
            data = response.text
            soup = BeautifulSoup(data, features='html.parser')
            try:
                tag = soup.find_all('div',{'class':'runseg'})
                if len(tag)>0:
                    txt = tag[0].text
                    dictionary[word] = txt
                else:
                    txt = tag.text           
                    dictionary[word] = txt
            except:
                pass
    return dictionary

def find_by_google(words,url):
    dictionary={}
    for word in words:
        url_f = url_google.format(word)
        response = requests.get(url_f)
        if response.status_code==200:
            try:
                get = json.loads(str(response.text))[0]
                definition = get['meanings'][0]['definitions'][0]['definition']
                dictionary[word] = definition
            except:
                dictionary[word] = ""     
    return dictionary

url1 = "https://medical-dictionary.thefreedictionary.com/"
url2 = "https://api.dictionaryapi.dev/api/v2/entries/en/{}"

def getdefs(service):
    definitions = word_by_word(service.split(),url1)
    if definitions == {}:
        definitions = find_by_google(service.split(),url2)

    return definitions

service_name = input()
print(getdefs(service_name))
