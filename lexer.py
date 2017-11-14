#Andrew Ang
#Prof Arias
#Nov 5th 2017
#Lexical Analyzer, the purpose of this program is to create a lexical analyzer
#for the mini - power grammar

import os
import sys
import re

#Checks if there is a file that can be opened, ends program if not
def checkValid():
    inputFile = input("prompt>  python lexer.py ")

    #check if the file is valid
    if not os.path.exists(inputFile):
        print("Input File is invalid")
        sys.exit()
    print(inputFile)
    return inputFile

#Go through line by line in the file
#inputFile refers to the string of the input file
def goThrough(inputFile):
    # open file using context manager dont need to close
    # closes by itself
    with open(inputFile, 'r') as file:
        for line in file:
            #print(file.read())
            #fileContents = file.readline()
            outputTokens(line)

#Passes each line of the file and processes it
def outputTokens(lineProcess):
    lenOfString = len(lineProcess)
    print(lenOfString)

    print(lineProcess)

    potentialToken = ""
    tokens = [] #create a list of tokens
    tokenIndex = 0
    for x in range(0, lenOfString-1): #check char by char
    #for char in lineProcess:
        print(lineProcess[x])
        if(lineProcess[x] != " "):
            potentialToken += lineProcess[x]
            # check if there is a capital
            if (x == lenOfString - 2):
                tokens.append(potentialToken)
                tokenIndex += 1
                # change potentialToken to empty
                potentialToken = ""
        else:
            #check if it is a valid string
            # add it to the list
            tokens.append(potentialToken)
            tokenIndex += 1
            # change potentialToken to empty
            potentialToken = ""

    #print(lineProcess[lenOfString-2])
    print(tokens)

    #Check for errors
    for token in tokens:
        #print(token)
        if (token == "="):
            print("ASSIGN")
        elif (token == ";"):
            print("SEMICOLON")
        elif (re.search('[a-z](([a-z]*)|([0-9]*))[$|#|%]', token)): #first character is lowercase letter
            print("ID    ", end="")
            print(token[:-1], "    ", end="") #everything except for the last
            if(token.endswith("$")):
                print("STRING")
            elif(token.endswith("#")):
                print("INTEGER")
            elif(token.endswith("%")):
                print("REAL")
        elif (re.search('([-|+]?)[0-9]([0-9]*)',token)): # num const
                print("jelo")
                #((-|+)?)[0-9]([0-9]*).([0-9]*)
        elif (re.search('[0-9]+',token)): # int-const
                print("Smello")


        #if there are any string left in the list produce an error

    #should work for any string starting with letter
    #followed by any combination of number and letter

#read char by char!!!!
    #matchID = re.search('[a-z](([a-z]*)|([0-9]*))[$|#|%]', lineProcess)
    #matchType = re.search('[$|#|%]', lineProcess)

    #match
    #if matchID:
    #    print("ID    ", end="")
        #print(re.search('[a-z]', lineProcess))
    #    print(matchID.group())
        #lastChar =


    sys.exit()

#main
inputFile = checkValid()
goThrough(inputFile)

'''
TO DO LIST:
1. make sure there is no Capitals
2. output into output file
3. make so works in terminal
'''
