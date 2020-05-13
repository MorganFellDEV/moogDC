# bot.py
import os
import random

import discord
from dotenv import load_dotenv
from load_mikus import load_miku_images

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

miku_pics = load_miku_images()
print (miku_pics)



@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'n!miku':
        response = random.choice("https://cloud.moorgaan.dev/resources/miku/"+miku_pics)
        await message.channel.send(response)
    elif message.content == 'n!showerror':
        raise discord.DiscordException

client.run("lol no token for you")
