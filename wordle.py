from colorama import Fore, Back, Style, init
from termcolor import colored, cprint
init()
targetWord = "point"
targetarr = list(targetWord)
guesses = 6

def getWord():
    input_word = input("Enter a word: ")
    if len(input_word) != 5: 
        print("You word must be 5 letters")
        getWord()
    if not input_word.isalpha():
        print("Letters only! No Spaces!")
        getWord()
    return input_word

def compareWord(guessWord, target):
    coloredString = ""
    for char in guessWord:
        if char in target:
            index = guessWord.find(char)
            if index == target.find(char):
                coloredString = coloredString + colored(char, "white", "on_green")
                continue
            coloredString = coloredString + colored(char, "white", "on_yellow")
        else:
            coloredString = coloredString + colored(char, "white", "on_grey")
    return coloredString
            


def guess():
    print(str(guesses) + " guesses remaining.")
    currWord = getWord()
    print(compareWord(currWord, targetWord))


print(compareWord("nrenn", "point"))
