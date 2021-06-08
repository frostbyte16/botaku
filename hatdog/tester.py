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

print(genreList)
count = 1
genre1 = []
genre2 = []
genre3 = []
genre4 = []
for i in range(len(genreList)):
    if count == 1:
        genre1.append(genreList[i])
    elif count == 2:
        genre2.append(genreList[i])
    elif count == 3:
        genre3.append(genreList[i])
    else:
        genre4.append(genreList[i])
        count = 0
    count = count + 1
print(genre1)
print(genre2)
print(genre3)
print(genre4)
# print(len(genreList))