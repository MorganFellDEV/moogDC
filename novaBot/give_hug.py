from os import listdir
from os.path import isfile, join
import random


def random_hug_image():
    onlyfiles = [f for f in listdir("/var/www/html/resources/hug/") if isfile(join("/var/www/html/resources/hug/", f))]
    file = str(("/var/www/html/resources/hug/" + random.choice(onlyfiles)))
    return file

def give_hug(ctx):
    hug_string = ""

    for incrementer, value in enumerate(ctx.message.mentions):
        print("length list " + str(len(ctx.message.mentions)))
        if len(ctx.message.mentions) > 2:
            print("more than two people")
            if incrementer == 0:
                # first person
                hug_string += str(ctx.message.mentions[incrementer].name)
                pass
            elif incrementer != len(ctx.message.mentions) - 1:
                hug_string += ", " + str(ctx.message.mentions[incrementer].name)
            else:
                hug_string += " and " + str(ctx.message.mentions[incrementer].name)

        else:
            if incrementer == 0:
                # first person
                hug_string += str(ctx.message.mentions[incrementer].name)
                pass
            elif incrementer != len(ctx.message.mentions):
                hug_string += " and " + str(ctx.message.mentions[incrementer].name)

    return ctx.message.author.name + " hugs " + hug_string + "!"