'''

 
 QUITO 
==============
'''
import couchdb
import sys
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
 
 
##########API CREDENTIALS ############   Poner sus credenciales del API de dev de Twitter
ckey = "WzcFjhTm8GHDFgj886jWEC0CC"
csecret = "0tv16COyKfxtsvqsY2BsNNXnVDysihYiTCXpPM1T6JG9b04BaD"
atoken = "309356518-qQBChXVWPxXagzv0TscLqR4tTVgRM0yTa4cFNL7V"
asecret = "rNDGQ5zs91k8qWFP7JU0ppm3viiiAHly0SFoZe7MLFWJc"
 
class listener(StreamListener):
 
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            #print ("SAVED" + str(doc) +"=>" + str(data))
            print (str(dictTweet['text']))
            print (str(dictTweet['lang']))
        except:
            print ("Already exists")
            pass
        return True
 
    def on_error(self, status):
        print (status)
 
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
 
 
if len(sys.argv)!=3:
    sys.stderr.write("Error: needs more arguments: <URL><DB name>\n")
    sys.exit()
 
URL = sys.argv[1]
db_name = sys.argv[2]
 
 
'''========couchdb'=========='''
server = couchdb.Server('http://'+URL+':5984/')  #('http://245.106.43.184:5984/') poner la url de su base de datos
try:
    print (db_name)
    db = server[db_name]
 
except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()
 
 
'''===============LOCATIONS=============='''
 
 #twitterStream.filter(locations=[-78.593445,-0.370099,-78.386078,-0.081711])  #QUITO 

#twitterStream.filter(locations=[-74.25909,40.477399,-73.700272,40.917577]) #New York

twitterStream.filter(locations=[-79.959122,-2.287573,-79.856354,-2.053361,-78.593445,-0.370099,-78.386078,-0.081711,-79.054695,-2.931505,-78.924065,-2.853034])#Quito Guayaquil y Cuenca