# Lara : Assignment 4 



# image making : version 1

import sys
from PIL import Image 
import random

if len(sys.argv) != 2:
    exit("This program requires one argument: the name of the image file that will be created.")

img = Image.new("RGB", (500,500) )

for y in range(500):

    for x in range(500):

        r = random.randint(1, 100)
        g = random.randint(100, 200)
        b = random.randint(200, 255)

        if x % 200 == 1:
           r = 0

        if x % 50 > 25:
           r = 255

        if y % 50 > 25:
           b = 255

        if x % 100 > 50 and y % 100 > 50:
           g = 255

        if y % 2 == 0:
           b = 0

        pixel = (r, g, b)
        img.putpixel( (x,y), pixel )

img.save(sys.argv[1])



# image making : version 2

import sys
from PIL import Image 

if len(sys.argv) != 2:
    exit("This program requires one argument: the name of the image file that will be created.")

img = Image.new("RGB", (500,500) )

for y in range(500):

    for x in range(500):

        r = 99
        b = 55
        if x % 22 == 0:
            b = 255
            
        if y % 200 == 0:
            r = 200

        if y % 3 == 0:
            r = 100
            b = 0

        pixel = (r, 0, b)
        img.putpixel( (x,y), pixel )

img.save(sys.argv[1])



# collaging : version 1

import sys
from PIL import Image 

if len(sys.argv) != 5:
    exit("This program requires 4 arguments: the name of 4 image files to combine.")

img1 = Image.open( sys.argv[1] )
img2 = Image.open( sys.argv[2] )
img3 = Image.open( sys.argv[3] )
img4 = Image.open( sys.argv[4] )

img1.thumbnail( (200, 200) )
img2.thumbnail( (200, 200) ) 
img3.thumbnail( (200, 200) )
img4.thumbnail( (200, 200) )

new_image = Image.new( "RGBA", (200, 200), "black" )

new_image.paste(img1, (0,0) )

img2.putalpha(120)
img3.putalpha(90)
img4.putalpha(100)

new_image.alpha_composite(img2, (0,0) )
new_image.alpha_composite(img3, (0,0) )
new_image.alpha_composite(img4, (0,0) )

new_image.save("collaging1.png")



# collaging : version 1

import sys
from PIL import Image 

if len(sys.argv) != 5:
    exit("This program requires 4 arguments: the name of 4 image files to combine.")

img1 = Image.open( sys.argv[1] )
img2 = Image.open( sys.argv[2] )
img3 = Image.open( sys.argv[3] )
img4 = Image.open( sys.argv[4] )

img1.thumbnail( (200, 200) )
img2.thumbnail( (200, 200) ) 
img3.thumbnail( (200, 200) )
img4.thumbnail( (200, 200) )

new_image = Image.new( "RGBA", (800, 400), "black" )

new_image.paste(img1, (0,0) )
new_image.paste(img2, (200,0) )
new_image.paste(img3, (400,0) )
new_image.paste(img4, (600,0) )

img1.putalpha(128)
img2.putalpha(128)
img3.putalpha(128)
img4.putalpha(128)

new_image.alpha_composite(img4, (0,200) )
new_image.alpha_composite(img3, (200,200) )
new_image.alpha_composite(img2, (400,200) )
new_image.alpha_composite(img1, (600,200) )

new_image.save("collaging2.png")