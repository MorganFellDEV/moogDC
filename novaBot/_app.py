# bot.py
import os
import random

import discord
from dotenv import load_dotenv
from load_mikus import load_miku_images

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

    if message.content == 'n!miku':
        miku_pics = load_miku_images()
        await message.channel.send(file=discord.File("/var/www/html/resources/miku/" + random.choice(miku_pics)))
    elif message.content == 'n!showerror':
        await message.channel.send("'''"+discord.DiscordException+"'''")
        raise discord.DiscordException

client.run("lol no token for you")
