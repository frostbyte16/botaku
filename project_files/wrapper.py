import kitsu
import contentBasedAnime as cba
import contentBasedManga as cbm
import asyncio

client = kitsu.Client()

async def anime_search(query):
    entries = await client.search('anime', query, limit=1)
    if not entries:
        print(f'No entries found for "{query}"')
        return []

    for i, anime in enumerate(entries, 1):
        print(anime.title)
        recommendation = cba.recommend_anime(anime.title, anime.subtype)
        # print(recommendation)
        if recommendation.size > 0:
            recoList = recommendation.values.tolist()
            return recoList
        else:
            return []

async def manga_search(query):
    entries = await client.search('manga', query, limit=5)
    if not entries:
        print(f'No entries found for "{query}"')
        return []

    for i, manga in enumerate(entries, 1):
        print(manga.title)
        recommendation = cbm.recommend_manga(manga.title)
        if recommendation.size > 0:
            recoList = recommendation.values.tolist()
            return recoList
        else:
            return []

# test
# loop = asyncio.get_event_loop()
#
# while 1!=0:
#     x = input('Insert an anime name: ')
#     listRec = loop.run_until_complete(anime_search(x))
#     if len(listRec) > 0:
#         for items in listRec:
#             print(items)
#
#     y = input('Insert a manga name: ')
#     listRec = loop.run_until_complete(manga_search(y))
#     if len(listRec) > 0:
#         for items in listRec:
#             print(items)