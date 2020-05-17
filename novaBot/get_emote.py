import requests
import os
import discord
import glob

resources_location = os.getenv('NOVABOT_RESOURCES')


def get_emote_image(ctx, emoji: discord.PartialEmoji):
    if emoji.animated:
        parsed_url = "https://cdn.discordapp.com/emojis/" + str(emoji.id) + ".gif"
        request_file = requests.get(parsed_url)
        open(str(resources_location) + "/emotes_grabbed/temp_emote.gif", 'wb').write(request_file.content)
        return discord.File(str(resources_location) + "/emotes_grabbed/temp_emote.gif")

    else:
        parsed_url = "https://cdn.discordapp.com/emojis/" + str(emoji.id) + ".png"
        request_file = requests.get(parsed_url)
        open(str(resources_location) + "/emotes_grabbed/temp_emote.png", 'wb').write(request_file.content)
        return discord.File(str(resources_location) + "/emotes_grabbed/temp_emote.png")


def cleanup_emote():
    for files_found in glob.glob(str(resources_location) + "/emotes_grabbed/*"):
        os.remove(files_found)
