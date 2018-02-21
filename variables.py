folder_tweets_limpios = './tweets_limpios/'
folder_data = './data/'

url_tweets_quito = 'http://localhost:5984/consulta_2018_final/_design/vistasbi/_view/get_tweets_quito'
tweets_limpios_quito = folder_tweets_limpios+'tweets_limpios_quito.txt'
tweets_label_quito_train = folder_data+'tweets_label_quito_train.csv'
tweets_label_quito_test = folder_data+'tweets_label_quito_test.csv'

url_tweets_guayaquil = 'http://localhost:5984/consulta_2018_final/_design/vistasbi/_view/get_tweets_guayaquil'
tweets_limpios_guayaquil = folder_tweets_limpios+'tweets_limpios_guayaquil.txt'
tweets_label_guayaquil_train = folder_data+'tweets_label_guayaquil_train.csv'
tweets_label_guayaquil_test = folder_data+'tweets_label_guayaquil_test.csv'

url_tweets_cuenca = 'http://localhost:5984/consulta_2018_final/_design/vistasbi/_view/get_tweets_cuenca'
tweets_limpios_cuenca = folder_tweets_limpios+'tweets_limpios_cuenca.txt'
tweets_label_cuenca_train = folder_data+'tweets_label_cuenca_train.csv'
tweets_label_cuenca_test = folder_data+'tweets_label_cuenca_test.csv'

tweets_limpios_totales = folder_tweets_limpios+'tweets_limpios_totales.txt'

diccionario_repeticiones = folder_tweets_limpios+'diccionario.csv'

matriz_confusion = 'matriz.txt'

train_file = folder_data+'train_file.csv'

forestclassifier = 'forestclassifier.pkl'
vectorizer = 'vectorizer.pkl'


dicc_words = [
['ratael', 0.5],
['mashirafael',-0.5],
['lenin',0.25],
['ciudadana',-0.25],
['ecuadorrc',-0.4],
['vecesno',-0.5],
['dilesno',-0.5],
['somosmasec',-0.5],
['moreno',0.4],
['patria',-0.25],
['lassoguillermo',-0.25],
['vecessi',+0.5],
['rafael',-0.25],
['votono',0.5],
['revolución',-0.4],
['traidor',-0.4],
['cuantico',-0.25],
['pillo',-0.25]
]


