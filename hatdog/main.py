import discord
from discord.ext import commands
import List_list
import random
import requests
import json

prefix = ''

def get_prefix(client, message):
    global prefix
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
        prefix = prefixes[str(message.guild.id)]
    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix)

TOKEN = 'ODMzNTk3NDI1NTc0ODcxMDYw.YH0qGQ.bWJgnmd0l4pYAWoZKNZVcVPye8o'



# changes prefix
@client.command()
@commands.has_permissions(administrator=True)
async def changeprefix(ctx, new_prefix):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = new_prefix

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f)
    await ctx.send(f"BOTaku prefix has been changed to {new_prefix}")


@client.event
async def on_message(msg):
    try:
        if msg.mentions[0] == client.user:
            with open("prefixes.json", "r") as f:
                prefixes = json.load(f)

            prfx = prefixes[str(msg.guild.id)]

            await msg.channel.send(f"BOTaku prefix has been changed to{prfx}")
    except:
        pass

    await client.process_commands(msg)

# sets default prefix
@client.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    prefixes[str(guild.id)] = "~"
    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f)


@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))


# command does not exist
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
            description=f'Please use {prefix}commands to view all the available commands',
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


# displays commands list
@client.command(aliases=['commands'])
async def commandlist(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        title='Commands',
        description='These are all the available commands.',
        colour=discord.Colour.purple()
    )

    embed.set_footer(text='BOT-aku commands')
    embed.set_thumbnail(
        url='https://i.pinimg.com/originals/9b/42/5d/9b425d00289b5d409ba584b5f4c84c55.gif')
    embed.set_author(name=ctx.author.display_name,
                     icon_url=ctx.author.avatar_url)
    embed.add_field(name=f"**{prefix}genre or {prefix}g**", value='Displays list of genre available', inline=False)
    embed.add_field(name=f"**{prefix}recommendAnime *title* or {prefix}a *title* **",
                    value='Recommends anime based on title.', inline=False)
    embed.add_field(name=f"**{prefix}recommendManga *title* or {prefix}m *title* **",
                    value='Recommends manga based on title.', inline=True)
    embed.add_field(name=f"**{prefix}animeGenre *genre* or {prefix}ag *genre* **",
                    value='Recommends anime based on genre.', inline=False)
    embed.add_field(name=f"**{prefix}mangaGenre *genre* or {prefix}mg *genre* **",
                    value='Recommends manga based on genre.', inline=True)
    embed.add_field(name=f"**{prefix}randomAnime or {prefix}ra**", value='Recommends random anime.', inline=False)
    embed.add_field(name=f"**{prefix}randomManga or {prefix}rm**", value='Recommends random manga.', inline=True)
    embed.add_field(name=f"**{prefix}hug or {prefix}hugs**", value='Botaku hugs user.', inline=False)

    await ctx.send(embed=embed)

# displays all genre
@client.command(aliases=['genre', 'g'])
async def _displayGenre(ctx):
    genre1 = List_list.colA
    genre2 = List_list.colB
    genre3 = List_list.colC

    embed = discord.Embed(
        title='Genres',
        description='These are all the available genres',
        colour=discord.Colour.purple()
    )

    embed.set_footer(text=f'For more info, type {prefix}commands to view commands list')
    embed.set_thumbnail(
        url='https://i.pinimg.com/originals/1e/91/49/1e9149f3e0f1edeae80aa1e90baa74de.png')
    embed.set_author(name=ctx.author.display_name,
                     icon_url=ctx.author.avatar_url)
    embed.add_field(name='List of Genres', value=genre1, inline=True)
    embed.add_field(name='\u200b', value=genre2, inline=True)
    embed.add_field(name='\u200b', value=genre3, inline=True)

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
@commands.cooldown(1, 2, commands.BucketType.user)
async def _searchAnimegenre(ctx, *arg):
    if not arg:
        embed = discord.Embed(
            title='No genre entered',
            description=f'Try adding a genre with that command. For example: {prefix}animeGenre comedy',
            colour=discord.Colour.dark_red()
        )

        embed.set_footer(text=f'For more info, type {prefix}commands to view commands list')
        embed.set_author(name=ctx.author.display_name,
                         icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        genre = arg
        genrelist = List_list.genreList

        if genre in genrelist:
            x = ga.recommend_anime(genre)
            recoList = x.values.tolist()

            for i in range(5):
                anime_Titles = recoList[i][0]
                anime_Status = recoList[i][2]
                anime_epCount = recoList[i][4]
                anime_Image = recoList[i][3]
                anime_Ratings = recoList[i][5]
                anime_Synopsis = recoList[i][7]

                embed = discord.Embed(
                    title=anime_Titles,
                    description=anime_Synopsis
                                + '\n\n**Status**: ' + str(anime_Status)
                                + '\n**No. of Episodes**: ' + str(int(anime_epCount))
                                + '\n **Rating**: ' + str(anime_Ratings),
                    colour=discord.Colour.blue()
                )
                embed.set_footer(text=f'For more info, type {prefix}commands to view commands list')
                embed.set_thumbnail(url=anime_Image)
                embed.set_author(name=ctx.author.display_name,
                                 icon_url=ctx.author.avatar.url)
                await ctx.send(embed=embed)

        else:
            embed = discord.Embed(
                title='Genre not Available',
                description=f'Please use the command {prefix}genre to show all available genres',
                colour=discord.Colour.dark_red()
            )

            embed.set_footer(text=f'For more info, type {prefix}commands to view commands list')
            embed.set_author(name=ctx.author.display_name,
                             icon_url=ctx.author.avatar_url)
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

    manga_Titles = ranManga[0]
    manga_Status = ranManga[1]
    manga_chCount = ranManga[3]
    manga_vCount = ranManga[4]
    manga_Image = ranManga[2]
    manga_Ratings = ranManga[5]
    manga_Synopsis = ranManga[7]
    embed = discord.Embed(
        title=manga_Titles,
        description=manga_Synopsis
                    + '\n\n**Status**: ' + str(manga_Status)
                    + '\n**No. of Chapters**: ' + str(int(manga_chCount))
                    + '\n**No. of Volumes**: ' + str(int(manga_vCount))
                    + '\n **Rating**: ' + str(manga_Ratings),
        colour=discord.Colour.red()
    )
    embed.set_footer(text=f'For more info, type {prefix}commands to view commands list')
    embed.set_thumbnail(url=manga_Image)
    embed.set_author(name=ctx.author.display_name,
                     icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


# recommends manga based on genre
@client.command(aliases=['mangaGenre', 'mg'])
@commands.cooldown(1, 2, commands.BucketType.user)
async def _mangaGenre(ctx, *arg):
    if not arg:
        embed = discord.Embed(
            title='No genre entered',
            description=f'Try adding a genre with that command. For example: {prefix}mangaGenre comedy',
            colour=discord.Colour.dark_red()
        )

        embed.set_footer(text=f'For more info, type {prefix}commands to view commands list')
        embed.set_author(name=ctx.author.display_name,
                         icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        genre = arg
        genrelist = List_list.genreList

        if genre in genrelist:
            x = gm.recommend_manga(genre)
            recoList = x.values.tolist()
            print(recoList)
            for i in range(5):
                manga_Titles = recoList[i][0]
                manga_Status = recoList[i][1]
                manga_chCount = recoList[i][3]
                manga_vCount = recoList[i][4]
                manga_Image = recoList[i][2]
                manga_Ratings = recoList[i][5]
                manga_Synopsis = recoList[i][7]
                embed = discord.Embed(
                    title=manga_Titles,
                    description=manga_Synopsis
                                + '\n\n**Status**: ' + str(manga_Status)
                                + '\n**No. of Chapters**: ' + str(int(manga_chCount))
                                + '\n**No. of Volumes**: ' + str(int(manga_vCount))
                                + '\n **Rating**: ' + str(manga_Ratings),
                    colour=discord.Colour.red()
                )
                embed.set_footer(text=f'For more info, type {prefix}commands to view commands list')
                embed.set_thumbnail(url=manga_Image)
                embed.set_author(name=ctx.author.display_name,
                                 icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title='Genre not Available',
                description=f'Please use the command {prefix}genre to show all available genres',
                colour=discord.Colour.dark_red()
            )

            embed.set_footer(text=f'For more info, type {prefix}commands to view commands list')
            embed.set_author(name=ctx.author.display_name,
                             icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)


# recommends manga based on title
@client.command(aliases=['recommendManga', 'm'])
@commands.cooldown(1, 2, commands.BucketType.user)
async def _recomanga(ctx, *arg):
    if not arg:
        embed = discord.Embed(
            title='No manga title entered',
            description=f'Try adding a title with that command. For example: {prefix}recommendManga Hunter x Hunter',
            colour=discord.Colour.dark_red()
        )

        embed.set_footer(text=f'For more info, type {prefix}commands to view commands list')
        embed.set_author(name=ctx.author.display_name,
                         icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        query = arg
        recoList = await w.manga_search(query)
        if len(recoList) > 0:
            for i in range(5):
                manga_Titles = recoList[i][0]
                manga_Status = recoList[i][1]
                manga_chCount = recoList[i][2]
                manga_vCount = recoList[i][3]
                manga_Image = recoList[i][4]
                manga_Ratings = recoList[i][5]
                manga_Synopsis = recoList[i][6]
                embed = discord.Embed(
                    title=manga_Titles,
                    description=manga_Synopsis
                                + '\n\n**Status**: ' + str(manga_Status)
                                + '\n**No. of Chapters**: ' + str(int(manga_chCount))
                                + '\n**No. of Volumes**: ' + str(int(manga_vCount))
                                + '\n **Rating**: ' + str(manga_Ratings),
                    colour=discord.Colour.red()
                )
                embed.set_footer(text=f'For more info, type {prefix}commands to view commands list')
                embed.set_thumbnail(url=manga_Image)
                embed.set_author(name=ctx.author.display_name,
                                 icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title='Manga Title Not Available',
                description=f'Please use the command {prefix}animeGenre to show all available genres',
                colour=discord.Colour.red()
            )

            embed.set_footer(text=f'For more info, type {prefix}commands to view commands list')
            embed.set_author(name='BOTaku',
                             icon_url='https://cdn.discordapp.com/attachments/833625892751278082/834321459618512896/fmdrbd5ruah61.jpg')
            await ctx.send(embed=embed)



client.run(TOKEN)
