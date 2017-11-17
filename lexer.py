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
    inputFile = ""
    if (len(sys.argv) > 1):
        inputFile = sys.argv[1]
    #check if the file is valid
    if not os.path.exists(inputFile):
        print("Input File is invalid")
        sys.exit()
    print("Processing input file " + inputFile)
    return inputFile

#Gets the total number of lines in the file
#Parameters: inputFile, the name of the inputfile (string)
#Returns: integer representing total number of lines
def getTotalNumOfLines(inputFile):
    numberOfLines = 0
    with open(inputFile, 'r') as file:
        for line in file:
            numberOfLines += 1
    return numberOfLines

#Go through entire file
#Parameters: inputFile refers to the string of the input file
#Returns: N/A
def goThroughLine(inputFile):
    # open file using context manager dont need to close
    # closes by itself
    totalNumTokens = 0
    totalNumOfLines = getTotalNumOfLines(inputFile)
    outputFileName = inputFile[:-4] + ".out"
    currentLine = 1
    with open(inputFile, 'r') as file:
        outFile = open(outputFileName,'w')
        for line in file:
            totalNumTokens += createTokens(line, outFile, totalNumOfLines, currentLine)
            currentLine += 1
        print(str(totalNumTokens) + " tokens produced")
        print("Result in file " + outputFileName)
        outFile.close()

#Passes each line of the file and processes it
#Parameters: lineProcess which is the line being processed(string)
#outputFile is the name of the output file
#totalNumOfLines is thetotal number of lines in the file
#currentLine is current line being processed in file
#Returns: total tokens for that specific line
def createTokens(lineProcess, outputFile, totalNumOfLines, currentLine):
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
    #print(tokens)
    checkSyntax(tokens, outputFile, totalNumOfLines, currentLine)
    return totalTokens

#Check if the tokens that are produced are part of the Rules
#Parameters: tokens the list of tokens, name of output file,
#totalNumOfLines is thetotal number of lines in the file
#currentLine is current line being processed in file
#Returns: N/A
def checkSyntax(token, outputFile, totalNumOfLines, currentLine):
    #Check for errors
    lenOfToken = len(token)
    #for token in tokens:
    for x in range(0, lenOfToken):
        #print(token)
        if (token[x] == "="):
            outputFile.write("ASSIGN\n")
        elif (currentLine == totalNumOfLines and token[x] == ";"): #last line of file cannot have ";"
            print("Error, File does not match grammar.")
            print("Last line cannot end with ';'")
            sys.exit()
        elif (token[x] == ";\n" or token[x] == ";"):
            outputFile.write("SEMICOLON\n")
        elif (re.search('^[a-z](([a-z]*)|([0-9]*))[$|#|%]$', token[x])): #RegEx for ID
            outputFile.write("ID    ")
            outputFile.write(token[x][:-1] + "   ") #everything except for the last
            if(token[x].endswith("$")):
                outputFile.write("STRING\n")
            elif(token[x].endswith("#")):
                outputFile.write("INTEGER\n")
            elif(token[x].endswith("%")):
                outputFile.write("REAL\n")
        elif (re.search('^[-|+]?[0-9]+$',token[x])): # int-const
            outputFile.write("INT_CONST   ")
            outputFile.write(token[x] + "\n")
        elif (re.search('^[-|+]?[0-9]+\.[0-9]*$',token[x])): # real-const
            outputFile.write("REAL_CONST  ")
            outputFile.write(token[x] + "\n")
        elif (token[x] == '+' ):
            outputFile.write("PLUS\n")
        elif (token[x] == '-'):
            outputFile.write("MINUS\n")
        elif (token[x] == '*'):
            outputFile.write("TIMES\n")
        elif (token[x] == '/'):
            outputFile.write("DIVIDE\n")
        elif (token[x] == "PRINT"):
            outputFile.write("PRINT\n")
        elif (re.search('([a-z]|\d]|\s)+',token[x]) and (not (re.findall('([A-Z])',token[x])))):
            #no capital letters for the string
            outputFile.write("STRING:   ")
            outputFile.write(token[x] + "\n")
        elif (token[x] == '('):
            outputFile.write("LEFT_PAREN  ")
        elif (token[x] == ')'):
            outputFile.write("RIGHT_PAREN  ")
        elif (token[x] == '^'):
            outputFile.write("EXPONENT  ")
        else:
            print("Error, File does not match grammar.")
            print("\"" + token[x] + "\""+ " is not in the grammar.")
            sys.exit()

#main
inputFile = checkValid()
goThroughLine(inputFile)

