# unit 1 project : algorithm 2

import os
from os import listdir, path
import random
from PIL import Image
import sys    
import PIL.ImageOps

# argument error message, called if command line programme call is not as desired

if len(sys.argv) != 2:
    exit("This command requires one argument : the name of your image folder. Image folder and algorithm must be in same folder.")

# to avoid ds store file errors where it chooses the ds_store file instead of an image file

def remove_ds_store(path): # define function with the image folder name as the parameter
      for files in os.walk(path): # for files in that folder
            for file in files: # checking if a file
                if file == ".DS_Store": # is a ds_store file
                   file_path = os.path.join(file) # if so, select file
                   os.remove(file_path) # remove it
                else:
                   exit # if not, exit
                   
remove_ds_store(sys.argv[1]) # call function with the desired folder

# doubling down on deleting ds_store :)
# try-except error handling because i got an error that said there was no ds_store file to delete
# so if there isn't one, it skips this part

try:

    files = listdir(sys.argv[1])
    files.remove(".DS_Store")

except:
    exit

# opening 3 random files in desired folder

random_file = random.choice(files)
ogimg1 = Image.open (path.join(str(sys.argv[1]),random_file))

random_file = random.choice(files)
ogimg2 = Image.open (path.join(str(sys.argv[1]),random_file))

random_file = random.choice(files)
img3 = Image.open (path.join(str(sys.argv[1]),random_file))

# 'try-except' error handling to give personalized ValueError error message
# so if the images aren't blendable due to diffe3ring sizes, it skips to the error message

try:

    # using blend as a test to see if images match in size (not part of edit) (not saved)
    # because blend needs matching sizes in images

    sizetest1 = Image.blend(ogimg1,ogimg2,.5)     
    sizetest2 = Image.blend(ogimg1,img3,.5)   
    sizetest3 = Image.blend(ogimg2,img3,.5)  

    # cropping images 1 & 2

    image_path = sys.argv[1] # initializing image path as the desired folder

    width, height = ogimg1.size # initializing image width and height
    crop = (0, 0, width, int(height/3)) # crop location and size in image
    cropimg1 = ogimg1.crop(crop) # crop
    cropimg1.save(f"{image_path}/cropimg1.jpeg") # save to desired folder

    width, height = ogimg2.size 
    crop = (0, int(height/3), width, int(height/3 + height/3))
    cropimg2 = ogimg2.crop(crop)

    # inverting cropped image 2

    invertimg = PIL.ImageOps.invert(cropimg2) # use python tools to invert
    invertimg.save(f"{image_path}/cropimg2.jpeg")

    # pasting on image 3 and saving

    width, height = img3.size
    img1 = Image.open (f"{image_path}/cropimg1.jpeg")
    img2 = Image.open (f"{image_path}/cropimg2.jpeg")
    img3.paste(img1, (0,0)) # paste image 1
    img3.paste(img2, (0, int(height/3))) #paste image 2
    img3.save(f"{image_path}/algo2-" + str(sys.argv[1]) + ".jpeg")

    # deleting cropped images

    def delete_image(image_path): # define function with the location and name of the image as the parameter
        if os.path.exists(image_path): # if the image exists in that folder
            os.getcwd() # select
            os.remove(image_path) # and remove

    delete1 = sys.argv[1] + "/cropimg1.jpeg" # initialize image path as the folder name and cropped image name
    delete2 = sys.argv[1] + "/cropimg2.jpeg"
    delete_image(delete1) # delete
    delete_image(delete2)

except:
    exit("Images must be of the same size.")
       


 