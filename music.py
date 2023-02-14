"""
Music bot
- install google-api-python-client
- install ffmpeg, ytmdl
"""

import os
import googleapiclient.discovery
import data
import discord

MUSIC_QUEUE = []
IS_PLAYING = False
IS_PAUSED = False
VOICE_CHANNEL = None

def search_youtube(query):
    api_service_name = "youtube"
    api_version = "v3"
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=data.API_GOOGLE)
    query = query.replace(" ", "+")
    request = youtube.search().list(
        part="snippet",
        maxResults=1,
        type="video",
        q=query
    )
    response = request.execute()
    video_id = response['items'][0]['id']['videoId']
    video_title = response['items'][0]['snippet']['title']
    url = f"http://www.youtube.com/watch?v={video_id}"
    return (video_title, url)

async def handle_music_request(message, user_message):
    p_message = user_message.lower()
    if p_message == '/play':
        await play_music(message)
    elif p_message == '/pause':
        await pause_music(message)
    elif p_message[:4] == '/add':
        await add_music(message, p_message[4:])
    elif p_message[:7] == '/remove':
        await remove_music(message, p_message[7:])
    elif p_message == '/skip':
        await skip_music(message)
    elif p_message == '/queue':
        await show_queue(message)
    elif p_message == '/leave':
        await leave_channel(message)
    elif p_message == '/clear':
        await clear_list(message)

async def play_music(message):
    global IS_PLAYING, IS_PAUSED, VOICE_CHANNEL
    if message.author.voice is None: # if user not connected to voice channel
        await message.channel.send("`Please connect to a voice channel!`")
        return
    if VOICE_CHANNEL is None or VOICE_CHANNEL != message.author.voice.channel: # connect to user's voice channel
        VOICE_CHANNEL = message.author.voice.channel # Message => Author(Member) => Voice(VoiceState) => Channel(VoiceChannel)
        await VOICE_CHANNEL.connect() # VoiceChannel => connect()
    if IS_PAUSED: # music was paused
        IS_PAUSED = False
        IS_PLAYING = True
        message.guild.voice_client.resume()
        await message.channel.send("`Resuming music!`")
        return
    elif IS_PLAYING: # music already playing in channel
        await message.channel.send("`Music is already playing in voice channel!`")
        return
    elif len(MUSIC_QUEUE) == 0: # no more music in queue
        IS_PLAYING = False
        await message.channel.send("`No music in queue!`")
        return

    url_song_to_play = MUSIC_QUEUE[0][1]
    IS_PLAYING = True
    
    os.system("rm -f *.mp3")
    os.system(f"ytmdl --quiet --url {url_song_to_play} -o .")
    os.system("mv *.mp3 audio.mp3")
    del MUSIC_QUEUE[0]

    audio = "audio.mp3"
    source = discord.FFmpegPCMAudio(audio)
    message.guild.voice_client.play(source, after=lambda e: play_next())

def play_next():
    global IS_PLAYING, VOICE_CHANNEL
    if not IS_PLAYING:
        return
    if len(MUSIC_QUEUE) == 0:
        IS_PLAYING = False
        return
    url_song_to_play = MUSIC_QUEUE[0][1]
    os.system("rm -f *.mp3")
    os.system(f"ytmdl --quiet --url {url_song_to_play} -o .")
    os.system("mv *.mp3 audio.mp3")
    del MUSIC_QUEUE[0]

    audio = "audio.mp3"
    source = discord.FFmpegPCMAudio(audio)
    IS_PLAYING = True
    VOICE_CHANNEL.guild.voice_client.play(source, after=lambda e: play_next())

async def clear_list(message):
    global MUSIC_QUEUE
    MUSIC_QUEUE = []
    await message.channel.send("`Cleared list`")

async def remove_music(message, index):
    global MUSIC_QUEUE
    max_length = len(MUSIC_QUEUE) - 1
    try:
        index = int(index)
        assert index <= max_length
    except:
        await message.channel.send("`Please insert a valid integer!`")
        return
    deleted_item =  MUSIC_QUEUE.pop(index)
    await message.channel.send(f"`Removed {deleted_item[0]} from list!`")

async def pause_music(message):
    global IS_PAUSED, IS_PLAYING
    if not IS_PLAYING:
        await message.channel.send("`No music is playing!`")
        return 
    IS_PAUSED = True
    IS_PLAYING = False
    message.guild.voice_client.pause()
    await message.channel.send("`Music paused!`")

async def skip_music(message):
    global IS_PLAYING
    if not IS_PLAYING:
        await message.channel.send("`No music is playing!`")
        return
    IS_PLAYING = False
    message.guild.voice_client.pause()
    await message.channel.send("`Music skipped!`")

async def leave_channel(message):
    global IS_PLAYING, VOICE_CHANNEL
    voice_client = message.guild.voice_client
    if voice_client.is_connected(): # Message => Guild(server) => voice_client(VoiceProtocol)
        message.guild.voice_client.pause()
        IS_PLAYING = False
        VOICE_CHANNEL = None
        await voice_client.disconnect()
        await message.channel.send("`Leaved voice channel!`")
        return 
    else:
        await message.send("The bot is not connected to a voice channel.")
        return

async def add_music(message, query):
    if len(query) <= 1:
        await message.channel.send("`Please include music to add!`")
        return
    item = search_youtube(query)
    MUSIC_QUEUE.append(item)
    await message.channel.send(f"`{item[0]} added to queue!`")

async def show_queue(message):
    if len(MUSIC_QUEUE) == 0:
        await message.channel.send("`No music in queue!`")
        return
    response = "```"
    for index, item in enumerate(MUSIC_QUEUE):
        response += f"{index}. {item[0]}\n"
    response += "```"
    await message.channel.send(response)
