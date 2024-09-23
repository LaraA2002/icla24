# unit 1 project : part 1

from os import listdir, path
import random
from PIL import Image
import sys

files = listdir("u1project-images")
files.remove(".DS_Store")

random_file = random.choice(files)
img1 = Image.open (path.join("u1project-images",random_file))

random_file = random.choice(files)
img2 = Image.open (path.join("u1project-images",random_file))

img1 = Image.open(sys.argv[1])
img2 = Image.open(sys.argv[2])
blended_img = Image.blend(img1,img2,.5)
blended_img.save("blended.jpg " + sys.argv[1] + " " + sys.argv[2])

if len(sys.argv) != 3:
    exit("This command requires two arguments (file names).")


# unit 1 project : part 2

