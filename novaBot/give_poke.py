from os import listdir
from os.path import isfile, join
import random
import os

resources_location = os.getenv('NOVABOT_RESOURCES')


def random_poke_image():
    onlyfiles = [f for f in listdir(str(resources_location) + "/poke/") if
                 isfile(join(str(resources_location) + "/poke/", f))]
    file = str((resources_location + "/poke/" + random.choice(onlyfiles)))
    return file


def give_poke(ctx,to_boop):
    poke_string = ""

    for incrementer, value in enumerate(ctx.message.mentions):
        print("length list " + str(len(ctx.message.mentions)))
        if len(ctx.message.mentions) > 2:
            print("more than two people")
            if incrementer == 0:
                # first person
                poke_string += str(ctx.message.mentions[incrementer].name)
                pass
            elif incrementer != len(ctx.message.mentions) - 1:
                poke_string += ", " + str(ctx.message.mentions[incrementer].name)
            else:
                poke_string += " and " + str(ctx.message.mentions[incrementer].name)

        else:
            if incrementer == 0:
                # first person
                poke_string += str(ctx.message.mentions[incrementer].name)
                pass
            elif incrementer != len(ctx.message.mentions):
                poke_string += " and " + str(ctx.message.mentions[incrementer].name)

    if to_boop:
        return ctx.message.author.name + " pokes " + poke_string + "! Boop!"
    else:
        return ctx.message.author.name + " pokes " + poke_string + "!"
