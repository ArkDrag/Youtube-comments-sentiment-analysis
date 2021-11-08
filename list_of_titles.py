


from googleapiclient.discovery import build

client_secrets_file='client_secret.json'
scopes=['https://www.googleapis.com/auth/youtube.force-ssl']
api_service_name= 'youtube' # name and version downloaded ofrm https://github.com/googleapis/google-api-python-client/blob/main/docs/dyn/index.md
api_version='v3'
api_key='api_key'
youtube= build("youtube",'v3', developerKey=api_key)
channelID='Channel_id'
#snippetdata=youtube.channels().list(part='snippet',id=channelID).execute()

   
def list_of_titles(channelID):
    videos = [ ]
    id_title=[]
    contentdata=youtube.channels().list(id=channelID,part='contentDetails').execute()
    
    
    playlist_id = contentdata['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    
    next_page_token = None
    
    
    
    while 1:
         res = youtube.playlistItems().list(playlistId=playlist_id,
                                                   part='snippet',
                                                   maxResults=50,
                                                   pageToken=next_page_token).execute()
         videos += res['items']
         next_page_token = res.get('nextPageToken')
    
    
    
         if next_page_token is None:
             break
         
            
         


   
    for i in range(len(videos)):
        lista=[]
        title=videos[i]['snippet']['title']
        video_id=videos[i]['snippet']['resourceId']['videoId']
        
        lista.append(video_id)
        lista.append(title)
        id_title.append(lista)
    
    return id_title

