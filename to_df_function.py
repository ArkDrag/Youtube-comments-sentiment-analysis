
import pandas as pd
from googleapiclient.discovery import build
import list_of_titles
import getting_comments
client_secrets_file='client_secret.json' #file from Google Cloud Platform
scopes=['https://www.googleapis.com/auth/youtube.force-ssl']
api_service_name= 'youtube' 
api_version='v3'
api_key='api_ key' #api key created in Google Cloud Platform
youtube= build(api_service_name,api_version, developerKey=api_key)
channelID='channelID' # name of Youtube channel, usually in URL


title=list_of_titles.list_of_titles(channelID)

last_list=[]
comments=[]

for i in range(len(title)):
    
    comments.append(getting_comments.komentarz(title[i][0]))

for i in range(len(comments)): # loops adding title, author and comment to one list
    lista=[]
    for j in range(len(comments[i])):
        
        for p in range(len(title)):
            if comments[i][j][0]==title[p][0]:
                comments[i][j][0]==title[p][1]
                lista.append(title[p][1])
                lista.append(comments[i][j][1])  
                lista.append(comments[i][j][2]) 
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


database=pd.DataFrame(dane)
database.to_csv("name.csv")



















