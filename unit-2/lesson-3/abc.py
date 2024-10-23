import markovify
# # look at documentation for markofivy here: https://github.com/jsvine/markovify

text = open("123.txt").read()

generator = markovify.Text(text, state_size=3) 

paragraph = ""

for i in range(10):
    paragraph += str(generator.make_short_sentence(80))
    paragraph += " "

print("\n\n\n")
print(paragraph)
print("\n\n\n")

# # ---

# import random
# import sys

# filename = sys.argv[1]
# text = open(filename).read().lower().split()
# markovDictionary = {}	



# # use this function to get indexes for words
# def getIndexForWord(wordFromLoop, nextPossibleWordsAmount): 
#     possibleWordIndexes = []
#     allWords = []
#     for index, word in enumerate(text):
#         if word == wordFromLoop:
#             possibleWordIndexes.append(index)
#     # print(wordFromLoop, "indexes:", possibleWordIndexes)
#     return possibleWordIndexes[nextPossibleWordsAmount]





# # build dictionary
# totalWords = len(text)
# for word in text:
#     if not word in markovDictionary:
#         markovDictionary[word] = []

#     if text.index(word) == (totalWords - 1): break

#     nextPossibleWordsAmount = len(markovDictionary[word]) 
#     textIndex = getIndexForWord(word, nextPossibleWordsAmount)

#     if word == text[(totalWords - 1)]:
#         continue
#     else:
#         nextWord = text[textIndex + 1]
#         markovDictionary[word].append(nextWord)

# # pprint.pprint(markovDictionary)




# # generate text from dictionary
# chosenWord = random.choice(text)
# generatedText = []
# for i in range(80):
#     if chosenWord == text[(totalWords - 1)]:
#         chosenWord = text[0]
#     else:
#         generatedText.append(chosenWord)
#         nextWord = random.choice(markovDictionary[chosenWord])
#         chosenWord = nextWord

# finalPrintOut = " ".join(generatedText)

# print("\n\n\n")
# print(finalPrintOut)
# print("\n\n\n")

# # ---

# import pprint

# file = open("4-text-small.txt").read().lower()

# markovDictionary = {}

# words = file.replace("\n"," ").split()

# for (i, word) in enumerate(words):
    
#     if i == len(words) - 1:
#         break

#     next_word = words[i+1]
    
#     if word in markovDictionary:
#         markovDictionary[word].append(next_word)
#     else:
#         markovDictionary[word] = [next_word]

# # # print(markovDictionary)
# # # use pretty print library to see dictionary more clearly
# pprint.pp(markovDictionary)

# # ---

import requests
from bs4 import BeautifulSoup

crgslist_response = requests.get("https://wiki.bloodontheclocktower.com/Trouble_Brewing")

crgslist_soup_html = BeautifulSoup(crgslist_response.text, "html.parser")

crgslist_text = crgslist_soup_html.get_text()

freeStuff = []

def getTitles(soupdata):
    titles = soupdata.select(".title")
    # if titles:
    #     for t in titles:
    freeStuff.append(soupdata.get_text())

getTitles(crgslist_soup_html)

freeText = " ".join(freeStuff)

crgslist_data = open('crgslist_free.txt', 'w')
crgslist_data.write(freeText)
crgslist_data.close()