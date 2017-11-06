#Andrew Ang
#Prof Arias
#Nov 5th 2017
#Lexical Analyzer, the purpose of this program is to create a lexical analyzer
# for the mini - power grammmar
import os #check if valid file
import sys #used to end program

def getInput():


    inputFile = input("prompt>  python lexer.py ")

    #check if the file is valid
    if not os.path.exists(inputFile):
        print("Input File is invalid")
        sys.exit()

    print(inputFile)
    #open file using context manager
    with open(inputFile, 'r') as file: #read the contents of file
        print(file.read())
        fileContents = file.read()



#main
getInput()