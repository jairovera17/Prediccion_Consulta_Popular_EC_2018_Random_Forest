from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import nltk
import pandas as pd
import numpy as np
import pickle
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from string import punctuation
from nltk.data import load  
from nltk import word_tokenize 

import variables

spanish_stopwords = stopwords.words('spanish')
stemmer = SnowballStemmer('spanish')

non_words = list(punctuation)  
non_words.extend(['¿', '¡'])  
non_words.extend(map(str,range(10)))

def stem_tokens(tokens, stemmer):  
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):  
    # remove punctuation
    text = ''.join([c for c in text if c not in non_words])
    # tokenize
    tokens =  word_tokenize(text)

    # stem
    try:
        stems = stem_tokens(tokens, stemmer)
    except Exception as e:
        print(e)
        print(text)
        stems = ['']
    return stems


def recuperar_pickle(path):
    file = open(path,'rb')
    return pickle.load(file)

forest = recuperar_pickle(variables.forestclassifier)
vectorizer = recuperar_pickle(variables.vectorizer)


test_tweets_label = []
test_tweets_text = []

test_files =[
    variables.tweets_label_quito_test,
    variables.tweets_label_guayaquil_test,
    variables.tweets_label_cuenca_test
]

for item in test_files:
    file = open(item,'r')
    line = file.read().split('\n')
    for linea in line:
        array = linea.split(',')
        if len(array)==2:
            test_tweets_label.append(int(array[0]))
            test_tweets_text.append(array[1]) 

test_data_features = vectorizer.transform(test_tweets_text)
test_data_features = test_data_features.toarray()


result = forest.predict(test_data_features)
print(len(test_tweets_text))
print(len(result))





