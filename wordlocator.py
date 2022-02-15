import csv
"""
DANGER:
This file can crash your system. Believe me.
Writes from test.csv to words.csv to copy the list of possible wordle words.
"""
def main():
    with open("test.csv", "r") as f, open("words.csv", "a", newline="") as wordslist:
        reader = csv.reader(f) #returns 2D Array
        writer = csv.writer(wordslist)
        wordsOnly = []
        for row in reader:
            wordsOnly.append([row[2]]) # appends list containing a word as one string
        for word in wordsOnly:
            writer.writerow(word) # writes each "row" which is one word to the file
main()