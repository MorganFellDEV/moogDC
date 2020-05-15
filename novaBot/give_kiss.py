from os import listdir
from os.path import isfile, join
import random
import os

resources_location = os.getenv("NOVABOT_RESOURCES")

def random_kiss_image():
    onlyfiles = [f for f in listdir(resources_location + "/kiss/") if
                 isfile(join(resources_location + "/kiss/", f))]
    file = str((resources_location + "/kiss/" + random.choice(onlyfiles)))
    return file


def give_kiss(ctx):
    kiss_string = ""

    for incrementer, value in enumerate(ctx.message.mentions):
        print("length list " + str(len(ctx.message.mentions)))
        if len(ctx.message.mentions) > 2:
            print("more than two people")
            if incrementer == 0:
                # first person
                kiss_string += str(ctx.message.mentions[incrementer].name)
                pass
            elif incrementer != len(ctx.message.mentions) - 1:
                kiss_string += ", " + str(ctx.message.mentions[incrementer].name)
            else:
                kiss_string += " and " + str(ctx.message.mentions[incrementer].name)

        else:
            if incrementer == 0:
                # first person
                kiss_string += str(ctx.message.mentions[incrementer].name)
                pass
            elif incrementer != len(ctx.message.mentions):
                kiss_string += " and " + str(ctx.message.mentions[incrementer].name)

    return ctx.message.author.name + " kisses " + kiss_string + "!"
