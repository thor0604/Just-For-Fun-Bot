"""Defines the behavior of our bot"""

import discord
import responses
import music
import data


async def send_message(message, user_message, specific):
    try:
        if specific is True:
            response = responses.handle_response_standard(user_message)
        else:
            response = responses.handle_response_random(message, user_message)
        if response[0] is True:
            await message.channel.send(response[1])

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = data.TOKEN
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '!':
            await send_message(message, user_message, specific=True)
        elif user_message[0] == '/':
            await music.handle_music_request(message, user_message)
        else:
            await send_message(message, user_message, specific=False)

    client.run(TOKEN)