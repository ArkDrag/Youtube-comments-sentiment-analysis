# Youtube-comments-sentiment-analysis

Hi,
in this project i focused on analysing the sentiment of comments under each video of Youtube channel.
As an exaple i used channel of George Gammon: https://www.youtube.com/c/GeorgeGammon 

1. At the beginning i had to create function which downloads all video IDs of channel.( file list_of_titles.py)
2. Then i had to download all comments and author of comment under video. (file getting_comment.py)
3. After that i had to combine both functions and create readable database. (to_df_function.py)
4. In Jupyter Notebook i had to clean data from emojis, neutral words and uppercases.
5. At the end i created two models: first using Naive Bayes classifier and external training data and second using TextBlob and divided comments to training and testing data.

Conclusion:
Model using Naive Bayes classifier showed that major of comments were neutral, few positive and zero negative.
Model using TextBlob showed that major were positive, 40% comments were neutral and around 10% of comments were negative.

Does it mean that second model is better?
First model could learn on wrong database ( i had not found sentminet database with bussines words and comments)
Second model predicted outputs based on TextBlob polarity and sometime gives wroge 'value' of comment.

Rest of files:
George-30.10.csv- sample of output database form to_df_function.py. I used it in my models.
Train.tsv - database which i used in Sentimend Model #1 to train my ML model

If you have any question do not hesitate to contact me: arkadiuszszymondrag@gmail.com



