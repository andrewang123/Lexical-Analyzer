#Andrew Ang
#Prof Arias
#Nov 5th 2017
#Lexical Analyzer, the purpose of this program is to create a lexical analyzer
# for the mini - power grammmar
import os #check if valid file
import sys #used to end program

#Checks if there is a file that can be opened, ends program if not
def checkValid():
    inputFile = input("prompt>  python lexer.py ")

    #check if the file is valid
    if not os.path.exists(inputFile):
        print("Input File is invalid")
        sys.exit()
    print(inputFile)
    return inputFile

def goThrough(inputFile):
    # open file using context manager dont need to close
    # closes by itself
    with open(inputFile, 'r') as file:
        print(file.read())
        fileContents = file.read()

#main
inputFile = checkValid()
goThrough(inputFile)

