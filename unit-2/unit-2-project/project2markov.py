import markovify

# TITLE

# open and read text file with scraped titles

text = open("corpus/scrapedtitles.txt").read()

# markovify, state size 2 seems to be the sweet spot between sensical, funny, and interesting
 
generator = markovify.Text(text, state_size=2) 

# open title variable

titlelevel = ""

# for loop that makes 1 sentence of upto 100 characters for the title

for i in range(1):
    titlelevel += str(generator.make_short_sentence(100))
    titlelevel += " "

# make into title case

titlecase = titlelevel.title()

# print title

print("\n\n\n")
print(titlecase)
print("\n")

# HEADER

# open and read text file with scraped headers

text = open("corpus/scrapedheaders.txt").read()

# markovify, state size 2

generator = markovify.Text(text, state_size=2) 

# open header variable

headerlevel = ""

# for loop that makes 1 sentence of upto 150 characters for the header

for i in range(1):
    headerlevel += str(generator.make_short_sentence(150))
    headerlevel += " "

# print header

print(headerlevel)

# BODY

# open and read text file with scraped body paras

text = open("corpus/scrapedbody.txt").read()

# markovify, state size 2

generator = markovify.Text(text, state_size=2) 

# open body variable

bodylevel = ""

# for loop that makes 15 sentences of upto 150 characters for the body

for i in range(15):
    bodylevel += str(generator.make_short_sentence(150))
    bodylevel += " "

# print body

print("\n")
print(bodylevel)
print("\n\n\n")

