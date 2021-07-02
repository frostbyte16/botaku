# Botaku: The Anime Recommender Bot

## About
A simple discord bot that provides anime and manga recommendations based on watched anime or genre using the following packages:
 * discord.py 
 * scikit-learn
 * pandas
 * kitsu-wrapper

The Database is created from the kitsu API link: https://kitsu.docs.apiary.io/#
 
## Instructions
For the bot to run install the following packages:
 * discord.py
 * scikit-learn
 * pandas
 * kitsu-wrapper

For the database building install the following:
 * requests
 * Beautiful Soup

 ### The bot
 1. Open the file main.py and there you will see the token variable. The token variable is where you will insert your token taken from the official Discord develeoper portal
 2. run main.py 

 In this scenario, the bot will run until you close your python IDE. In order for it to run 24/7 you need to use a cloud machine server (Amazon AWS, Heroku, etc.) 
 
 ### The Data Collector
 Open getData.py and run it. after running you should see that two .csv file are created named anime.csv and manga.csv this two files is where the data from the api will be written. You will also notice that in your console there are numbers getting printed in there, it is the number of iteration in from Kitsu API. 


## The Developers
This discord bot was created by: <br/>
<img src="https://static.wikia.nocookie.net/gensin-impact/images/d/d4/Item_Primogem.png/revision/latest?cb=20201117071158" height="15" width="15"> 
**Freemogems plz** <br/>
<img src="https://preview.redd.it/blbm0bfqqyv51.png?width=960&crop=smart&auto=webp&s=cf42f1b7b57b1ea2f48c8b9fe5b698c24e4abfc0" height="15" width="15">
 Back-end Developer: _**Carl Camara**_ <br/>
<img src="https://preview.redd.it/z1c5jjeqqyv51.png?width=960&crop=smart&auto=webp&s=540d90e069704dc4d7dfeb3632f2ac5384ef3b3f" height="15" width="15">
 Front-end Developer: _**Brendan Canoy**_<br/>
<img src="https://preview.redd.it/iaty0jeqqyv51.png?width=960&crop=smart&auto=webp&s=ce805f300bdca81a7c652c8366b0a3ca057f39f8" height="15" width="15">
 Project Manager: _**Vince dela Peña**_<br/>

## Discord Bot
<div align="center"><img src="https://cdn.discordapp.com/attachments/853265856233865246/853571628130500608/unknown.png"></div>

### Features

You can get recommendations through three different ways:

* Anime/Manga Title: Get recommendations related to an anime or manga title.
<img src="https://cdn.discordapp.com/attachments/835427579284160532/853572003230646292/unknown.png">
<img src="https://cdn.discordapp.com/attachments/835427579284160532/853572638765219880/unknown.png">

* Anime/Manga Genre: Get recommendations based on an anime or manga genre.
<img src="https://cdn.discordapp.com/attachments/835427579284160532/853573311435112479/unknown.png">
<img src="https://cdn.discordapp.com/attachments/835427579284160532/853573712742055976/unknown.png">

* Random: Get a random anime or manga recommendation.
<img src="https://cdn.discordapp.com/attachments/835427579284160532/853574389500084234/unknown.png">
<img src="https://cdn.discordapp.com/attachments/835427579284160532/853574701988315146/unknown.png">

### Commands
<img src="https://cdn.discordapp.com/attachments/835427579284160532/853574972290236416/unknown.png">
