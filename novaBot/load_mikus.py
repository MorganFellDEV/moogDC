# load_mikus.py
from os import listdir
from os.path import isfile, join


def load_miku_images():
    onlyfiles = [f for f in listdir("/var/www/html/resources/miku/") if isfile(join("/var/www/html/resources/miku/", f))]
    return onlyfiles
