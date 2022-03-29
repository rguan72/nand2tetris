import sys
import os
import codewriter

inputFile = sys.argv[1]
inputFileName, _ = os.path.splitext(inputFile)
if len(sys.argv) > 2:
    outputFile = sys.argv[2]
else:
    outputFile = inputFileName + ".asm"
with open(inputFile, "r") as ifstream, open(outputFile, "w") as ofstream:
    myCodewriter = codewriter.CodeWriter(ifstream, ofstream, os.path.basename(inputFileName))
    myCodewriter.codewrite()
