from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd
import spacy
import re
npl = spacy.load('en_core_web_lg')
from nltk.tokenize import sent_tokenize, word_tokenize
stopwords = npl.Defaults.stop_words
new_stop_words = ['ll', 've', 'heat', 'wave', 'heatwave']
stopwords.update(new_stop_words)
from sklearn.feature_extraction.text import CountVectorizer

def newsWebscrapping(link):
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req, timeout=20).read()
    bs = BeautifulSoup(webpage, 'html5lib')
    for item in bs.find_all('div', attrs={'class': 'Gx5Zad fP1Qef xpd EtOod pkphOe'}):
        raw_link = (item.find('a', href=True)['href'])
        link = (raw_link.split("/url?q=")[1]).split('&sa=U&')[0]
        title = (item.find('div', attrs={'class': 'BNeawe vvjwJb AP7Wnd'}).get_text())
        description = (item.find('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'}).get_text())
        #title = title.replace(",", "")
        #title = title.encode("utf-8")
        #title = re.sub(r'\W+', ' ', title)
        #description = description.replace(",", "")
        #description = re.sub(r'\W+', ' ', description)
        document = open("./dat/00_newsWebScrapping.csv", "a")
        document.write("{} \n".format(link))
        #document.write("{}, {}, {} \n".format(title, description, link))
        #document.write("{}, {} \n".format(title, link))
        document.close()
    next = bs.find('a', attrs={'aria-label':'Página siguiente'})
    if(next is not None):
        next = (next['href'])
        link2 = root + next
        newsWebscrapping(link2)



def cleaning_text1(text):
    cleantext = text.replace("\r", " ")
    cleantext = cleantext.replace("\n", " ")
    cleantext = cleantext.lower()
    cleantext = re.sub(r'\W+', ' ', cleantext)
    cleantext = re.sub(r'\d+', ' ', cleantext)
    cleantext = re.sub(r'\b[a-z]{1,2}\b', '', cleantext)
    cleantext = re.sub(r'\b[a-z]{20,200}\b', '', cleantext)
    cleantext =  ' '.join([word for word in cleantext.split() if word not in stopwords])
    doc = npl(cleantext)
    lemmas = [tok.lemma_.lower() for tok in doc]
    cleantext = " ".join(lemmas)
    cleantext = re.sub(r'\b[a-z]{1,2}\b', '', cleantext)
    cleantext = re.sub(r"\s{2,10}", " ", cleantext)
    return cleantext

def get_top_n_words(corpus, n=1,k=1):
    vec = CountVectorizer(ngram_range=(k,k), stop_words = stopwords).fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0) 
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
    return words_freq[:n]


def cleaning_text2(text):
    cleantext =  ' '.join([word for word in text.split() if word not in new_stop_words])
    cleantext = tokenizer.tokenize(cleantext)
    return cleantext

def cleaning_text3(text):
    cleantext = text.replace("\r", " ")
    cleantext = cleantext.replace("\n", " ")
    cleantext = cleantext.lower()
    cleantext = re.sub(r'\W+', ' ', cleantext)
    cleantext =  ' '.join([word for word in cleantext.split() if word not in stopwords])
    return cleantext