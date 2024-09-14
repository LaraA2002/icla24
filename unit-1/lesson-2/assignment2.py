from unit1lesson2 import *



# Exercise 1

smallestnumber = number_list[0]
if number_list[1] < smallestnumber:
    smallestnumber = number_list[1]
for x in number_list:
    if x < smallestnumber:
        smallestnumber = x
print(smallestnumber)

# E1 Answer is 175



# Exercise 2

smallestnumberover500 = number_list[0]
if number_list[1] < smallestnumberover500:
    smallestnumberover500 = number_list[1]
for x in number_list:
    if 500 < x < smallestnumberover500:
        smallestnumberover500 = x
print(smallestnumberover500)

# E2 Answer is 501



# Exercise 3

smallestevennumber = number_list[0]
if number_list[1] < smallestevennumber:
    smallestevennumber = number_list[1]
for x in number_list:
    if x < smallestevennumber and x % 2 == 0:
        smallestevennumber = x
print(smallestevennumber)

# E3 Answer is 176



# Exercise 4

if "a" > "z":
    print("true")
else:
    print("false")

if "azure" > "apple" < "zebra":
    print("true")
else:
    print("false")

higherletter = word_list[0]
if word_list[1] > higherletter:
    higherletter = word_list[1]
for x in word_list:
    if x > higherletter:
        higherletter = x
print(higherletter)

# E4 Answer is 'violation'



# Exercise 5

longestword = word_list[0]
if word_list[1] > longestword:
    longestword = word_list[1]
for x in word_list:
    if len(x) > len(longestword):
        longestword = x
        print(longestword)
    if len(longestword) == len(x):
        print(x)

# E5 Answer is 'rehabilitation' and 'recommendation'

