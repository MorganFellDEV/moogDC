import requests
import os
import discord
import glob


def get_emote_image(ctx, emoji: discord.PartialEmoji):
    if emoji.animated:
        parsed_url = "https://cdn.discordapp.com/emojis/" + str(emoji.id) + ".gif"
        request_file = requests.get(parsed_url)
        open("/var/www/html/resources/emotes_grabbed/temp_emote.gif", 'wb').write(request_file.content)
        return discord.File("/var/www/html/resources/emotes_grabbed/temp_emote.gif")

    else:
        parsed_url = "https://cdn.discordapp.com/emojis/" + str(emoji.id) + ".png"
        request_file = requests.get(parsed_url)
        open("/var/www/html/resources/emotes_grabbed/temp_emote.png", 'wb').write(request_file.content)
        return discord.File("/var/www/html/resources/emotes_grabbed/temp_emote.png")


def cleanup_emote():
    for files_found in glob.glob("/var/www/html/resources/emotes_grabbed/"):
        os.remove(files_found)
