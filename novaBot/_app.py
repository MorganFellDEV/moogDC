# bot.py
import os
import random

import discord
from dotenv import load_dotenv
from load_mikus import random_miku_image
from give_hug import random_hug_image
from give_kiss import random_kiss_image

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

    if message.content.startswith('n!miku'):
        await message.channel.send(file=discord.File(random_miku_image()))

    elif message.content.startswith('n!hug'):

        hug_string = ""

        for incrementer, value in enumerate(message.mentions):

            if incrementer == len(message.mentions) - 1:
                hug_string += str(message.mentions[incrementer].name)
                hug_string += "!"
                break
            else:
                hug_string += str(message.mentions[incrementer].name)
                hug_string += " and "

            incrementer += 1

        await message.channel.send(message.author.name + " hugs " + hug_string)
        await message.channel.send(file=discord.File(random_hug_image()))

    elif message.content.startswith('n!kiss'):

        kiss_string = ""

        for incrementer, value in enumerate(message.mentions):

            if incrementer == len(message.mentions) - 1:
                kiss_string += str(message.mentions[incrementer].name)
                kiss_string += "!"
                break
            else:
                kiss_string += str(message.mentions[incrementer].name)
                kiss_string += " and "

            incrementer += 1

        await message.channel.send(message.author.name + " kisses " + kiss_string)
        await message.channel.send(file=discord.File(random_hug_image()))

    elif message.content.startswith('n!showerror'):
        await message.channel.send("```" + str(discord.DiscordException) + "```")
        raise discord.DiscordException


client.run(TOKEN)
