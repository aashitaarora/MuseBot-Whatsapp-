import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "client-secret1.json"

import dialogflow_v2 as dialogflow
dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "music-neiedm"

from musixmatch import Musixmatch
musixmatch=Musixmatch("668ca0e26add2355dafb6fded1744099")

from gnewsclient import gnewsclient

client = gnewsclient.NewsClient(max_results=3)

from pymongo import MongoClient

cl=MongoClient("mongodb+srv://test:test@cluster0-qfiec.mongodb.net/test?retryWrites=true&w=majority")
db=cl.get_database('user_db')
records=db.user_info

def update_records(id,topic,language,location):
    if (topic!=" "):
        records.update_one({'session_id':id},{"$set":{"news_type":topic}},upsert=True)
    if (language!=" "):
        records.update_one({'session_id':id},{"$set":{"language":language}},upsert=True)
    if (location!=" "):
        records.update_one({'session_id':id},{"$set":{"location":location}},upsert=True)
    a=records.find_one({"session_id":id})
    return (a["news_type"],a["language"],a["location"])


def get_news(id,parameters):
    print(parameters)
    client.topic=parameters.get('news_type')
    client.language=parameters.get('language')
    client.location =parameters.get('geo-country')
    updated = update_records(id,client.topic,client.language,client.location)
    client.topic=updated[0]
    client.language=updated[1]
    client.location = updated[2]
    return client.get_news()

def list_tracks(country):
    tr=musixmatch.chart_tracks_get(1, 5,'in')['message']['body']['track_list']
    li=[]
    for i in range(5):
        li.append(tr[i]['track']['track_name'])
    return li

def findthesong(parameters):
    track=parameters.get('trackname')
    artist=parameters.get('music-artist')
    print(track)
    print(artist)
    a=musixmatch.matcher_track_get(track,artist)
    result=a['message']['body']['track']['track_share_url']
    return result

def detect_intent_from_text(text, session_id, language_code='en'):
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result

def fetch_reply(msg,session_id):
    response=detect_intent_from_text(msg,session_id)

    print(response.parameters)
    if response.intent.display_name =='get_news':
        news=get_news(session_id,dict(response.parameters))
        #news_str="Yeah sure .. Here:"
        
        #for row in news:
            #news_str += "\n\n{}\n\n{}\n\n".format(row['title'],row['link'])
        #return news_str
        return news
    elif response.intent.display_name=='get_tracks':
        li=list_tracks('India')
        new_str="Yeah ..sure ..These are the top 5 in your country\n"
        for i in li:
            new_str+="\n\n{}".format(i)
        #print(li)
        return new_str
    elif response.intent.display_name=='find_song':
            r=findthesong(dict(response.parameters))
            return r
            
        
        
    else:
        return response.fulfillment_text