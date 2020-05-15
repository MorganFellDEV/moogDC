# bot.py
import os
import requests
import discord
import discord.emoji
from discord.ext.commands import Bot
from dotenv import load_dotenv
from load_mikus import random_miku_image
import give_hug
import give_kiss
import give_poke

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

# client = discord.Client()
bot = Bot(command_prefix="n!")


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command()
async def jumbo(ctx, emoji: discord.PartialEmoji):
    emoji_url = str(emoji.id)
    if emoji.animated:
        parsed_url = "https://cdn.discordapp.com/emojis/" + emoji_url + ".gif"
    else:
        parsed_url = "https://cdn.discordapp.com/emojis/" + emoji_url + ".png"
    request_file = requests.get(parsed_url)
    open("/var/www/html/resources/emotes_grabbed/temp_emote", 'wb').write(request_file.content)
    await ctx.send(file=discord.File("/var/www/html/resources/emotes_grabbed/temp_emote"))


@bot.command()
async def miku(ctx):
    await ctx.send(file=discord.File(random_miku_image()))


@bot.command()
async def hug(ctx):
    await ctx.send(give_hug.give_hug(ctx))
    await ctx.send(file=discord.File(give_hug.random_hug_image()))


@bot.command()
async def kiss(ctx):
    await ctx.send(give_kiss.give_kiss(ctx))
    await ctx.send(file=discord.File(give_kiss.random_kiss_image()))


@bot.command()
async def poke(ctx):
    await ctx.send(give_poke.give_poke(ctx, False))
    await ctx.send(file=discord.File(give_poke.random_poke_image()))


@bot.command()
async def boop(ctx):
    await ctx.send(give_poke.give_poke(ctx, True))
    await ctx.send(file=discord.File(give_poke.random_poke_image()))


bot.run(TOKEN)
