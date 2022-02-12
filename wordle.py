from colorama import init
from termcolor import colored, cprint
init()
targetWord = "point"
targetarr = list(targetWord)
guesses = 6

def getWord():
    input_word = input("Enter a word: ")
    if len(input_word) != 5: 
        print("You word must be 5 letters")
        return getWord()
    elif not input_word.isalpha():
        print("Letters only! No Spaces!")
        return getWord()
    return input_word

"""
TODO:
1. compareWord should check if the correct word was guest
2. incorporate game structure in the form of a "main" function?
"""
def compareWord(guessWord, target):
    coloredString = ""
    count = 0
    for char in guessWord:
        if char in target:
            index = guessWord.find(char, count)
            #print("count: " + str(count) + " targetIndex: " + str(target.find(char, count))+ "index: " + str(index))
            if index == target.find(char, count):
                coloredString = coloredString + colored(char, "white", "on_green")
                count+=1
                continue
            coloredString = coloredString + colored(char, "white", "on_yellow")
        else:
            coloredString = coloredString + colored(char, "white", "on_grey")
        count+=1
    return coloredString
            
def guess():
    print(str(guesses) + " guesses remaining.")
    currWord = getWord()
    print(compareWord(currWord, targetWord))


guess()
