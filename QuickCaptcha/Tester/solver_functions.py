import os
import subprocess
from PIL import Image


def string_processing(data):
    chars = []
    chars[:0] = data
    lines = data.split('Click verify once there are none left')
    lines = [i.strip() for i in lines]
    key = lines[0].split('\n')[1].strip('a ')  # I'll make this line clearer
    return key


def check_special_case(key):
    if(key == "MOTORCYCLE" or key == "MOTORCYCLES" or key == "BICYCLE" or key == "BICYCLES"):
        key = "BIKE"
    if(key == "TRAFFICLIGHT" or key == "TRAFFICLIGHTS"):
        key = "STREETLIGHT"
    if(key == "VEHICLE" or key == "VEHICLES"):
        key = "CAR"
    return key


def get_plural_key(key):
    es = ["S", "Z", "X", "H"]
    if(key[-1] in es):
        key = key + "ES"
    else:
        key = key + "S"
    return key


def is_mac():
    return subprocess.call("system_profiler SPDisplaysDataType | grep -i 'retina'", shell=True) == 0


def move_image():
    os.system("mv ~/Downloads/payload.jpeg ~/Desktop/git_project/image.jpeg")


def split_image():
    filepath = "image.jpeg"
    img = Image.open(filepath)
    if(img.size == (300, 300)):
        os.system('split-image image.jpeg 3 3 -s')
        dim = 3
    else:
        dim = 4
        os.system('split-image image.jpeg 4 4 -s')
    return dim
