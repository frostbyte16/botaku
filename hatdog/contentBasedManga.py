# content based filtering manga
import pandas as pd
from sklearn.metrics.pairwise import sigmoid_kernel, cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

df_manga = pd.read_csv("manga.csv")
df_manga.drop_duplicates(subset=['title'])
x = df_manga.loc[(df_manga['synopsis'].isnull())]

# Drops all blank manga with blank synopsis
df_manga.dropna(subset=['synopsis'], inplace=True)

# Computes for the similarity of synopsis using sigmoid kernel
tfv = TfidfVectorizer(min_df=3, max_features=None, strip_accents='unicode',
                       analyzer='word', token_pattern=r'\w{1,}', ngram_range=(1, 3), stop_words='english')

tfv_matrix = tfv.fit_transform(df_manga['synopsis'])
sig = sigmoid_kernel(tfv_matrix, tfv_matrix)
indices = pd.Series(df_manga.index,index=df_manga['title']).drop_duplicates()

# Computes for the similarity of genre and rating using cosine similarity
m = df_manga.userCount.quantile(0.75)
C = df_manga.rating.mean()

def weighted_rating(df, m, C):
    term = df['userCount'] / (m + df['userCount'])
    return df['rating'] * term + (1-term) * C

df_manga = pd.concat([df_manga, df_manga['genre'].str.get_dummies(sep=',')], axis=1)

manga_features = df_manga.loc[:, " 'action'":].copy()
cosine_sim = cosine_similarity(manga_features.values, manga_features.values)
manga_index = pd.Series(df_manga.index, index=df_manga.title).drop_duplicates()

def recommend_manga(title, similarity=cosine_similarity):
    # Searches for manga if title exists in dataframe
    if df_manga['title'].str.contains(title).sum() > 0:
        idx = int(indices[title])

        # multiplies the similarity of synopsis and genre
        scores = list(enumerate(sig[idx]*cosine_sim[idx]))

        # sort the movies
        scores = sorted(scores, key=lambda x: x[1], reverse=True)

        # manga indices
        manga_indices = [i[0] for i in scores]

        recommendation = df_manga[['title','status','chCount','vCount','image','rating','synopsis']].iloc[manga_indices]

        # Top 5 most similar manga
        recommendation = recommendation[1:6]
    else:
        # Returns empty dataframe if title is not found
        recommendation = df_manga.iloc[0:0]

    return recommendation
#
# while 1!=0:
#     mangaTitle = input('Enter title: ')
#
#     x = recommend_manga(mangaTitle)
#     y = x.values.tolist()
#
#     for a in y:
#         print(a)
