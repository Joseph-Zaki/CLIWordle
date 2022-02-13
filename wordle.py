from colorama import init
from termcolor import colored, cprint
import random
import csv
init()
targetWord = ""
guesses = 6
won = False

def getWord():
    input_word = input("Enter a word: ")
    if len(input_word) != 5: 
        print("You word must be 5 letters")
        return getWord()
    elif not input_word.isalpha():
        print("Letters only! No Spaces!")
        return getWord()
    return input_word

def compareWord(guessWord, target):
    coloredString = ""
    count = 0
    global won
    if guessWord == target:
        won = True
        return colored(guessWord, "white", "on_green")
    for char in guessWord:
        if char in target:
            index = guessWord.find(char, count)
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
    global guesses
    print(str(guesses) + " guesses remaining.")
    currWord = getWord()
    guesses = guesses - 1
    print(compareWord(currWord, targetWord))

def selectWord():
    global targetWord
    with open("words.csv") as words:
        reader = csv.reader(words)
        chosen = random.choice(list(reader))
        targetWord = chosen[0]
        # reader = csv.reader(words)
        # print(random.choice(list(reader)))
        # choices = words.read()
        # targetWord = random.choice(choices)
    print("Your word is: " + targetWord)
        

def main():
    selectWord()
    print("Welcome to CLI Wordle!")
    while not won and guesses > 0:
        guess()
    if won:
        print("You won in " + str(6-guesses) + " guess(es)!")
        return
    else:
        print("You lost!")
        print("word was " + targetWord)


main()