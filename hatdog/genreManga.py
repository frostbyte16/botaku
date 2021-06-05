# genre manga
import pandas as pd
import random

df_manga = pd.read_csv("manga.csv")

# Drops all blank manga with duplicate titles
df_manga.drop_duplicates(subset=['title'], inplace=True)

x = df_manga.loc[(df_manga['synopsis'].isnull())]

# Drops all blank manga with blank synopsis
df_manga.dropna(subset=['synopsis'], inplace=True)

# Change None to 0
df_manga['chCount'] = df_manga['chCount'].fillna(0)
df_manga['vCount'] = df_manga['vCount'].fillna(0)
df_manga['rating'] = df_manga['rating'].fillna(0)

# Resets the index of dataframe after removing blanks and duplicates
df_manga.reset_index(drop=True, inplace=True)

def recommend_manga(genre):
    # Searches for manga if title exists in dataframe
    genre = df_manga[df_manga['genre'].str.contains(f"'{genre}'")]
    #start = random.randrange(0, 20)
    #recommendation = genre[start:start+5]

    if len(genre) > 50:
        start = random.randrange(0, 44)
        recommendation = genre[start:start + 5]
    elif len(genre) < 6:
        recommendation = genre
    else:
        size = len(genre) - 5
        start = random.randrange(0, size)
        recommendation = genre[start:start + 5]
    # recommendation = genre
    # print(len(genre))

    return recommendation

# Testing
while 1!=0:
    mangaGenre = input('Enter genre: ')
    x = recommend_manga(mangaGenre)
    y = x.values.tolist()
    for a in y:
        print(a)