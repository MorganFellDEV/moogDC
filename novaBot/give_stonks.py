from os import listdir
from os.path import isfile, join
import random
import os

resources_location = os.getenv("NOVABOT_RESOURCES")


def random_stonks_image():
    onlyfiles = [f for f in listdir(str(resources_location) + "/stonks/") if
                 isfile(join(str(resources_location) + "/stonks/", f))]
    file = str((str(resources_location) + "/stonks/" + random.choice(onlyfiles)))
    return file


def give_stonks(ctx):
    stonks_string = ""

    for incrementer, value in enumerate(ctx.message.mentions):
        print("length list " + str(len(ctx.message.mentions)))
        if len(ctx.message.mentions) > 2:
            print("more than two people")
            if incrementer == 0:
                # first person
                stonks_string += str(ctx.message.mentions[incrementer].name)
                pass
            elif incrementer != len(ctx.message.mentions) - 1:
                stonks_string += ", " + str(ctx.message.mentions[incrementer].name)
            else:
                stonks_string += " and " + str(ctx.message.mentions[incrementer].name)

        else:
            if incrementer == 0:
                # first person
                stonks_string += str(ctx.message.mentions[incrementer].name)
                pass
            elif incrementer != len(ctx.message.mentions):
                stonks_string += " and " + str(ctx.message.mentions[incrementer].name)

    return ctx.message.author.name + " stonks " + stonks_string + "!"


