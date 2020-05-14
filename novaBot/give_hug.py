from os import listdir
from os.path import isfile, join
import random


def random_hug_image():
    onlyfiles = [f for f in listdir("/var/www/html/resources/hug/") if isfile(join("/var/www/html/resources/hug/", f))]
    file = str(("/var/www/html/resources/hug/" + random.choice(onlyfiles)))
    return file
