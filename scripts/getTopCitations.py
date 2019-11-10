#!/usr/bin/python
__author__ = 'shastri@utexas.edu'

import argparse
from datetime import datetime
import os 
import sys
import operator
import re
import statistics

# { 'author' : list['citation', 'list of authors'] }
citationDict = dict()

def buildCitationsDict():
    global citationDict

    confFile = "socc.citations"
    print ('Reading file: ', confFile)
    if os.path.isfile(confFile):
        with open(confFile) as inFp:
            lines = []
            for line in inFp:
                lines.append(line)
                if len(lines) >= 4:
                    citationDict[lines[0]] = lines[1]
                    lines = []
            if len(lines) > 0:
                citationDict[lines[0]] = lines[1]
    return
# END buildCitationsDict


def writeResult():
    global citationDict

    print ("Num of papers: " + str(len(citationDict)) + "\n")

    for dictKey, dictVal in sorted(citationDict.items(), key=lambda x: int(x[1]), reverse=True):
        print (dictKey + str(dictVal)) 
    
    return
# END writeResult


if __name__ == '__main__':
    print ('\nBuilding citation dictionary\n')
    buildCitationsDict()
    writeResult()
