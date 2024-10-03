# unit 1 project : algorithm 1

import os
from os import listdir, path
import random
from PIL import Image
import sys

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

# opening 2 random files in desired folder

random_file = random.choice(files)
img1 = Image.open (path.join(str(sys.argv[1]),random_file))

random_file = random.choice(files)
img2 = Image.open (path.join(str(sys.argv[1]),random_file))

# 'try-except' error handling to give personalized ValueError error message
# so if the images aren't blendable due to diffe3ring sizes, it skips to the error message

try:
    
    #  blend images as a first step

    img = Image.blend(img1,img2,.5)     

    # save output to same folder that the images were taken from

    image_path = sys.argv[1]
    img.save(f"{image_path}/tobedeleted.jpeg")    

    # alter pixels under certain value to fun colour and save

    img_hsv = img.convert(mode="HSV") # convert to HSV
    img_hsv_data = img_hsv.getdata() # get image data
    new_img_data = [] # set up new image variable

    for p in img_hsv_data: # for pixel in the original HSV image
        if p[2] < 50: # if the y-value(?) of the pixe is under 50
            new_img_data.append((200, 255, 255)) # make the pixel magenta
        else: # otherwise
            new_img_data.append(p) # add the original pixel

    img_hsv.putdata(new_img_data) # add data to new image
    img_rgb = img_hsv.convert("RGB") # convert to RGB
    img_rgb.save(f"{image_path}/algo1-" + str(sys.argv[1]) + ".jpeg") # save

    # delete the blended base image

    def delete_image(image_path): # define function with the location and name of the image as the parameter
        if os.path.exists(image_path): # if the image exists in that folder
            os.getcwd() # select
            os.remove(image_path) # and remove

    image_path = sys.argv[1] + "/tobedeleted.jpeg" # initialize image path as the folder name and base image name
    delete_image(image_path) # call function

except:
    exit("Images must be of the same size.")
