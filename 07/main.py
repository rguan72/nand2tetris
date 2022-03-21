import codewriter

with open("StackArithmetic/SimpleAdd/SimpleAdd.vm", "r") as ifstream, open("StackArithmetic/SimpleAdd/SimpleAdd.asm", "w") as ofstream:
    codewriter.codewrite(ifstream, ofstream)