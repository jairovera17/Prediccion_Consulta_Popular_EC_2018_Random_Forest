import re
import sys
import json
import couchdb
import os
import urllib.request

import nltk
from nltk.corpus import stopwords  
from nltk import word_tokenize  
from nltk.data import load  
from nltk.stem import SnowballStemmer  
from string import punctuation  
from sklearn.feature_extraction.text import CountVectorizer       

import variables


non_words = list(punctuation)
non_words.extend(['¿', '¡'])  
non_words.extend(map(str,range(10)))

def clear_regex(a):
    b = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+','',a)   #removemos links)
    c = re.sub('[^@]+@[^@]+\.[^@]+','',b)
    d = re.sub('[^a-zA-Zñáíóúé ]','',c)
    text = re.sub(' +',' ',d)
    output = ''.join([ c for c in text if c not in non_words])#re.sub('[!@#$%^&*]','',b) 
    return output.lower()

def limpieza(input_array, file_name, limite = 20):
    aux = 0
    output_file = open(file_name,'w')
    for item in input_array:
        aux += 1
        clean_tweet = clear_regex(str(item['value']))
        output_file.write(str(clean_tweet)+'\n')
        if aux>limite :
            break;
        if aux%1000 == 0:
            print('acoplando', aux)
    output_file.close()


response_quito = urllib.request.urlopen(variables.url_tweets_quito)
json_quito_data =  json.loads(response_quito.read()) 
quito_data = json_quito_data['rows']

response_guayaquil = urllib.request.urlopen(variables.url_tweets_guayaquil)
json_guayaquil_data =  json.loads(response_guayaquil.read()) 
guayaquil_data = json_guayaquil_data['rows']

response_cuenca = urllib.request.urlopen(variables.url_tweets_cuenca)
json_cuenca_data =  json.loads(response_cuenca.read()) 
cuenca_data = json_cuenca_data['rows']



limpieza(quito_data,variables.tweets_limpios_quito,len(quito_data))
limpieza(guayaquil_data,variables.tweets_limpios_guayaquil,len(guayaquil_data))
limpieza(cuenca_data,variables.tweets_limpios_cuenca,len(cuenca_data))

