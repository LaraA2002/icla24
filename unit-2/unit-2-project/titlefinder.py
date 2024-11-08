import requests
from bs4 import BeautifulSoup
import sys

# request desired website url as customized in command line with sys

siterequest = requests.get(sys.argv[1])

# use beautifulsoup to parse website html

sitehtml = BeautifulSoup(siterequest.text, "html.parser")

# get html

sitetext = sitehtml.get_text()

# open a variable to append to

titletext = []

# function to get titles

def titleget(soupdata): # define function and parameter
    titles = soupdata.select(sys.argv[2]) # customize tags to look for in command line using sys
    for t in titles: # for loop that appends titles to opened variable
            titletext.append(t.get_text())

# call function with parsed html as parameter

titleget(sitehtml)

# make appended text a string instead of a list

tabtitles = " ".join(titletext)
print(tabtitles)

# open the relevant text file and append the data and close

with open("corpus/scrapedtitles.txt", "a") as file:
    file.write(tabtitles)
    file.close()

    