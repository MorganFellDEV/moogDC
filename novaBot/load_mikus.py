# load_mikus.py
from os import listdir
from os.path import isfile, join
import random
import os

resources_location = os.getenv("NOVABOT_RESOURCES")

def random_miku_image():
    onlyfiles = [f for f in listdir(str(resources_location) + "/miku/") if isfile(join(str(resources_location) + "/miku/", f))]
    file = str((resources_location + "/miku/" + random.choice(onlyfiles)))
    return file


