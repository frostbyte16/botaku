# returns one random anime or manga
import pandas as pd
import random

# Reads the anime and manga csv files and drops all null values as well as resets the index for any blank rows
df_anime = pd.read_csv("anime.csv")
df_anime.dropna(subset=['synopsis'], inplace=True)
df_anime.drop_duplicates(subset=['title'], inplace=True)
df_anime.reset_index(drop=True, inplace=True)

df_manga = pd.read_csv("manga.csv")
df_manga.dropna(subset=['synopsis'], inplace=True)
df_manga.drop_duplicates(subset=['title'], inplace=True)
df_manga.reset_index(drop=True, inplace=True)

def randomAnime():
    rand = random.randrange(0,len(df_anime))
    recommendation = df_anime.iloc[rand]
    recoList = recommendation.values.tolist()
    print(recoList)
    return recoList

def randomManga():
    rand = random.randrange(0,len(df_manga))
    recommendation = df_manga.iloc[rand]
    recoList = recommendation.values.tolist()
    return recoList
