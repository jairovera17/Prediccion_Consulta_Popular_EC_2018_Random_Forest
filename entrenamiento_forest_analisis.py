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

spanish_stopwords = stopwords.words('spanish')
stemmer = SnowballStemmer('spanish')
non_words = list(punctuation)  
non_words.extend(['¿', '¡'])  
non_words.extend(map(str,range(10)))

train_files = [
    variables.tweets_label_quito_train,
    variables.tweets_label_guayaquil_train,
    variables.tweets_label_cuenca_train
]

train_tweets_text = []
train_tweets_label= []

for item in train_files:
    file = open(item,'r')
    line = file.read().split('\n')
    for linea in line:
        array = linea.split(',')
        if len(array)==2:
            train_tweets_label.append(int(array[0]))
            train_tweets_text.append(array[1]) 



vectorizer = CountVectorizer(analyzer = 'word', \
                            tokenizer = tokenize, \
                            preprocessor = None, \
                            stop_words = spanish_stopwords, \
                            max_features = 5000)


train_data_features = vectorizer.fit_transform(train_tweets_text)
train_data_features = train_data_features.toarray()


print(train_data_features.shape)

vocab = vectorizer.get_feature_names()
#print(vocab)            #Imprime el vocabulario

#Random Forest

forest = RandomForestClassifier(n_estimators = 100)

forest = forest.fit(train_data_features, train_tweets_label)

vector  = open('vectorizer.pkl','wb')
pickle.dump(vectorizer,vector)
vector.close()

output = open('forestclassifier.pkl','wb')
pickle.dump(forest,output)
output.close()