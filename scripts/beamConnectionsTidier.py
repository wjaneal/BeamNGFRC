#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 13:55:48 2022

@author: wneal
"""

inputFile = "beamConnectionsInput.txt"
outputFile = "beamConnectionsOutput.txt"

inputFileData = open(inputFile,"r")
outputFileData = open(outputFile,"w")


connectionsList = []


def processLine(item):
    itemSections = []
    currentSection = ''
    characterType = "Text"
    for character in item:
        print("Start ", character)
        if ord(character) < 48 or ord(character)> 57:
            print(character, "Text")
            if characterType == "Numeric":
                itemSections.append(currentSection)
                currentSection = ""
                characterType = "Text"
            currentSection+=character
            
        else:
            print(character, "Numeric")
            characterType = "Numeric"
            if currentSection != '':
                print("Numeric; Current Section ",currentSection)
                itemSections.append(currentSection)
                currentSection = ''
            else:
                currentSection+=character
    integers = []
    for item in itemSections:
        if item.isnumeric():
            integers.append(item)
    print(itemSections)
    if len(integers) != 2:
        print(integers, "Error!")
    else:
        if integers[0] > integers[1]:
            integers[0], integers[1] = integers[1], integers[0]
    numberIndex = 0
    for i in range(len(itemSections)):
        if itemSections[i].isnumeric():
            itemSections[i] = numberIndex
            numberIndex += 1
    finalOutput = ""
    for item in itemSections:
        if isinstance(item,int):
            item = str(item)
        finalOutput+=item
    return finalOutput
        
    
def processLineII(item):
    l = item.split(",")
    number1text = l[0]
    number2text = l[1]
    number1 = 0
    number2 = 0
    try:
        number1 = int(number1text[5:len(number1text)-1])
        number2 = int(number2text[2:len(number2text)-2])
    except:
        print(number1, number2,  " .....Error")
    if number1==0 and number2 == 0:
        return("Error")
    if number1 > number2:
        return '\t["n'+str(number2)+'","n'+str(number1)+'"],'
    else:
        return '\t["n'+str(number1)+'","n'+str(number2)+'"],'
    
    return item
        

for line in inputFileData:
    processedLine = processLineII(line)
    if processedLine not in connectionsList and processedLine!="Error":
        print("Now adding...")
        print(processedLine)
        connectionsList.append(processedLine)

for item in connectionsList:
    outputFileData.write(item)
    outputFileData.write('\n')
    
outputFileData.close()
