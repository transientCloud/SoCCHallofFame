#!/usr/bin/python
__author__ = 'shastri@umass.edu'

import argparse
from datetime import datetime
import os 
import sys
import operator
import re
import statistics

# { 'author' : list['year', 'num of papers'] }
authorDict = dict()

def addAuthor(titleLine, authorLine):
    global authorDict

    print (titleLine)

    authors=authorLine.split(',')
    for author in authors:
	author=author.strip()
	if author in authorDict:
	    authorDict[author] += 1
	else:
            authorDict[author] = 1

    return
# END addAuthor

def buildAuthorDict(confDir):

    for inputFile in os.listdir(confDir):
        confFile = confDir + inputFile
    	print ('Reading file: ', confFile)
        if os.path.isfile(confFile):
            with open(confFile) as inFp:
    		lines = []
    		for line in inFp:
        	    lines.append(line)
        	    if len(lines) >= 3:
			addAuthor(lines[0], lines[1])
			lines = []
		if len(lines) > 0:
        	    addAuthor(lines[0], lines[1])
    return
# END buildAuthorDict


def writeResult(filename):
    outputStringRes = ""
    global authorDict

    #for dictKey, dictVal in sorted(authorDict.items(), key=lambda x: (x[1], x[0]), reverse=True):
    for dictKey, dictVal in sorted(authorDict.items(), key=lambda(dictKey, dictVal):(-dictVal,dictKey)):
        outputStringRes += dictKey + "\t" + str(dictVal) + "\n" 
    
    with open(filename, 'w') as outFp:
        outFp.write(outputStringRes)

    return
# END writeResult


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("confDir", help="Path to conference directory")
    parser.add_argument("resultDir", help="Path to result directory")
    args = parser.parse_args()

    print ('\nBuilding author dictionary\n')
    buildAuthorDict(args.confDir)

    print ('\nPrinting results\n')
    writeResult(args.resultDir + "/soccHallOfFame.txt")

    print ('\nDone\n')

