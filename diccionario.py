from nltk.corpus import stopwords
import variables

spanish_stopwords = stopwords.words('spanish')
diccionario = []

def acoplar(word):
    for i in range(len(diccionario)):
        if (str(diccionario[i][1]) == word):
            diccionario[i][0]+=1
            return
    diccionario.append([1,word])

def generar_diccionario(frases_input):
    aux = 0
    for item in frases_input:
        aux += 1
        array = item.split(' ')
        frase_array = [w for w in array if not w in spanish_stopwords]
        for word in frase_array:
            acoplar(word)
        if aux%1000 == 0:
            print('acoplados =>'+str(aux))

def guardar_diccionario(input_diccionario):
    file = open(variables.diccionario_repeticiones,'w')
    for word in diccionario:
        if word[0]>10:
            file.write(str(word[0])+','+str(word[1])+'\n')

file = open(variables.tweets_limpios_totales,'r')
frases = file.read().split('\n')

generar_diccionario(frases)
diccionario.sort()
guardar_diccionario(diccionario)