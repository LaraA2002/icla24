import sys

print(sys.argv)

print(len(sys.argv))





import sys

data = [ 643, 452, 230, 219, 962, 532 ]

# check if the user did not enter an argument
if len(sys.argv) < 2:
    print("You forgot to type an argument")
    exit()

index = int(sys.argv[1])

# check if the user entered an argument that is too large
if index >= len(data):
    print("You typed a number thats too large")
    exit()

print( data[index] )