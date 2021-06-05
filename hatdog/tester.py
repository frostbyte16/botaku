import requests
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

for items in genreList:
    print(items)