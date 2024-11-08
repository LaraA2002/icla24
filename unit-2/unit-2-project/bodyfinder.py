import requests
from bs4 import BeautifulSoup
import sys

# request desired website url as customized in command line with sys

websiterequest = requests.get(sys.argv[1])

# use beautifulsoup to parse website html

websitehtml = BeautifulSoup(websiterequest.text, "html.parser")

# get html

websitetext = websitehtml.get_text()

# open a variable to append to

bodytext = []

# function to get body paras

def bodyget(soupdata): # define function and parameter
    body = soupdata.select(sys.argv[2]) # customize tags to look for in command line using sys
    for b in body: # for loop that appends body to opened variable
            bodytext.append(b.get_text())

# call function with parsed html as parameter

bodyget(websitehtml)

# make appended text a string instead of a list

tabbody = " ".join(bodytext)
print(tabbody)

# open the relevant text file and append the data and close

with open("corpus/scrapedbody.txt", "a") as file:
    file.write(tabbody)
    file.close()

