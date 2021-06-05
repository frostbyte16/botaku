# content based filtering anime
import pandas as pd
from sklearn.metrics.pairwise import sigmoid_kernel, cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

df_anime = pd.read_csv("anime.csv")

# Drops all blank anime with duplicate titles
df_anime.drop_duplicates(subset=['title'], inplace=True)

x = df_anime.loc[(df_anime['synopsis'].isnull())]

# Drops all blank anime with blank synopsis
df_anime.dropna(subset=['synopsis'], inplace=True)

# Resets the index of dataframe after removing blanks and duplicates
df_anime.reset_index(drop=True, inplace=True)

# Computes for the similarity of synopsis using sigmoid kernel
tfv = TfidfVectorizer(min_df=3, max_features=None, strip_accents='unicode',
                      analyzer='word', token_pattern=r'\w{1,}', ngram_range=(1, 3), stop_words='english')

tfv_matrix = tfv.fit_transform(df_anime['synopsis'])
sig = sigmoid_kernel(tfv_matrix, tfv_matrix)
indices = pd.Series(df_anime.index, index=df_anime['title']).drop_duplicates()

# Computes for the similarity of genre and rating using cosine similarity
m = df_anime.userCount.quantile(0.75)
C = df_anime.rating.mean()

df_anime = pd.concat([df_anime, df_anime['subtype'].str.get_dummies(), df_anime['genre'].str.get_dummies(sep=',')],
                     axis=1)

anime_features = df_anime.loc[:, "TV":].copy()
anime_features.head()
cosine_sim = cosine_similarity(anime_features.values, anime_features.values)
anime_index = pd.Series(df_anime.index, index=df_anime.title).drop_duplicates()


def recommend_anime(title, type, similarity=cosine_sim):
    # Searches for anime if title exists in dataframe
    if df_anime['title'].str.contains(title).sum() > 0:
        idx = int(indices[title])

        # multiplies the similarity of synopsis and genre
        scores = list(enumerate(sig[idx] * cosine_sim[idx]))

        # sort the movies
        scores = sorted(scores, key=lambda x: x[1], reverse=True)

        # anime indices
        anime_indices = [i[0] for i in scores]

        recommendation = df_anime[['title', 'status', 'subtype', 'epCount', 'image', 'rating', 'synopsis']].iloc[
            anime_indices]

        if type == 'TV':
            recommendation.drop(df_anime[df_anime['subtype'] == 'movie'].index, inplace=True)
            recommendation.drop(df_anime[df_anime['subtype'] == 'ONA'].index, inplace=True)
            recommendation.drop(df_anime[df_anime['subtype'] == 'OVA'].index, inplace=True)
            recommendation.drop(df_anime[df_anime['subtype'] == 'special'].index, inplace=True)
            recommendation.drop(df_anime[df_anime['subtype'] == 'music'].index, inplace=True)
        elif type == 'movie':
            recommendation.drop(df_anime[df_anime['subtype'] == 'TV'].index, inplace=True)
            recommendation.drop(df_anime[df_anime['subtype'] == 'ONA'].index, inplace=True)
            recommendation.drop(df_anime[df_anime['subtype'] == 'OVA'].index, inplace=True)
            recommendation.drop(df_anime[df_anime['subtype'] == 'special'].index, inplace=True)
            recommendation.drop(df_anime[df_anime['subtype'] == 'music'].index, inplace=True)

        # Top 5 most similar anime
        recommendation = recommendation[1:6]
    else:
        # Returns empty dataframe if title is not found
        recommendation = df_anime.iloc[0:0]

    return recommendation

# while 1!=0:
#     #print(df_anime)
#     animeTitle = input('Enter title: ')
#
#     x = recommend_anime(animeTitle, 'TV')
#     y = x.values.tolist()
#
#     for a in y:
#         print(a)
