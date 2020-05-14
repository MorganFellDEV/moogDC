# load_mikus.py
from os import listdir
from os.path import isfile, join
import discord
import random


def random_miku_image():
    onlyfiles = [f for f in listdir("/var/www/html/resources/miku/") if isfile(join("/var/www/html/resources/miku/", f))]
    file = str(("/var/www/html/resources/miku/" + random.choice(onlyfiles)))
    return file


