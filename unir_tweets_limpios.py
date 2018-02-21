#Se unen los tweets limpios de Quito,Guayaquil y Cuenca para extraer el diccionario de palabras repetidas
import variables

tweets_limpios = []
def acoplamiento(filename):
    file = open(filename, 'r')
    array = file.read().split('\n')
    for item in array:
        if item != '':
            tweets_limpios.append(item)
    file.close()

def imprimir_tweets_totales(filename, input_array):
    file = open(filename, 'w')
    for item in input_array:
        file.write(item+'\n')
    file.close()

archivos = [
    variables.tweets_limpios_quito,
    variables.tweets_limpios_guayaquil,
    variables.tweets_limpios_cuenca
]

def unir_todo():
    for archivo in archivos:
        acoplamiento(archivo)
    imprimir_tweets_totales(variables.tweets_limpios_totales,tweets_limpios)

unir_todo()

