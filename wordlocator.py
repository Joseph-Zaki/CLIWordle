import csv

def main():
    with open("test.csv") as f, open("words.csv", "a") as wordslist:
        reader = csv.reader(f)
        writer = csv.writer(wordslist)
        wordslist.write("TestTest1")

main()