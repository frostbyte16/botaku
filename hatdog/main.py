import discord
from discord.ext import commands
import List_list
import random
import kitsu
import requests

client = commands.Bot(command_prefix='~')
search = kitsu.Client()
TOKEN = 'ODMzNTk3NDI1NTc0ODcxMDYw.YH0qGQ.bWJgnmd0l4pYAWoZKNZVcVPye8o'



@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_command_error(ctx, error):
    url = "https://giphy.p.rapidapi.com/v1/gifs/search"

    randOffset = random.randint(0, 100)
    querystring = {"api_key": "25UOV1WGwmIp6epexjskJeFFhupkIRYr", "q": "anime funny", "limit": "5",
                   "offset": {randOffset}}

    headers = {
        'x-rapidapi-key': "eebf03e5f6mshcaf6432163cf632p1fe268jsndd6b5a2a0507",
        'x-rapidapi-host': "giphy.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    poopoo = response.json()
    gif = poopoo['data'][0]['images']['original']['url']

    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
            title='**Command does not exist**',
            description='Please use ~commands to view all the available commands',
            colour=discord.Colour.dark_red()
        )
        embed.set_footer(text='BOT-aku commands')
        embed.set_author(name='BOTaku',
                         icon_url='https://cdn.discordapp.com/attachments/833625892751278082/834321459618512896/fmdrbd5ruah61.jpg')
        embed.set_image(
            url=gif)
        await ctx.send(embed=embed)

# command for hug
@client.command(aliases=['hug', 'hugs'])
async def _hugger(ctx):
    dere = List_list.Bot_say
    randomdere = random.choice(dere)
    await ctx.send(f"**HUGS** {ctx.author.mention} {randomdere} :heartbeat:")


# command list
@client.command(aliases=['commands'])
async def commandlist(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        title='Commands',
        description='These are all the available commands.',
        colour=discord.Colour.blue()
    )

    embed.set_footer(text='BOT-aku commands')
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/833625892751278082/834321459618512896/fmdrbd5ruah61.jpg')
    embed.set_author(name='BOTaku',
                     icon_url='https://cdn.discordapp.com/attachments/833625892751278082/834321459618512896/fmdrbd5ruah61.jpg')
    embed.add_field(name="**~genre or ~g**", value='displays all the available genre for anime and manga', inline=False)
    embed.add_field(name="**~animeName or ~an**", value='This searches based on anime name.', inline=True)
    embed.add_field(name="**~animeGenre or ~ag**", value='This searches based on anime genre.', inline=True)
    embed.add_field(name="**~randomAnime or ~ra**", value='displays random recommended anime.', inline=False)
    embed.add_field(name="**~mangaName or ~mn**", value='This searches based on manga name.', inline=True)
    embed.add_field(name="**~mangaGenre or ~mg**", value='This searches based on manga genre.', inline=True)
    embed.add_field(name="**~randomManga or ~rm**", value='displays random recommended manga.', inline=False)

    await ctx.send(embed=embed)


# display genre
@client.command(aliases=['genre', 'g'])
async def _displayGenre(ctx):
    genreM = List_list.printListManga
    genreA = List_list.printListAnime

    embed = discord.Embed(
        title='Genres',
        description='These are all the available genres',
        colour=discord.Colour.purple()
    )

    embed.set_footer(text='For more info, type ~commands to view commands list')
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/833625892751278082/834321459618512896/fmdrbd5ruah61.jpg')
    embed.set_image(url='https://pbs.twimg.com/media/Ex0DmZiWUAA1FGQ.jpg')
    embed.set_author(name='BOTaku',
                     icon_url='https://cdn.discordapp.com/attachments/833625892751278082/834321459618512896/fmdrbd5ruah61.jpg')
    embed.add_field(name='Anime', value=genreA, inline=True)
    embed.add_field(name='Manga', value=genreM, inline=True)

    await ctx.send(embed=embed)


# random anime
@client.command(aliases=['randomAnime', 'ra'])
async def _surpriseAnime(ctx):
    genreList = List_list.genreListAnime
    genre = random.choice(genreList)
    randOffset = random.randint(0, 100)

    api = f'https://kitsu.io/api/edge/anime?filter[categories]={genre}&sort=-averageRating&page[limit]=5&page[offset]={randOffset}'
    response = requests.get(api)

    animeDict = response.json()
    print(genre)
    print(randOffset)
    for i in range(5):
        animeTitle = str(animeDict["data"][i]["attributes"]["canonicalTitle"])
        animeImg = animeDict["data"][i]["attributes"]["posterImage"]["large"]
        animeStatus = animeDict["data"][i]["attributes"]["status"]
        animeEpCount = animeDict["data"][i]["attributes"]["episodeCount"]
        animeRating = animeDict["data"][i]["attributes"]["averageRating"]

        if animeStatus == 'current':
            animeStatus = 'ongoing'

        if animeDict["data"][i]["attributes"]["synopsis"] == '':
            animeSynopsis = ("Synopsis unavailable")
        else:
            animeSynopsis = str(animeDict["data"][i]["attributes"]["synopsis"])

        embed = discord.Embed(
            title=animeTitle,
            description=animeSynopsis
                        + '\n\n**Status**: ' + str(animeStatus)
                        + '\n**No. of Episodes**: ' + str(animeEpCount)
                        + '\n **Rating**: ' + str(animeRating),
            colour=discord.Colour.blue()
        )

        embed.set_footer(text='For more info, type ~commands to view commands list')
        embed.set_thumbnail(url=animeImg)
        embed.set_author(name='BOTaku',
                         icon_url='https://cdn.discordapp.com/attachments/833625892751278082/834321459618512896/fmdrbd5ruah61.jpg')

        await ctx.send(embed=embed)


# anime search genre
@client.command(aliases=['animeGenre', 'ag'])
async def _searchAnimegenre(ctx, arg):
    genre = arg
    genrelist = List_list.genreListAnime

    if genre in genrelist:
        randOffset = random.randint(0, 100)
        api = f'https://kitsu.io/api/edge/anime?filter[categories]={genre}&sort=-averageRating&page[limit]=5&page[offset]={randOffset}'
        response = requests.get(api)
        animeDict = response.json()

        print(genre)
        print(randOffset)
        for i in range(5):
            animeTitle = str(animeDict["data"][i]["attributes"]["canonicalTitle"])
            animeImg = animeDict["data"][i]["attributes"]["posterImage"]["large"]
            animeStatus = animeDict["data"][i]["attributes"]["status"]
            animeEpCount = animeDict["data"][i]["attributes"]["episodeCount"]
            animeRating = animeDict["data"][i]["attributes"]["averageRating"]

            if animeStatus == 'current':
                animeStatus = 'ongoing'

            if animeDict["data"][i]["attributes"]["synopsis"] == '':
                animeSynopsis = str("Synopsis unavailable")
            else:
                animeSynopsis = str(animeDict["data"][i]["attributes"]["synopsis"])

            embed = discord.Embed(
                title=animeTitle,
                description=animeSynopsis
                            + '\n\n**Status**: ' + str(animeStatus)
                            + '\n**No. of Episodes**: ' + str(animeEpCount)
                            + '\n **Rating**: ' + str(animeRating),
                colour=discord.Colour.blue()
            )

            embed.set_footer(text='For more info, type ~commands to view commands list')
            embed.set_thumbnail(url=animeImg)
            embed.set_author(name='BOTaku',
                             icon_url='https://cdn.discordapp.com/attachments/833625892751278082/834321459618512896/fmdrbd5ruah61.jpg')
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title='Genre not Available',
            description='Please use the command ~animeGenre to show all available genres',
            colour=discord.Colour.blue()
        )

        embed.set_footer(text='For more info, type ~commands to view commands list')
        embed.set_author(name='BOTaku',
                         icon_url='https://cdn.discordapp.com/attachments/833625892751278082/834321459618512896/fmdrbd5ruah61.jpg')
        await ctx.send(embed=embed)


# search anime by name
@client.command(aliases=['animeName', 'an'])
async def _animeName(ctx, arg):
    query = arg
    entries = await search.search('anime', query, limit=5)

    if not entries:
        await ctx.send(f'No entries found for "{query}"')
        return

    for i, anime in enumerate(entries, 1):
        animeTitle = anime.title
        animeStatus = anime.status
        animeSynopsis = anime.synopsis
        animeEpCount = anime.episode_count
        animeRating = anime.average_rating
        animeImg = anime.poster_image_url
        embed = discord.Embed(
            title=animeTitle,
            description=animeSynopsis
                        + '\n\n**Status**: ' + str(animeStatus)
                        + '\n**No. of Episodes**: ' + str(animeEpCount)
                        + '\n **Rating**: ' + str(animeRating),
            colour=discord.Colour.blue()
        )
        embed.set_footer(text='For more info, type ~commands to view commands list')
        embed.set_thumbnail(url=animeImg)
        embed.set_author(name='BOTaku',
                         icon_url='https://cdn.discordapp.com/attachments/833625892751278082/834321459618512896/fmdrbd5ruah61.jpg')

        await ctx.send(embed=embed)


# random manga search
@client.command(aliases=['randomManga', 'rm'])
async def _supriseManga(ctx):
    genreList = List_list.genreListManga
    genre = random.choice(genreList)
    randOffset = random.randint(0, 100)

    api = f'https://kitsu.io/api/edge/manga?filter[categories]={genre}&sort=-averageRating&page[limit]=5&page[offset]={randOffset}'
    response = requests.get(api)

    mangaDict = response.json()
    print(genre)
    print(randOffset)

    for i in range(5):

        if mangaDict["data"][i]["attributes"]["canonicalTitle"] == '':
            try:
                titleIndex0 = list(mangaDict["data"][i]["attributes"]["titles"])[0]
                titleIndex1 = list(mangaDict["data"][i]["attributes"]["titles"])[1]
            except:
                print('')

            if mangaDict["data"][i]["attributes"]["titles"][titleIndex0] == '':
                print(mangaDict["data"][i]["attributes"]["titles"][titleIndex1])
            else:
                print(mangaDict["data"][i]["attributes"]["titles"][titleIndex0])
        else:
            mangaTitle = str(mangaDict["data"][i]["attributes"]["canonicalTitle"])

        mangaImg = str(mangaDict["data"][i]["attributes"]["posterImage"]["large"])
        mangaStatus = str(mangaDict["data"][i]["attributes"]["status"])
        mangaChCount = str(mangaDict["data"][i]["attributes"]["chapterCount"])
        mangaVolCount = str(mangaDict["data"][i]["attributes"]["volumeCount"])
        mangaRating = str(mangaDict["data"][i]["attributes"]["averageRating"])

        if mangaStatus == "current":
            mangaStatus = "ongoing"

        if mangaDict["data"][i]["attributes"]["synopsis"] == '':
            mangaSynopsis = str("Synopsis unavailable")
        else:
            mangaSynopsis = str(mangaDict["data"][i]["attributes"]["synopsis"])

        embed = discord.Embed(
            title=mangaTitle,
            description=mangaSynopsis
                        + '\n\n**Status**: ' + str(mangaStatus)
                        + '\n**No. of Chapters**: ' + str(mangaChCount)
                        + '\n**No. of Volumes**: ' + str(mangaVolCount)
                        + '\n**Average Rating**: ' + str(mangaRating),
            colour=discord.Colour.red()
        )

        embed.set_footer(text='BOT-aku commands')
        embed.set_thumbnail(url=mangaImg)
        embed.set_author(name='BOTaku',
                         icon_url='https://cdn.discordapp.com/attachments/833625892751278082/834321459618512896/fmdrbd5ruah61.jpg')

        await ctx.send(embed=embed)
        print(i + 1)


# manga search genre
@client.command(aliases=['mangaGenre', 'mg'])
async def _mangaGenre(ctx, arg):
    genre = arg
    genrelist = List_list.genreListManga

    if genre in genrelist:
        randOffset = random.randint(0, 100)
        api = f'https://kitsu.io/api/edge/manga?filter[categories]={genre}&sort=-averageRating&page[limit]=5&page[offset]={randOffset}'
        response = requests.get(api)
        mangaDict = response.json()
        print(genre)
        print(randOffset)
        for i in range(5):
            if mangaDict["data"][i]["attributes"]["canonicalTitle"] == '':
                try:
                    titleIndex0 = list(mangaDict["data"][i]["attributes"]["titles"])[0]
                    titleIndex1 = list(mangaDict["data"][i]["attributes"]["titles"])[1]
                except:
                    print('')

                if mangaDict["data"][i]["attributes"]["titles"][titleIndex0] == '':
                    print(mangaDict["data"][i]["attributes"]["titles"][titleIndex1])
                else:
                    print(mangaDict["data"][i]["attributes"]["titles"][titleIndex0])
            else:
                mangaTitle = str(mangaDict["data"][i]["attributes"]["canonicalTitle"])

            mangaImg = str(mangaDict["data"][i]["attributes"]["posterImage"]["large"])
            mangaChCount = str(mangaDict["data"][i]["attributes"]["chapterCount"])
            mangaVolCount = str(mangaDict["data"][i]["attributes"]["volumeCount"])
            mangaRating = str(mangaDict["data"][i]["attributes"]["averageRating"])
            mangaStatus = str(mangaDict["data"][i]["attributes"]["status"])

            if mangaStatus == "current":
                mangaStatus = "ongoing"

            if mangaDict["data"][i]["attributes"]["synopsis"] == '':
                mangaSynopsis = str("Synopsis unavailable")
            else:
                mangaSynopsis = str(mangaDict["data"][i]["attributes"]["synopsis"])

            embed = discord.Embed(
                title=mangaTitle,
                description=mangaSynopsis
                            + '\n\n**Status**: ' + str(mangaStatus)
                            + '\n**No. of Chapters**: ' + str(mangaChCount)
                            + '\n**No. of Volumes**: ' + str(mangaVolCount)
                            + '\n **Rating**: ' + str(mangaRating),
                colour=discord.Colour.red()
            )

            embed.set_footer(text='For more info, type ~commands to view commands list')
            embed.set_thumbnail(url=mangaImg)
            embed.set_author(name='BOTaku',
                             icon_url='https://cdn.discordapp.com/attachments/833625892751278082/834321459618512896/fmdrbd5ruah61.jpg')
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title='Genre not Available',
            description='Please use the command ~mangaGenre to show all available manga genres',
            colour=discord.Colour.red()
        )

        embed.set_footer(text='For more info, type ~commands to view commands list')
        embed.set_author(name='BOTaku',
                         icon_url='https://cdn.discordapp.com/attachments/833625892751278082/834321459618512896/fmdrbd5ruah61.jpg')
        await ctx.send(embed=embed)


# search manga by name
@client.command(aliases=['mangaName', 'mn'])
async def _mangaName(ctx, arg):
    query = arg
    entries = await search.search('manga', query, limit=5)

    if not entries:
        await ctx.send(f'No entries found for "{query}"')
        return

    for i, manga in enumerate(entries, 1):
        mangaTitle = manga.title
        mangaStatus = manga.status
        mangaSynopsis = manga.synopsis
        mangaChCount = manga.chapter_count
        mangaVolCount = manga.volume_count
        mangaRating = manga.average_rating
        mangaImg = manga.poster_image_url

        embed = discord.Embed(
            title=mangaTitle,
            description=mangaSynopsis
                        + '\n\n**Status**: ' + str(mangaStatus)
                        + '\n**No. of Chapters**: ' + str(mangaChCount)
                        + '\n**No. of Volumes**: ' + str(mangaVolCount)
                        + '\n **Rating**: ' + str(mangaRating),
            colour=discord.Colour.red()
        )

        embed.set_footer(text='For more info, type ~commands to view commands list')
        embed.set_thumbnail(url=mangaImg)
        embed.set_author(name='BOTaku',
                         icon_url='https://cdn.discordapp.com/attachments/833625892751278082/834321459618512896/fmdrbd5ruah61.jpg')

        await ctx.send(embed=embed)


# @client.command(aliases=['mood'])
# async def _animeMood(ctx):
#     emotionsList = List_list.emotions
#     embed = discord.Embed(
#         title='Commands',
#         description='These are all the available commands.',
#         colour=discord.Colour.blue()
#     )
#
#     embed.set_footer(text='BOT-aku commands')
#     embed.set_thumbnail(
#         url='https://cdn.discordapp.com/attachments/833625892751278082/834321459618512896/fmdrbd5ruah61.jpg')
#     embed.set_author(name='BOTaku',
#                      icon_url='https://cdn.discordapp.com/attachments/833625892751278082/834321459618512896/fmdrbd5ruah61.jpg')
#     embed.add_field(name="**Question 1**", value='Are you overjoyed?', inline=False)
#     embed.add_field(name="**Question 2**", value='Do you want to get bonked?', inline=False)
#     embed.add_field(name="**Question 3**", value='Do you want to cry?', inline=False)
#     embed.add_field(name="**Question 4**", value='Do you want a life-guide', inline=False)
#     embed.add_field(name="**Question 5**", value='Do you want revenge?', inline=False)
#     embed.add_field(name="**Question 6**", value='Do you want to get hit by Truck-kun?', inline=False)
#     embed.add_field(name="**Question 8**", value='Do you want anxiety?', inline=False)
#     embed.add_field(name="**Question 9**", value='Do you want to use your brain?', inline=False)
#
#     await ctx.send(embed=embed)
#
#
#
#
#     titleList = List_list.animeEmotionList
#     title = random.choice(titleList)
#     api = f'https://kitsu.io/api/edge/anime?filter[text]={title}'
#     response = requests.get(api)
#     emotionDict = response.json()


client.run(TOKEN)
