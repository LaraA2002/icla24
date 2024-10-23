import requests
from bs4 import BeautifulSoup
import sys
import markovify
import syllables

# error handling
if len(sys.argv) != 2:
    exit("This command requires one argument : the url of the site you wish to scrape from. I recommend https://www.wikihow.com/Apologize-to-a-Cat !")

# SCRAPING

# to automate the code and make it flexible without having to change it individually everytime i run it on a diff site i'll use sys.argv here
# i can then put the large repository i want to scrape in the command line
site = requests.get(sys.argv[1])

# printing the site url
print("\n")
print("site name : " + sys.argv[1])
print("\n")

# scraping site and extracting text
html = BeautifulSoup(site.text, "html.parser")

# assigning text to variable
text = html.get_text()

# open for writing(?) and add text to .txt file, then close
data = open('scrape.txt', 'w')
data.write(text)
data.close()

# DATA PROCESSING

# create dictionary
d = {}

# assigning text to a variable
with open("scrape.txt", "r") as filex:
   file = filex.read()
    
# adding words and their counts to the dictionary
for wordx in file.split():
         if wordx.isalpha():
            word = wordx.lower() # this line is bc upper and lowercase words were being counted separately
            if word in d:
                d[word] += 1
            else: 
                d[word] = 1

# getting a word/key that has a count/value of 1
def appearsonce(d, value): # function asking for dict & value as parameters
    for key, val in d.items():
      if key.isalpha(): # only words, because I was getting numbers and other characters
        if val == value:
            return key
    return None
key = appearsonce(d, 1) 

# printing one of the least frequent words on the scraped site
print("1 of the least frequent words on the site : " + str(key))
print("\n")

# MARKOVIFYING

# open and read created text
txt = open("scrape.txt").read()

# markovify
markov = markovify.Text(txt)

paragraph = ""

for i in range(10):
    paragraph += str(markov.make_short_sentence(80))
    paragraph += " "

print("\n\n\n")
print(paragraph)
print("\n\n\n")