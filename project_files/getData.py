# get data file
import requests
import csv
import multiprocessing

# gets the list of genres from kitsu
genreList = []
genreOffset = 0
index = 0

for j in range(4):
    for i in range(20):
        index = index + 1
        api = f'https://kitsu.io/api/edge/genres?page%5Blimit%5D=20&page%5Boffset%5D={genreOffset}'
        response = requests.get(api)
        genreDict = response.json()
        if index < 63:
            genreList.append(genreDict["data"][i]["attributes"]["slug"])
        else:
            break
    genreOffset = genreOffset + 20

genreList.insert(0, "none")
genreList.insert(12, "none")
genreList.insert(18, "none")
genreList.insert(33, "none")


def getAnime():
    # gets data of all anime
    animeFile = open('anime.csv', 'w', encoding="utf8")
    writer = csv.writer(animeFile)
    offset = 0

    # range = 500 due to getting relevant anime only
    animeFields = [['title', 'subtype', 'status', 'image', 'epCount', 'rating', 'synopsis', 'genre']]
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
                synopsis = animeDict["data"][i]["attributes"]["synopsis"]
                genreLink = animeDict["data"][i]["relationships"]["genres"]["links"]["self"]

                if animeDict["data"][i]["attributes"]["posterImage"]["large"] == None:
                    image = animeDict["data"][i]["attributes"]["posterImage"]["original"]
                else:
                    image = animeDict["data"][i]["attributes"]["posterImage"]["large"]

                if status == 'current':
                    status = 'Ongoing'
                elif status == 'finished':
                    status = 'Finished'

                print(offset + i)
                responseGenre = requests.get(genreLink)
                genreDictB = responseGenre.json()

                genre = []
                if len(genreDictB["data"]) == 0:
                    genre.append(genreList[0])
                for k in range(len(genreDictB["data"])):
                    genre_number = int(genreDictB["data"][k]["id"])
                    genre.append(genreList[genre_number])

                rows = [[title, subtype, status, image, epCount, rating, synopsis, genre]]
                #       0       1       2       3       4       5       6           7
                writer.writerows(rows)
        offset = offset + 20
    animeFile.close()


def getManga():
    # gets data of all manga
    mangaFile = open('manga.csv', 'w', encoding="utf8")
    writer = csv.writer(mangaFile)
    offset = 0

    # range = 500 due to getting relevant manga only
    mangaFields = [['title', 'status', 'image', 'chCount', 'vCount', 'rating', 'synopsis', 'genre']]
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
                synopsis = mangaDict["data"][i]["attributes"]["synopsis"]
                genreLink = mangaDict["data"][i]["relationships"]["genres"]["links"]["self"]

                if mangaDict["data"][i]["attributes"]["posterImage"]["large"] == None:
                    image = mangaDict["data"][i]["attributes"]["posterImage"]["original"]
                else:
                    image = mangaDict["data"][i]["attributes"]["posterImage"]["large"]

                if status == 'current':
                    status = 'Ongoing'
                elif status == 'finished':
                    status = 'Finished'

                print(offset + i)
                responseGenre = requests.get(genreLink)
                genreDictB = responseGenre.json()

                genre = []
                if len(genreDictB["data"]) == 0:
                    genre.append(genreList[0])
                for k in range(len(genreDictB["data"])):
                    genre_number = int(genreDictB["data"][k]["id"])
                    genre.append(genreList[genre_number])

                rows = [[title, status, image, chCount, vCount, rating, synopsis, genre]]
                #       0       1       2       3       4       5       6       7
                writer.writerows(rows)
        offset = offset + 20
    mangaFile.close()


anime = multiprocessing.Process(target=getAnime)
manga = multiprocessing.Process(target=getManga)

if __name__ == '__main__':
    anime.start()
    manga.start()