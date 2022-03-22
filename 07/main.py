import sys
import os
import codewriter

inputFile = sys.argv[1]
inputFileName, _ = os.path.splitext(inputFile)
outputFile = inputFileName + ".asm"
with open(inputFile, "r") as ifstream, open(outputFile, "w") as ofstream:
    codewriter.codewrite(ifstream, ofstream, os.path.basename(inputFileName))