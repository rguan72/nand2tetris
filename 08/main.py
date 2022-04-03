import sys
import os
import codewriter

inputFile = sys.argv[1]
inputFileName, _ = os.path.splitext(inputFile)
if len(sys.argv) > 2:
    outputFile = sys.argv[2]
else:
    if os.path.isfile(inputFile):
        outputFile = inputFileName + ".asm"
    else:
        outputFile = os.path.join(inputFileName, os.path.basename(inputFileName) + ".asm")
with open(outputFile, "w") as ofstream:
    myCodewriter = codewriter.CodeWriter(ofstream, inputFile)
    myCodewriter.codewrite()
