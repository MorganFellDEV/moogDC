# bot.py
import os
import requests
import sys
import prometheus_client
import discord
import discord.emoji
from discord.ext.commands import Bot
from discord.ext import tasks
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
import check_kermit
import give_bonk
import give_stonks
from FileStore import FileStore

load_dotenv()

# Setting up Prometheus
prometheus_client.start_http_server(10001)
prom_global_served_requests = prometheus_client.Gauge("all_served_requests", "All successfully served requests.")
prom_global_failed_requests = prometheus_client.Gauge("all_failed_requests", "All failed NovaBot requests.")

prom_shelly_user_count = prometheus_client.Gauge("shelly_user_count", "Shelly's server user count.")

# Setting up specific counters for Prometheus / Bot commands
prom_command_jumbo_requests = prometheus_client.Gauge("all_served_jumbo_requests", "All served n!jumbo requests.")
prom_command_miku_requests = prometheus_client.Gauge("all_served_miku_requests", "All served n!miku requests.")
prom_command_hug_requests = prometheus_client.Gauge("all_served_hug_requests", "All served n!hug requests.")
prom_command_kiss_requests = prometheus_client.Gauge("all_served_kiss_requests", "All served n!kiss requests.")
prom_command_poke_requests = prometheus_client.Gauge("all_served_poke_requests", "All served n!poke requests.")
prom_command_pat_requests = prometheus_client.Gauge("all_served_pat_requests", "All served n!pat requests.")
prom_command_lick_requests = prometheus_client.Gauge("all_served_lick_requests", "All served n!lick requests.")
prom_command_feed_requests = prometheus_client.Gauge("all_served_feed_requests", "All served n!feed requests.")
prom_command_cuddle_requests = prometheus_client.Gauge("all_served_cuddle_requests", "All served n!cuddle requests.")
prom_command_tickle_requests = prometheus_client.Gauge("all_served_tickle_requests", "All served n!tickle requests.")
prom_command_luna_requests = prometheus_client.Gauge("all_served_luna_requests", "All served n!luna requests.")
prom_command_bonk_requests = prometheus_client.Gauge("all_served_bonk_requests", "All served n!bonk requests.")
prom_command_stonks_requests = prometheus_client.Gauge("all_served_stonks_requests", "All served n!stonks requests.")
prom_command_serverinfo_requests = prometheus_client.Gauge("all_served_serverinfo_requests",
                                                           "All served n!serverinfo requests.")

TOKEN = os.getenv('DISCORD_TOKEN')
resources_location = os.getenv("NOVABOT_RESOURCES")

# TODO: Remove nd! when out of 'dev mode'.
bot = Bot(command_prefix="nd!")
fileStore = FileStore()


@tasks.loop(seconds=30.0)
async def get_user_count(ctx):
    prom_shelly_user_count.set(ctx.guild.member_count)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command()
async def botinit(ctx):
    if ctx.message.author.id == 109069934541144064:
        get_user_count.start(ctx)
        await ctx.send("``Bot initialising...``")
    else:
        pass


@bot.command(description="Posts the image of the emote sent to it.")
async def jumbo(ctx, emoji: discord.PartialEmoji):
    try:
        await ctx.send(file=get_emote.get_emote_image(ctx, emoji, fileStore))
        prom_command_jumbo_requests.inc()
        prom_global_served_requests.inc()
    except:
        print(sys.exc_info())
        prom_global_failed_requests.inc()


@bot.command(description="A homage to Nova, posts a random Miku image.")
async def miku(ctx):
    try:
        await ctx.send(file=discord.File(random_miku_image()))
        prom_command_miku_requests.inc()
        prom_global_served_requests.inc()
    except:
        print(sys.exc_info())
        prom_global_failed_requests.inc()


@bot.command(description="HUGS!!!!!")
async def hug(ctx):
    try:
        await ctx.send(give_hug.give_hug(ctx), file=discord.File(give_hug.random_hug_image()))
        prom_command_hug_requests.inc()
        prom_global_served_requests.inc()
    except:
        print(sys.exc_info())
        prom_global_failed_requests.inc()


@bot.command(description="SMOOCHES!!")
async def kiss(ctx):
    try:
        await ctx.send(give_kiss.give_kiss(ctx), file=discord.File(give_kiss.random_kiss_image()))
        prom_command_kiss_requests.inc()
        prom_global_served_requests.inc()
    except:
        print(sys.exc_info())
        prom_global_failed_requests.inc()


@bot.command(description="Annoy your friends!")
async def poke(ctx):
    try:
        await ctx.send(give_poke.give_poke(ctx, False), file=discord.File(give_poke.random_poke_image()))
        prom_command_poke_requests.inc()
        prom_global_served_requests.inc()
    except:
        print(sys.exc_info())
        prom_global_failed_requests.inc()


@bot.command(description="Boop!")
async def boop(ctx):
    try:
        await ctx.send(give_poke.give_poke(ctx, True), file=discord.File(give_poke.random_poke_image()))
        prom_command_poke_requests.inc()
        prom_global_served_requests.inc()
    except:
        print(sys.exc_info())
        prom_global_failed_requests.inc()


@bot.command(description="PATTING INTENSIFIES!")
async def pat(ctx):
    try:
        await ctx.send(give_pats.give_pat(ctx), file=discord.File(give_pats.random_pat_image()))
        prom_command_pat_requests.inc()
        prom_global_served_requests.inc()
    except:
        print(sys.exc_info())
        prom_global_failed_requests.inc()


@bot.command(description="LICC LICC LICC!!!")
async def lick(ctx):
    try:
        await ctx.send(give_licks.give_lick(ctx), file=discord.File(give_licks.random_lick_image()))
        prom_command_lick_requests.inc()
        prom_global_served_requests.inc()
    except:
        print(sys.exc_info())
        prom_global_failed_requests.inc()


@bot.command(description="Say AAAAAA!!")
async def feed(ctx):
    try:
        await ctx.send(give_food.give_food(ctx), file=discord.File(give_food.random_feed_image()))
        prom_command_feed_requests.inc()
        prom_global_served_requests.inc()
    except:
        print(sys.exc_info())
        prom_global_failed_requests.inc()


@bot.command(description="Maximum comfy mode!")
async def cuddle(ctx):
    try:
        await ctx.send(give_cuddles.give_cuddles(ctx), file=discord.File(give_cuddles.random_cuddle_image()))
        prom_command_cuddle_requests.inc()
        prom_global_served_requests.inc()
    except:
        print(sys.exc_info())
        prom_global_failed_requests.inc()


@bot.command(description="Tickle your enemies!")
async def tickle(ctx):
    try:
        await ctx.send(give_tickles.give_tickles(ctx), file=discord.File(give_tickles.random_tickle_image()))
        prom_command_tickle_requests.inc()
        prom_global_served_requests.inc()
    except:
        print(sys.exc_info())
        prom_global_failed_requests.inc()


@bot.command(description="Bonk!")
async def bonk(ctx):
    try:
        await ctx.send(give_bonk.give_bonk(ctx), file=discord.File(give_bonk.random_bonk_image()))
        prom_command_bonk_requests.inc()
        prom_global_served_requests.inc()
    except:
        print(sys.exc_info())
        prom_global_failed_requests.inc()

@bot.command(description="Stonks!")
async def stonks(ctx):
    try:
        await ctx.send(give_stonks.give_stonks(ctx), file=discord.File(give_bonk.random_bonk_image()))
        prom_command_stonks_requests.inc()
        prom_global_served_requests.inc()
    except:
        print(sys.exc_info())
        prom_global_failed_requests.inc()



@bot.command(description="What's that smell?")
async def luna(ctx):
    try:
        await ctx.send(file=discord.File(str(resources_location) + "/misc/luna_stinky.mp4"))
        prom_command_luna_requests.inc()
        prom_global_served_requests.inc()
    except:
        print(sys.exc_info())
        prom_global_failed_requests.inc()


@bot.command(description="Learn about the server!")
async def serverinfo(ctx):
    try:
        await ctx.send(file=discord.File(str(resources_location) + "/misc/rule_britannia.mp4"))
        prom_command_serverinfo_requests.inc()
        prom_global_served_requests.inc()
    except:
        print(sys.exc_info())
        prom_global_failed_requests.inc()


@bot.command(description="Secret!")
async def kermit(ctx):
    try:
        if ctx.message.author.id == 187715144556609538 or ctx.message.author.id == 109069934541144064 or ctx.message.author.id == 123133337387663360:
            await ctx.send(file=discord.File(check_kermit.random_kermit_image()))
        else:
            await ctx.send("Nice try.")
        prom_global_served_requests.inc()
    except:
        print(sys.exc_info())
        prom_global_failed_requests.inc()


bot.run(TOKEN)
