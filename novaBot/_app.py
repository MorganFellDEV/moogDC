# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    miku = [
        'no links yet',
        'this is supposed to be a link!',

    ]

    if message.content == 'n!miku':
        response = random.choice(miku)
        await message.channel.send(response)
    elif message.content == 'n!showerror':
        raise discord.DiscordException


client.run("lol no token for you")