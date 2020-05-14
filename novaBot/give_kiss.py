from os import listdir
from os.path import isfile, join
import random


def random_kiss_image():
    onlyfiles = [f for f in listdir("/var/www/html/resources/kiss/") if isfile(join("/var/www/html/resources/kiss/", f))]
    file = str(("/var/www/html/resources/kiss/" + random.choice(onlyfiles)))
    return file
