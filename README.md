# MuseBot-Whatsapp-
**A music and news companion**

**This is a Whatsapp bot built using Twilio, Dialogflow, Pymusixmatch and Gnewsclient.**
The bot can serve three intents : **get_news , find_song and get_tracks.**
The find_song and get_tracks intents are built using Pymusixmatch wrapper library 
**Find_song** intent is based on the entities track_name and music_artist. Queries like "Find the song Old Town by Lil Nas" . The bot answers with a link to the audio and its lyrics


The **get_tracks** intent takes entity : Country and lists the current top 5 tracks.

The **get_news** takes three entities news_type , language and location and sends three news headlines along with links of detailed articles. This has been implemented through gnewsclient Python wrapper library.

Extended functionality using MongoDB : Parameters of every search query are stored and if any of the paramters are missing in any query the last used value of that parameter will be used . For example if the user says "Sports News in India in English" and the next query is "News in India in Hindi" then the news_type .. "Sports" will remain persistent between these queries.

The web server has been hosted on :https://mnbotserver.herokuapp.com/

Send a WhatsApp message to +14155238886 with code join chief-television
