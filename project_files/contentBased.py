# content based filtering
import pandas as pd
from sklearn.metrics.pairwise import sigmoid_kernel, cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import random


def recommend(name, anime_type, subtype):
    df_anime = pd.read_csv(f"{anime_type}.csv")
    # Drops all blank anime with duplicate titles
    df_anime.drop_duplicates(subset=['title'], inplace=True)

    x = df_anime.loc[(df_anime['synopsis'].isnull())]

    # Drops all blank anime with blank synopsis
    df_anime.dropna(subset=['synopsis'], inplace=True)

    if anime_type == 'manga':
        df_anime['chCount'] = df_anime['chCount'].fillna(0)
        df_anime['vCount'] = df_anime['vCount'].fillna(0)

    # Resets the index of dataframe after removing blanks and duplicates
    df_anime.reset_index(drop=True, inplace=True)

    # Computes for the similarity of synopsis using sigmoid kernel
    tfv = TfidfVectorizer(min_df=3, max_features=None, strip_accents='unicode',
                          analyzer='word', token_pattern=r'\w{1,}', ngram_range=(1, 3), stop_words='english')

    tfv_matrix = tfv.fit_transform(df_anime['synopsis'])
    sig = sigmoid_kernel(tfv_matrix, tfv_matrix)
    indices = pd.Series(df_anime.index, index=df_anime['title']).drop_duplicates()

    if anime_type == 'anime':
        df_anime = pd.concat(
            [df_anime, df_anime['subtype'].str.get_dummies(), df_anime['genre'].str.get_dummies(sep=',')], axis=1)
        anime_features = df_anime.loc[:, "TV":].copy()
    elif anime_type == 'manga':
        df_anime = pd.concat([df_anime, df_anime['genre'].str.get_dummies(sep=', ')], axis=1)
        anime_features = df_anime.loc[:, "'Cooking']":].copy()

    cosine_sim = cosine_similarity(anime_features.values, anime_features.values)

    def recommend_anime(title, similarity=cosine_sim):
        title = title.replace(' (TV)', '')

        # Searches for anime if title exists in dataframe
        if title in df_anime.values:
            if df_anime['title'].str.contains(title).sum() > 0:
                idx = int(indices[title])

                # multiplies the similarity of synopsis and genre
                scores = list(enumerate(sig[idx] * cosine_sim[idx]))

                # sort the movies
                scores = sorted(scores, key=lambda x: x[1], reverse=True)

                # anime indices
                anime_indices = [i[0] for i in scores]

                if anime_type == 'anime':
                    recommendation = \
                        df_anime[['title', 'status', 'subtype', 'epCount', 'image', 'rating', 'synopsis']].iloc[
                            anime_indices]
                    if subtype == 'TV':
                        recommendation.drop(df_anime[df_anime['subtype'] == 'movie'].index, inplace=True)
                    elif subtype == 'movie':
                        recommendation.drop(df_anime[df_anime['subtype'] == 'TV'].index, inplace=True)
                else:
                    recommendation = \
                        df_anime[['title', 'status', 'chCount', 'vCount', 'image', 'rating', 'synopsis']].iloc[
                            anime_indices]

                # Returns 5 from Top 10 most similar anime
                ran_idx = random.randint(1, 5)
                recommendation = recommendation[ran_idx:ran_idx+5]
        else:
            # Returns empty dataframe if title is not found
            recommendation = df_anime.iloc[0:0]

        return recommendation

    recommended = recommend_anime(name, anime_type)
    return recommended