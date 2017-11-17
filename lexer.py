#Andrew Ang
#Prof Arias
#Nov 5th 2017
#Lexical Analyzer, the purpose of this program is to create a
#lexical analyzer for the mini - power grammar

import os
import sys
import re

#Checks if there is a file that can be opened, ends program if not
#Parameters: N/A
#Returns: the name of the inputfile
def checkValid():
    inputFile = input("prompt>  python lexer.py ")

    #check if the file is valid
    if not os.path.exists(inputFile):
        print("Input File is invalid")
        sys.exit()
    print("Processing input file " + inputFile)
    return inputFile

#Go through entire file
#Parameters: inputFile refers to the string of the input file
#Returns: N/A
def goThroughLine(inputFile):
    # open file using context manager dont need to close
    # closes by itself
    totalNumTokens = 0
    outputFileName = inputFile[:-4] + ".out"
    with open(inputFile, 'r') as file:
        outFile = open(outputFileName,'w')
        for line in file:
            #print(file.read())
            #fileContents = file.readline()
            totalNumTokens += createTokens(line, outFile)
        print(str(totalNumTokens) + " tokens produced")
        print("Result in file " + outputFileName)
        outFile.close()

#Passes each line of the file and processes it
#Parameters: lineProcess which is the line being processed
#Returns: total tokens for that specific line
def createTokens(lineProcess, outputFile):
    lenOfString = len(lineProcess)
    potentialToken = "" #string to construct the token
    tokens = [] #create a list of tokens
    isString = False; #check for strings ex) "The result is"
    seenQuotation = 0
    totalTokens = 0
    for x in range(0, lenOfString): #check char by char
        #print(lineProcess[x])
        if(lineProcess[x] != " "):
            if(lineProcess[x] == "\""): #check for '"'
                isString = True
                seenQuotation += 1
                if (seenQuotation == 2):
                    isString = False
                    seenQuotation = 0
            else:
                potentialToken += lineProcess[x]
            #account for last character in line
            if (x == lenOfString - 1):
                tokens.append(potentialToken)
                totalTokens += 1
                # change potentialToken to empty
                potentialToken = ""
        else: # There is a space
            if (not(isString)): #not a string
                 # add it to the list
                tokens.append(potentialToken)
                totalTokens += 1
                # change potentialToken to empty
                potentialToken = ""
            else: #it is a string
                potentialToken += lineProcess[x] #add a space
    print(tokens)
    checkSyntax(tokens, outputFile)
    return totalTokens

#Check if the tokens that are produced are part of the Rules
#Parameters: tokens the list of tokens, name of the file
#Returns: N/A
def checkSyntax(tokens, outputFile):
    #Check for errors
    lenOfToken = len(tokens)
    for token in tokens:
    #for x in range(0, lenOfToken):
        #print(token)
        if (token == "="):
            outputFile.write("ASSIGN\n")
        elif (token == ";\n" or token == ";"):
            outputFile.write("SEMICOLON\n")
        elif (re.search('^[a-z](([a-z]*)|([0-9]*))[$|#|%]$', token)): #RegEx for ID
            outputFile.write("ID    ")
            outputFile.write(token[:-1] + "   ") #everything except for the last
            if(token.endswith("$")):
                outputFile.write("STRING\n")
            elif(token.endswith("#")):
                outputFile.write("INTEGER\n")
            elif(token.endswith("%")):
                outputFile.write("REAL\n")
        elif (re.search('^[-|+]?[0-9]+$',token)): # int-const
            outputFile.write("INT_CONST   ")
            outputFile.write(token + "\n")
        elif (re.search('^[-|+]?[0-9]+\.[0-9]*$',token)): # real-const
            outputFile.write("REAL_CONST  ")
            outputFile.write(token + "\n")
        elif (token == '+' ):
            outputFile.write("PLUS\n")
        elif (token == '-'):
            outputFile.write("MINUS\n")
        elif (token == '*'):
            outputFile.write("TIMES\n")
        elif (token == '/'):
            outputFile.write("DIVIDE\n")
        elif (token == "PRINT"):
            outputFile.write("PRINT\n")
            # re.search('^[a-z] ([ *]([a-z]*))*',token)
            #" " in token and
            #([\s*][\d*]([a-z]*))*
            #re.search('^([a-z]|\s|\d)([\s*]|[\d*]|([a-z]*))*',token)
            #" " in token and (not (re.findall('([A-Z])',token)))
        elif (re.search('([a-z]|\d]|\s)+',token) and (not (re.findall('([A-Z])',token)))):
            #no capital letters for the string
            outputFile.write("STRING:   ")
            outputFile.write(token + "\n")
        elif (token == '('):
            outputFile.write("LEFT_PAREN  ")
        elif (token == ')'):
            outputFile.write("RIGHT_PAREN  ")
        elif (token == '^'):
            outputFile.write("EXPONENT  ")
        else:
            print("Error, File does not match grammar.")
            print("\"" + token + "\""+ " is not in the grammar.")
            sys.exit()
        # make sure that the ending token is no semi colon

        #if there are any string left in the list produce an error
#main
inputFile = checkValid()
goThroughLine(inputFile)

'''
TO DO LIST:
2. output into output file
3. make so works in terminal
'''
