

from googleapiclient.discovery import build
# required data   
api_key = 'api_key'
videoId='video_ID'

youtube = build('youtube', 'v3',
            developerKey=api_key)
#---------------------------------------

def komentarz(videoId):
    komentarze_viedo_id=[]
    video_response=youtube.commentThreads().list(
    part='snippet,replies',
    videoId=videoId
    ).execute()
    
    
    while video_response:
       
    # data set of video with unique ID
        for item in video_response['items']:
            komentarze=[]
            
            #getting comments, authrs
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            autor=item['snippet']['topLevelComment']['snippet']['authorDisplayName']
            komentarze.append(videoId)
            komentarze.append(comment)
            komentarze.append(autor)
            #amount of replied comments
            replycount = item['snippet']['totalReplyCount']
            komentarze_viedo_id.append(komentarze)
            #adding comments and replies to the same list 
            if replycount>0:
                for reply in item['replies']['comments']:
                    komentarze2=[]
                    reply2 = reply['snippet']['textDisplay']
                    autor2 = reply['snippet']['authorDisplayName']
                    
                    komentarze2.append(videoId)
                    komentarze2.append(reply2)
                    komentarze2.append(autor2)
                    komentarze_viedo_id.append(komentarze2)

                  
        return komentarze_viedo_id
