from os import listdir
from os.path import isfile, join
import random


def random_poke_image():
    onlyfiles = [f for f in listdir("/var/www/html/resources/poke/") if isfile(join("/var/www/html/resources/poke/", f))]
    file = str(("/var/www/html/resources/poke/" + random.choice(onlyfiles)))
    return file


