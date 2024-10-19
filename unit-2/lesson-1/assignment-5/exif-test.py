from os import listdir, path
from PIL import Image, ExifTags
import random
import sys

if len(sys.argv) != 2:
    exit("This command requires one argument : the name of your image folder. Image folder and algorithm must be in same folder.")

try:

    files = listdir(sys.argv[1]) 
    files.remove(".DS_Store")

except:
    exit

# randomizing images to open

random_file = random.choice(files)
img = Image.open (path.join(str(sys.argv[1]),random_file))
exifData = img.getexif()


print(exifData)
for key in img.getexif().keys():
    print(key, ExifTags.TAGS[key])

# i found a module(?) called GPS in the pillow library andi tried using it but nothing happened :I
# >>> from PIL.ExifTags import GPS
# >>> GPS.GPSDestLatitude.value
