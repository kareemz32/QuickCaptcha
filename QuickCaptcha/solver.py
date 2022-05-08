import os #runs commands on command line
import platform
import tensorflow as tf
import pyautogui as pg
import subprocess
import pyperclip
import time
from PIL import Image
from imageai.Detection import ObjectDetection
from keras.layers.normalization import batch_normalization
from tensorflow.python.framework.ops import disable_eager_execution

def is_retina_display():
    return subprocess.call("system_profiler SPDisplaysDataType | grep -i 'retina'", shell=True) == 0

def find_image(target):
    x, y = pg.locateCenterOnScreen(target, grayscale=True)
    if is_retina_display():
        x /= 2
        y /= 2
    return x, y

def clickSquare():
    try:
        #x, y = pg.locateCenterOnScreen("checkbox.png", grayscale = True)
        x, y = find_image("checkbox.png")
        pg.moveTo(x, y)
        if(platform.system() == "Darwin"):
            pg.click(clicks = 2)
        else:
            pg.click()
        return True
    except:
        return False

def getKey():
    if is_retina_display():
        pg.hotkey('command', 'a', interval=0.5)
        pg.hotkey('command', 'c')
    else:
        pg.hotkey('ctrl', 'a', interval=0.5)
        pg.hotkey('ctrl', 'c')
    #data = pyperclip.paste()#debug statement
    return string_processing(data=pyperclip.paste())

def string_processing(data):
    chars = []#debug statement
    chars[:0] = [data for i in range(len(chars))]#debug statement
    lines = data.split('Click verify once there are none left')
    lines = [i.strip() for i in lines]
    key = lines[0].split('\n')[1].strip('a ') #I'll make this line clearer
    return key

def get_plural_key(key):
	es = ["S","Z","X","H"]
	if(key[-1] in es):
		key = key +"ES"
	else:
		key = key + "S"
	return key

def check_special_case(key):
    if(key == "MOTORCYCLE" or key == "BICYCLE" or key == "BICYCLES"):
        key = "BIKE"
    if(key == "TRAFFICLIGHT" or key == "TRAFFICLIGHTS"):
        key = "STREETLIGHT"
    if(key == "VEHICLE" or key == "VEHICLES"):
        key = "CAR"
    return key

def retrain(key, plural, dataset):
    if(key not in dataset):
        if(key not in plural):
            os.system('python3 google_images_download.py --keywords \"' + key + '\" --limit 30  -o \"trainingdataset\"')
            os.system("bash train.sh");

def download_image():
	x, y = find_image("info.png")
	y -= 80
	pg.moveTo(x,y)
	pg.keyDown("ctrl")
	pg.click()
	pg.keyUp("ctrl")
	x, y = find_image("download.png")
	pg.moveTo(x, y)
	pg.click()

def move_image(src, dest):
    os.rename(src, dest)
	# os.system("mv ~/Downloads/payload.jpeg ~/Desktop/git_project/image.jpeg")

def split_image(filepath):
	#filepath = "image.jpeg"
	img = Image.open(filepath)
	if(img.size == (300,300)):
		os.system('split-image image.jpeg 3 3 -s')
		dim = 3
	else:
		dim = 4
		os.system('split-image image.jpeg 4 4 -s')
	return dim

clickSquare()
key = getKey().upper().replace(" ", "")
key = check_special_case(key)
download_image()
time.sleep(3)
os.system("mv ~/Downloads/payload.jpeg ~/Desktop/git_project/image.jpeg")
move_image(os.path.join("~/Downloads", f"payload.jpeg"), os.path.join("~/Desktop/git_project", f"image.jpeg"))
dim = split_image("image.jpeg")
print("dim = " + str(dim))
dataset = get_dataset()
plural_dataset = get_plural_dataset()
disable_eager_execution()
indexes = []
object_count = -1;
execution_path = os.getcwd()
execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
detector.loadModel()
for i in range(dim * dim):
	image = "image_" + str(i) + ".png"
	print(image)
	detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , image), output_image_path=os.path.join(execution_path , "imagenew.jpg"), minimum_percentage_probability=30)
	for eachObject in detections:
		object = eachObject["name"]
		object = object.upper().replace(" ", "");
		object = check_special_case(object);
		print(object)
		if(object == key or get_plural_key(object) == key):
			indexes.append(i)
			break
print(indexes)
def solve():
	pg.press("up");
	i = dim * dim - 1;
	while(len(indexes) > 0):
		index = indexes.pop(object_count)
		print("index == " + str(index))
		while(i > 0):
			if(i == index):
				pg.press("enter")
				pg.press("left")
				i-= 1
				break
			else:
				time.sleep(1)
				pg.press("left")
				i -= 1

#def click_next():
#	try:
#		x, y = find_image("next.png")
#		pg.moveTo(x,y)
#		pg.click()
#		return False
#solve()
#click_next()
#download_image()
#time.sleep(3)
#move_image()
#dim = split_image()
#indexes = []
#execution_path = os.getcwd()
#execution_path = os.getcwd()

#detector = ObjectDetection()
#detector.setModelTypeAsYOLOv3()
#detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
#detector.loadModel()
#for i in range(dim * dim):
#	image = "image_" + str(i) + ".png"
#	print(image)
#	detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , image), output_image_path=os.path.join(execution_path , "imagenew.jpg"), minimum_percentage_probability=30)
#	for eachObject in detections:
#		object = eachObject["name"]
#		object = object.upper().replace(" ", "");
#		object = check_specialCase(object);
#		print(object)
#		if(object == key):
#			indexes.append(i)
#			break
#		if(get_plural_key(object) == key):
#			indexes.append(i)
#			break
#print(indexes)
#solve()
