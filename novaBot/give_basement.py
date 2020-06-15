from os import listdir
from os.path import isfile, join
import random
import os

resources_location = os.getenv("NOVABOT_RESOURCES")



def send_to_basement(ctx):
    basement_string = ""

    for incrementer, value in enumerate(ctx.message.mentions):
        print("length list " + str(len(ctx.message.mentions)))
        if len(ctx.message.mentions) > 2:

            print("more than two people")
            if incrementer == 0:
                # first person
                basement_string += str(ctx.message.mentions[incrementer].name)
                pass
            elif incrementer != len(ctx.message.mentions) - 1:
                basement_string += ", " + str(ctx.message.mentions[incrementer].name)
            else:
                basement_string += " and " + str(ctx.message.mentions[incrementer].name)

        else:
            if incrementer == 0:
                # first person
                basement_string += str(ctx.message.mentions[incrementer].name)
                pass
            elif incrementer != len(ctx.message.mentions):
                basement_string += " and " + str(ctx.message.mentions[incrementer].name)

    if len(ctx.message.mentions) == 0:
        return ctx.message.author.name + " goes to the basement!"
    else:
        return ctx.message.author.name + " sends " + basement_string + " to the basement!"


def random_basement_image(singledive):
    if singledive:
        onlyfiles = [f for f in listdir(str(resources_location) + "/basement/single/") if
                     isfile(join(str(resources_location) + "/basement/single/", f))]
        file = str((str(resources_location) + "/basement/single/" + random.choice(onlyfiles)))
    else:
        onlyfiles = [f for f in listdir(str(resources_location) + "/basement/multiple/") if
                     isfile(join(str(resources_location) + "/basement/multiple/", f))]
        file = str((str(resources_location) + "/basement/multiple/" + random.choice(onlyfiles)))
    return file
