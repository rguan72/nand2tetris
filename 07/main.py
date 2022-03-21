import codewriter

with open("StackArithmetic/StackTest/StackTest.vm", "r") as ifstream, open("StackArithmetic/StackTest/StackTest.asm", "w") as ofstream:
    codewriter.codewrite(ifstream, ofstream)