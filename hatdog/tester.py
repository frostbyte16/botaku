import requests
import random

genreList = ['action', 'adventure', 'angst', 'anime-influenced', 'anthropomorphism', 'blackmail', 'comedy', 'detective',
         'drama', 'ecchi', 'fantasy', 'ghost', 'harem', 'henshin', 'horror', 'magical-girl', 'mystery', 'parasite',
         'psychological', 'romance', 'science-fiction', 'super-power', 'supernatural', 'thriller', 'vampire',
         'virtual-reality', 'zombie', 'josei', 'kids', 'seinen', 'shoujo', 'shounen']

#genre = random.choice(genreList)
genre='zombie'
randOffset = random.randint(0, 100)

api = f'https://kitsu.io/api/edge/manga?filter[categories]={genre}&page[limit]=5&page[offset]={randOffset}'
response = requests.get(api)

animeDict = response.json()
print(genre)
print(randOffset)

for i in range(5):
    print(i + 1)
    #print(animeDict["data"][i]["attributes"]["titles"])
    try:
        titleIndex0 = list(animeDict["data"][i]["attributes"]["titles"])[0]
        titleIndex1 = list(animeDict["data"][i]["attributes"]["titles"])[1]
    except:
        print('')

    #finds the first anime title available
    if animeDict["data"][i]["attributes"]["titles"][titleIndex0] == None:
        print(animeDict["data"][i]["attributes"]["titles"][titleIndex1])
    else:
        print(animeDict["data"][i]["attributes"]["titles"][titleIndex0])

    print(animeDict["data"][i]["attributes"]["posterImage"]["medium"])
    print(animeDict["data"][i]["attributes"]["posterImage"]["medium"])

    if animeDict["data"][i]["attributes"]["synopsis"] == '':
        print("Synopsis unavailable")
    else:
        print("Synopsis:" + animeDict["data"][i]["attributes"]["synopsis"])
    print("======")
