from googleapiclient.discovery import build
import pandas as pd


class YouTubeAPI():
    '''
    Class YoutTubeAPI cotains moduls which can help to get
    data from Youtube API and put it into DataFrame
    '''
    def __init__(self):
        self.name="Class contains moduls which help to ectract data from Youtube"
    def built(api_key):
        '''
        Construct a Resource for interacting with an API.
        more: https://googleapis.github.io/google-api-python-client/docs/epy/googleapiclient.discovery-module.html#build
        Parameters
        ----------        
        api_key: must be a string, it is a key created on Google Cloud Platform
        api service name= youtube
        api version=v3
        '''
        youtube= build('youtube','v3', developerKey=api_key)
        return youtube
        
    def comment(videoId,youtube):
        '''
    
        Parameters
        ----------
        videoId: must be a string; more: https://gist.github.com/jakebellacera/d81bbf12b99448188f183141e6696817
        youtube: output of built module
        
        Returns
        -------
        Creating a list of lists containing comment, author of comment and video ID.
        '''
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
    def list_of_titles(channelID, youtube):
        '''
        

        Parameters
        ----------
        channelID : must be a string; ID of the channel on Youtube
        youtube : output of built module

        Returns
        -------
        id_title : List of Videos ID of given channel

        '''
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
    def to_dataframe(titles, dataset_name, youtube):
        '''
        

        Parameters
        ----------
        titles : output of list_of_titles module
        dataset_name : name of created .csv file
        youtube : output of built module

        Returns
        -------
        File dataset_name.csv. File contains some data about given channel

        '''

        last_list=[]
        comments_base=[]
        
        for i in range(len(titles)):
            
            comments_base.append(YouTubeAPI.comment(titles[i][0], youtube))
        
        for i in range(len(comments_base)): # loops adding title, author and comment to one list
            lista=[]
            for j in range(len(comments_base[i])):
                
                for p in range(len(titles)):
                    if comments_base[i][j][0]==titles[p][0]:
                        comments_base[i][j][0]==titles[p][1]
                        lista.append(titles[p][1])
                        lista.append(comments_base[i][j][1])  
                        lista.append(comments_base[i][j][2]) 
            last_list.append(lista)
        titles_of_movies=[]
        comm=[]
        comm_author=[]
        for item in range(len(last_list)):  
            titles_of_movies.append(last_list[item][0::3])
            #titles_of_movies=titles_of_movies[item]*len(last_list[item])/3
            comm.append(last_list[item][1::3])
            comm_author.append(last_list[item][2::3])
        
        from nltk import flatten
        
        # data for a one-dimensional list, needed to create a database
        titles_of_movies = flatten(titles_of_movies)
        comm=flatten(comm)
        comm_author=flatten(comm_author)
        dane=[]
        
        for i in range(len(titles_of_movies)): #loop adding list [title,author, comment] to one list
            lista2=[]
            lista2.append(titles_of_movies[i])
            lista2.append(comm_author[i])
            lista2.append(comm[i])
            dane.append(lista2)
        
        name_of_db=str(dataset_name)+".csv"
        database=pd.DataFrame(dane)
        database=database.rename(columns={"0": "Title",'1':"Author", "2":"Comment"})
        database=database.drop(columns="Unnamed: 0")
        database.to_csv(name_of_db)
                
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        