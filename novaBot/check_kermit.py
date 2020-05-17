from os import listdir
from os.path import isfile, join
import random
import os
import discord


resources_location = os.getenv("NOVABOT_RESOURCES")


def random_kermit_image():
    onlyfiles = [f for f in listdir(str(resources_location) + "/kermit/") if
                 isfile(join(str(resources_location) + "/kermit/", f))]
    file = str((str(resources_location) + "/kermit/" + random.choice(onlyfiles)))
    return file
