# genre anime
import pandas as pd
import random

df_anime = pd.read_csv("anime.csv")

# Drops all blank anime with duplicate titles
df_anime.drop_duplicates(subset=['title'], inplace=True)

x = df_anime.loc[(df_anime['synopsis'].isnull())]

# Drops all blank anime with blank synopsis
df_anime.dropna(subset=['synopsis'], inplace=True)

# Change None to 0
df_anime['epCount'] = df_anime['epCount'].fillna(0)
df_anime['rating'] = df_anime['rating'].fillna(0)

# Resets the index of dataframe after removing blanks and duplicates
df_anime.reset_index(drop=True, inplace=True)

def recommend_anime(genre):
    # Searches for anime if title exists in dataframe
    genre = df_anime[df_anime['genre'].str.contains(f"'{genre}'")]
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
# while 1!=0:
#     animeGenre = input('Enter genre: ')
#     x = recommend_anime(animeGenre)
#     y = x.values.tolist()
#     for a in y:
#         print(a)
#
