import random

####################################################################
#
#   Made in Python using Visual Studio Code
#   Reccomended to also run this in VS Code
#   By: Matty Slyzys
#
#   For COSC 4P01 A1 Q2
#
#   This program makes use of seeded random values to generate random values. Since random values are deterministic, 
#   we seed the random using the exact date and time (something that connot be easilly replicated to give the 
#   appearance of truly random values. This program layers on seeded random values to add an extra layer to the
#   randomness
#
#   CFG:
#   test_case -> event*
#   event -> randint(i,j)
#   i -> 0|1|...|100000
#   j -> 0|1|...|100000
#   event -> event
#   event -> event^range
#   range -> randint(i,k)
#   k-> 0|1|...|1000 
#
####################################################################

# random integer list generation that creates a randomly sized list with random values
def randomInt():
    random.seed()
    randList = []
    for i in range(random.randint(1,1000)):
        randList.append(random.randint(1,100000))
    return randList

# The method to sort the array. It uses bubblesort
def sortInt(unsortedInts):
    length = len(unsortedInts)
    sortedInts = unsortedInts
    for i in range(0, length-1):
        for j in range(0, length-i-1):
            if unsortedInts[j] > sortedInts[j+1]:
                temp = sortedInts[j]
                sortedInts[j] = sortedInts[j+1]
                sortedInts[j+1] = temp
    return sortedInts

# test the program and print its results at each stage
number = randomInt()
print(number)
sortedNumber = sortInt(number)
print(sortedNumber)

