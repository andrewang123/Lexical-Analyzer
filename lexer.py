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
            ouputTokens(line)

#Passes each line of the file and processes it
def ouputTokens(lineProcess):
    print(lineProcess)
    #should work for any string starting with letter
    #followed by any combination of number and letter

#read char by char!!!!
    matchID = re.search('[a-z](([a-z]*)|([0-9]*))[$|#|%]', lineProcess)
    #matchType = re.search('[$|#|%]', lineProcess)
    name = "Andrew"
    print(name[0])
    #match
    if matchID:
        print("ID    ", end="")
        #print(re.search('[a-z]', lineProcess))
        print(matchID.group())
        #lastChar =
        '''
        if (matchType == "$"):
            print("STRING")
        elif (matchType == "#"):
            print("INTEGER")
        elif (matchType == "#"):
            print("REAL")
        '''

    #if re.search():

    '''
    if a - z then ID
    '''

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
