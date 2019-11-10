#!/usr/bin/python
__author__ = 'shastri@utexas.edu'

import argparse
from datetime import datetime
import os 
import sys
import operator
import re
import statistics
import scholarly

citationDict = dict()

def getCitation(titleLine, authorLine):
    global citationDict

    search_query = scholarly.search_pubs_query(titleLine)
    citeCount = next(search_query).citedby
    print(titleLine + str(citeCount) + "\n"+ authorLine)

    return
# END getCitation

def buildCitationsDict(confDir):

    for inputFile in os.listdir(confDir):
        confFile = confDir + inputFile
        print ('Reading file: ', confFile)
        if os.path.isfile(confFile):
            with open(confFile) as inFp:
                lines = []
                for line in inFp:
                    lines.append(line)
                    if len(lines) >= 3:
                        getCitation(lines[0], lines[1])
                        lines = []
                if len(lines) > 0:
                    getCitation(lines[0], lines[1])
    return
# END buildCitationsDict


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("confDir", help="Path to conference directory")
    args = parser.parse_args()

    print ('\nBuilding citation dictionary\n')
    buildCitationsDict(args.confDir)

    print ('\nDone\n')
