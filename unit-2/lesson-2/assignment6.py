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

# make poem variable
poem = ""

# make poem, similar to paragraph we did except I changed the full stops to commas, shortened the sentences a bit, and moved the lines under each other
for i in range(3):
    poem += "\n"
    poem += str(markov.make_short_sentence(50))
    poem = poem.replace(".", ",")
    poem += "\n"
    poem += str(markov.make_short_sentence(50))

# print poem
print("fun markov poem based on the site : " + str(poem))
print("\n")



# I tried to make a haiku instead of a regular poem first, it didn't work but here's the code I wrote while attempting that :)
# If you know why it didn't work please let me know!
# haiku = open("haiku.txt", "w")
# for x in str(markov):
#     print(x)
#     if x.isalpha():
#         syllcount = syllables.estimate(x)
#         haiku = open("haiku.txt").read()
#         linesyllcount = syllables.estimate(haiku)
#         print(linesyllcount)
#         if syllcount <= 5:
#             while linesyllcount <= 5:
#                 haiku = open("haiku.txt", "w")
#                 haiku.write(x)



# Unit 2 Project ideating : 
# Based on my initial ideas (copied again below), i think a question could be something like:
# Q : What kind of language do the media use to describe/narrativize male and female politicians/criminals/celebrities? (obviously will be refined based on which avenue i choose)
# 1(gathering news articles on male killers to analyze the language used to describe them and frame the narrative, bc ive seen so many headlines that undermine that violence by adding weird/irrelevant/deflecting details) 
# 2(analyzing other texts/articles where there is a difference in the narrativization between the actions of men/women, maybe in political news articles) 
# 3(similarly analyzing the way male/female children are described/encouraged to behave/complimented maybe using literature or articles) 
# 4(similarly how people intract with male/female content creators/celebrities maybe anlayzing comment sections)
