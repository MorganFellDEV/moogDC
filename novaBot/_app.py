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
import get_emote
import give_pats
import give_licks
import give_food
import give_cuddles
import give_tickles

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
resources_location = os.getenv("NOVABOT_RESOURCES")

# client = discord.Client()
# TODO: Remove nd! when out of 'dev mode'.
bot = Bot(command_prefix="n!")


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command()
@bot.description("Posts the image of the emote sent to it")
async def jumbo(ctx, emoji: discord.PartialEmoji):
    await ctx.send(file=get_emote.get_emote_image(ctx, emoji))
    get_emote.cleanup_emote()


@bot.command()
@bot.description("An homage to Nova, posts a random Miku image.")
async def miku(ctx):
    await ctx.send(file=discord.File(random_miku_image()))


@bot.command()
@bot.description("HUGS!!!!!")
async def hug(ctx):
    await ctx.send(give_hug.give_hug(ctx))
    await ctx.send(file=discord.File(give_hug.random_hug_image()))


@bot.command()
@bot.description("Smooches!")
async def kiss(ctx):
    await ctx.send(give_kiss.give_kiss(ctx))
    await ctx.send(file=discord.File(give_kiss.random_kiss_image()))


@bot.command()
@bot.description("Annoy your friends!")
async def poke(ctx):
    await ctx.send(give_poke.give_poke(ctx, False))
    await ctx.send(file=discord.File(give_poke.random_poke_image()))


@bot.command()
@bot.description("Boop!")
async def boop(ctx):
    await ctx.send(give_poke.give_poke(ctx, True))
    await ctx.send(file=discord.File(give_poke.random_poke_image()))


@bot.command()
@bot.description("PATTING INTENSIFIES")
async def pat(ctx):
    await ctx.send(give_pats.give_pat(ctx))
    await ctx.send(file=discord.File(give_pats.random_pat_image()))


@bot.command()
@bot.description("Lick?")
async def lick(ctx):
    await ctx.send(give_licks.give_lick(ctx))
    await ctx.send(file=discord.File(give_licks.random_lick_image()))


@bot.command()
@bot.description("Say AAAAAAA")
async def feed(ctx):
    await ctx.send(give_food.give_food(ctx))
    await ctx.send(file=discord.File(give_food.random_feed_image()))


@bot.command()
@bot.description("Maximum comfy mode")
async def cuddle(ctx):
    await ctx.send(give_cuddles.give_cuddles(ctx))
    await ctx.send(file=discord.File(give_cuddles.random_cuddle_image()))


@bot.command()
@bot.description("Tickle your enemies!")
async def tickle(ctx):
    await ctx.send(give_tickles.give_tickles(ctx))
    await ctx.send(file=discord.File(give_tickles.random_tickle_image()))


@bot.command()
@bot.description("What's that smell?")
async def luna(ctx):
    await ctx.send(file=discord.File(str(resources_location) + "/misc/luna_stinky.mp4"))


bot.run(TOKEN)
