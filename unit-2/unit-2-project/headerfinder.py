import requests
from bs4 import BeautifulSoup
import sys

# request desired website url as customized in command line with sys

webrequest = requests.get(sys.argv[1])

# use beautifulsoup to parse website html

webhtml = BeautifulSoup(webrequest.text, "html.parser")

# get html

webtext = webhtml.get_text()

# open a variable to append to

headertext = []

# function to get headers

def headerget(soupdata): # define function and parameter
    headers = soupdata.select(sys.argv[2]) # customize tags to look for in command line using sys
    for h in headers: # for loop that appends headers to opened variable
            headertext.append(h.get_text())

# call function with parsed html as parameter

headerget(webhtml)

# make appended text a string instead of a list

tabheaders = " ".join(headertext)
print(tabheaders)

# open the relevant text file and append the data and close

with open("corpus/scrapedheaders.txt", "a") as file:
    file.write(tabheaders)
    file.close()

