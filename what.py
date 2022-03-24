import pandas as pd


#this csv is a selection of 16 randomly selected titles. The idea is that the game will narrown the list by genre and then 
# audience. Ideally, it would then also use keywords to narrow it down even more by keywords. If I run out of time it will stop 
# after audience. 
df = pd.read_csv("cynb_selections.csv")

df.rename(columns={'Title ': 'title'}, inplace=True)
df.rename(columns={'Author ': 'author'}, inplace=True)
df.rename(columns={'Audience': 'audience'}, inplace=True)
df.rename(columns={'Genre ': 'genre'}, inplace=True)
df.rename(columns={'Pub Year ': 'pub_year'}, inplace=True)
df.rename(columns={'Keywords ': 'keywords'}, inplace=True)







