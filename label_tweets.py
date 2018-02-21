import variables

tweets_sin_label = [
    [variables.tweets_limpios_quito,variables.tweets_label_quito],
    [variables.tweets_limpios_guayaquil,variables.tweets_label_guayaquil],
    [variables.tweets_limpios_cuenca,]
]


def generar_labels(input_array):
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

def label_tweets(input_array):
    file = open(input_array[0],'r')
    frases = file.read().split('\n')
    label = generar_labels(frases)

array = [1,2,3,4,5,6,7]
    
def split_array(input_array):
    ar1=[]
    ar2=[]
    for i in range(len(input_array)):
        if i%2==0:
            ar1.append(i)
        else:
            ar2.append(i)
    print(ar1)
    print(ar2)
            
        





