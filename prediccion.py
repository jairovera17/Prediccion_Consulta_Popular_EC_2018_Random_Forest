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

    
def porcentaje(maximo,obtenido):
    return (obtenido*100)/maximo

        

def calcular_matriz_confusion(actual,prediccion):
    if len(actual)!=len(prediccion):
        print('error en dimensiones')
        return
    falso_positivo = 0
    falso_negativo = 0
    verdadero_negativo = 0
    verdadero_positivo = 0
    actual_si = 0
    actual_no = 0
    prediccion_si = 0
    prediccion_no = 0

    for i in range(len(actual)):
        if actual[i] == 1:
            if prediccion[i] == 1:
                verdadero_positivo+=1
        if actual[i] == 0:
            if prediccion[i] == 0:
                verdadero_negativo+=1
        if actual[i] == 1:
            if prediccion[i] == 0:
                falso_negativo+=1
        if actual[i] == 0:
            if prediccion[i] == 1:
                falso_positivo+=1

        if actual[i]== 1:
            actual_si+=1
        if actual[i]== 0:
            actual_no+=1
        if prediccion[i]==1:
            prediccion_si+=1
        if prediccion[i]==0:
            prediccion_no+=1
    
    file = open(variables.matriz_confusion,'w')
    file.write('\tsi\tno\n')
    file.write('si\t'+str(verdadero_positivo)+'\t'+str(falso_negativo)+'\n')
    file.write('no\t'+str(falso_positivo)+'\t'+str(verdadero_negativo)+'\n')
    file.write('\n\n')

    file.write('Reales\n')
    file.write('Si ==> '+str(actual_si)+'\n')
    file.write('No ==> '+str(actual_no)+'\n')
    file.write('Predicciones\n')
    file.write('Si ==> '+str(prediccion_si)+'\n')
    file.write('No ==> '+str(prediccion_no)+'\n')

    file.write('\nPorcentajes\n')
    file.write('Reales\n')
    total = len(actual)
    file.write('Si ==> '+str(porcentaje(total,actual_si))+'\n')
    file.write('No ==> '+str(porcentaje(total,actual_no))+'\n\n')

    file.write('Predicciones\n')
    total = len(actual)
    file.write('Si ==> '+str(porcentaje(total,prediccion_si))+'\n')
    file.write('No ==> '+str(porcentaje(total,prediccion_no)))

    file.write('\nAccuracy\n')
    total = len(actual)
    file.write('% ==> '+str(porcentaje((verdadero_negativo+verdadero_positivo+falso_negativo+falso_positivo),(verdadero_negativo+verdadero_positivo)))+'\n')
    file.close()


forest = recuperar_pickle(variables.forestclassifier)
vectorizer = recuperar_pickle(variables.vectorizer)


test_tweets_label = []
test_tweets_text = []

test_files =[
    variables.tweets_label_quito_test,
  #  variables.tweets_label_guayaquil_test,
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

calcular_matriz_confusion(test_tweets_label,result)