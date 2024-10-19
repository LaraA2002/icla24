d = {}

# assigning text to a variable

with open("codetxt.txt", "r") as filex:
   file = filex.read()
    
# adding words and their counts to the dictionary

for wordx in file.split():
         word = wordx.lower() # this line is bc upper and lowercase words were being counted separately
         if word in d:
              d[word] += 1
         else: 
              d[word] = 1

# removing generic words

remove = ("the", "and", "a", "of", "to", "in", "by", "was", "for", "from", "it", "with", "but", "because", "she", "he", "her", "him", "them", "they", "be", "are", "this", "that", "at", "which", "or", "his", "hers", "as", "is", "were", "their", "there", "an", "on", "into", "not", "had", "so", "have", "called", "project", "gutenberg")
for x in remove:
    if x in d:
        del d[x]

# sorting the dictionary by value by dict->list->dict conversion

listmaking = sorted(d.items(), key=lambda x:x[1], reverse=True)
nd = dict(listmaking)

print(nd)

# Top 10 most frequent words : 'the': 2512, 'of': 1895, 'and': 1159, 'a': 837, 'to': 723, 'was': 607, 'in': 496, 'see': 372, 'he': 301, 'by': 295
# Top 10 most frequent interesting words : 'see': 372, 'who': 195, 'name': 181, 'one': 162, 'god': 116, 'son': 106, 'goddess': 96, 'all': 89, 'when': 80, 'king': 80
# I found out how to remove words from a dict in python and how to do list-dict conversions

# Unit 2 Project ideating : 
# 1(gathering news articles on male killers to analyze the language used to describe them and frame the narrative, bc ive seen so many headlines that undermine that violence by adding weird/irrelevant/deflecting details) 
# 2(analyzing other texts/articles where there is a difference in the narrativization between the actions of men/women, maybe in political news articles) 
# 3(similarly analyzing the way male/female children are described/encouraged to behave/complimented maybe using literature or articles) 
# 4(similarly how people intract with male/female content creators/celebrities maybe anlayzing comment sections)