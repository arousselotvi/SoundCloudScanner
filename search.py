import requests
import json
myClientId="5DeoP85oSz6LoxhpVvEwf4d9eJHUBRKP"
apiUrl="https://api.soundcloud.com/"

def getResults(keyWords,genre,label):
    #create query string
    queryString=""
    if len(keyWords)>0:
        queryString+="&q="+keyWords.replace(" " , "%20")
    if len(genre)>0:
        queryString+="&genres="+genre.replace(" " , "%20")
    r = requests.get(apiUrl+"tracks/?client_id=" + myClientId+queryString+"&limit=200")
    print(apiUrl+"tracks/?client_id=" + myClientId+queryString)
    r = r.json()
    #filter results
    #retrieve only downloadable tracks
    if len(label)>0:
        r=[tracks for tracks in r if (tracks['downloadable']==True and tracks['label_name']==label)]
    else:
        r=[tracks for tracks in r if (tracks['downloadable']==True)]
    return r

