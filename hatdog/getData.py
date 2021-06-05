# get data file
import requests
import csv

# gets the list of genres from kitsu
genrelist = []
Goffset = 0
index = 0

for j in range(4):
    for i in range(20):
        index = index + 1
        api = f'https://kitsu.io/api/edge/genres?page%5Blimit%5D=20&page%5Boffset%5D={Goffset}'
        response = requests.get(api)
        genreDict = response.json()
        if (index < 63):
            genrelist.append(genreDict["data"][i]["attributes"]["slug"])
        else:
            break
    Goffset = Goffset + 20

genrelist.insert(0, "none")
genrelist.insert(12, "none")
genrelist.insert(18, "none")
genrelist.insert(33, "none")

# gets data of all anime
animeFile = open('anime.csv', 'w', encoding="utf8")
writer = csv.writer(animeFile)
offset = 0

# range = 500
animeFields = [['title', 'subtype', 'status', 'image', 'epCount', 'rating', 'userCount', 'synopsis', 'genre']]
writer.writerows(animeFields)
for j in range(500):
    print("iteration no." + str(j))
    print(offset)
    for i in range(20):
        api = f'https://kitsu.io/api/edge/anime?&sort=-averageRating&page[limit]=20&page[offset]={offset}'
        response = requests.get(api)

        if response.status_code != 200:
            print('Error')
        else:
            animeDict = response.json()

            title = animeDict["data"][i]["attributes"]["canonicalTitle"]
            subtype = animeDict["data"][i]["attributes"]["subtype"]
            status = animeDict["data"][i]["attributes"]["status"]
            epCount = animeDict["data"][i]["attributes"]["episodeCount"]
            rating = animeDict["data"][i]["attributes"]["averageRating"]
            userCount = animeDict["data"][i]["attributes"]["userCount"]
            synopsis = animeDict["data"][i]["attributes"]["synopsis"]
            genreLink = animeDict["data"][i]["relationships"]["genres"]["links"]["self"]

            if animeDict["data"][i]["attributes"]["posterImage"]["large"] == None:
                image = animeDict["data"][i]["attributes"]["posterImage"]["original"]
            else:
                image = animeDict["data"][i]["attributes"]["posterImage"]["large"]

            if status == 'current':
                status = 'ongoing'

            print(offset+i)
            responseGenre = requests.get(genreLink)
            genreDictB = responseGenre.json()

            genre = []
            if len(genreDictB["data"]) == 0:
                genre.append(genrelist[0])
            for k in range(len(genreDictB["data"])):
                genre_number = int(genreDictB["data"][k]["id"])
                genre.append(genrelist[genre_number])
            # 'title', 'subtype', 'status', 'image', 'epCount', 'rating', 'userCount', 'synopsis', 'genre'
            rows = [[title, subtype, status, image, epCount, rating, userCount, synopsis, genre]]
            writer.writerows(rows)
    offset = offset + 20
animeFile.close()

# gets data of all manga
mangaFile = open('manga.csv', 'w', encoding="utf8")
writer = csv.writer(mangaFile)
offset = 0

# range = 500
mangaFields = [['title', 'status', 'image', 'chCount', 'vCount', 'rating', 'userCount', 'synopsis', 'genre']]
writer.writerows(mangaFields)
for j in range(500):
    print("iteration no." + str(j))
    print(offset)
    for i in range(20):
        api = f'https://kitsu.io/api/edge/manga?&sort=-averageRating&page[limit]=20&page[offset]={offset}'
        response = requests.get(api)

        if response.status_code != 200:
            print('Error')
        else:
            mangaDict = response.json()

            title = mangaDict["data"][i]["attributes"]["canonicalTitle"]
            status = mangaDict["data"][i]["attributes"]["status"]
            chCount = mangaDict["data"][i]["attributes"]["chapterCount"]
            vCount = mangaDict["data"][i]["attributes"]["volumeCount"]
            rating = mangaDict["data"][i]["attributes"]["averageRating"]
            userCount = mangaDict["data"][i]["attributes"]["userCount"]
            synopsis = mangaDict["data"][i]["attributes"]["synopsis"]
            genreLink = mangaDict["data"][i]["relationships"]["genres"]["links"]["self"]

            if mangaDict["data"][i]["attributes"]["posterImage"]["large"] == None:
                image = mangaDict["data"][i]["attributes"]["posterImage"]["original"]
            else:
                image = mangaDict["data"][i]["attributes"]["posterImage"]["large"]

            if status == 'current':
                status = 'ongoing'

            print(offset+i)
            responseGenre = requests.get(genreLink)
            genreDictB = responseGenre.json()

            genre = []
            if len(genreDictB["data"]) == 0:
                genre.append(genrelist[0])
            for k in range(len(genreDictB["data"])):
                genre_number = int(genreDictB["data"][k]["id"])
                genre.append(genrelist[genre_number])
            # 'title', 'status', 'image', 'chCount', 'vCount', 'rating', 'userCount', 'synopsis', 'genre'
            rows = [[title, status, image, chCount, vCount, rating, userCount, synopsis, genre]]
            writer.writerows(rows)
    offset = offset + 20
mangaFile.close()