from os import listdir
from os.path import isfile, join
import random
import os

resources_location = os.getenv("NOVABOT_RESOURCES")

def random_pat_image():
    onlyfiles = [f for f in listdir(str(resources_location) + "/pat/") if
                 isfile(join(str(resources_location) + "/pat/", f))]
    file = str((str(resources_location) + "/pat/" + random.choice(onlyfiles)))
    return file


def give_pat(ctx):
    pat_string = ""

    for incrementer, value in enumerate(ctx.message.mentions):
        print("length list " + str(len(ctx.message.mentions)))
        if len(ctx.message.mentions) > 2:
            print("more than two people")
            if incrementer == 0:
                # first person
                pat_string += str(ctx.message.mentions[incrementer].name)
                pass
            elif incrementer != len(ctx.message.mentions) - 1:
                pat_string += ", " + str(ctx.message.mentions[incrementer].name)
            else:
                pat_string += " and " + str(ctx.message.mentions[incrementer].name)

        else:
            if incrementer == 0:
                # first person
                pat_string += str(ctx.message.mentions[incrementer].name)
                pass
            elif incrementer != len(ctx.message.mentions):
                pat_string += " and " + str(ctx.message.mentions[incrementer].name)

    return ctx.message.author.name + " pats " + pat_string + "!"
