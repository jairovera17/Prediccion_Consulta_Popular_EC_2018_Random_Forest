import variables

tweets_sin_label = [
    [variables.tweets_limpios_quito,variables.tweets_label_quito_train,variables.tweets_label_quito_test],
    [variables.tweets_limpios_guayaquil,variables.tweets_label_guayaquil_train,variables.tweets_label_guayaquil_test],
    [variables.tweets_limpios_cuenca,variables.tweets_label_cuenca_train,variables.tweets_label_cuenca_test]
]

def split_array(input_array):
    ar1=[]
    ar2=[]
    for i in range(len(input_array)):
        if i%2==0:
            ar1.append(input_array[i])
        else:
            ar2.append(input_array[i])
    output_array = [ar1,ar2]
    return output_array

def generar_labels(frases_input):
    train_data = []
    for frase in frases_input:
        words = frase.split(' ')
        polarity = 0
        for word in words:
            for dicc in variables.dicc_words:
                if word == dicc[0]:
                    polarity+=dicc[1]
        if polarity!=0:
            train_data.append([polarity,frase])
    return train_data

def save_data(input,label):
    file = open(input,'w')
    for item in label:
        voto = 0
        if item[0] > 0:
            voto = 1
        file.write(str(voto)+','+item[1]+'\n')
    file.close()
    
             
        

def label_tweets(input_array):
    file = open(input_array[0],'r')
    frases = file.read().split('\n')
    label = split_array(generar_labels(frases))
    save_data(input_array[1],label[0])
    save_data(input_array[2],label[1])



for item in tweets_sin_label:
    label_tweets(item)



