import csv
import requests
import json
import pandas as pd

offset = 0

api = f'https://kitsu.io/api/edge/anime?&page[limit]=20&page[offset]={offset}'
response = requests.get(api)
animeDict = response.json()

animeFile = open('anime.csv', 'w', encoding='utf-8')

writer = csv.writer(animeFile)
for key, value in animeDict.items():
    writer.writerow([key, value])

animeFile.close()