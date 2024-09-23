from os import listdir, path
import random
from PIL import Image

files = listdir("images")
# files.remove(".DS_Store")

random_file = random.choice(files)

img = Image.open (path.join("images",random_file))