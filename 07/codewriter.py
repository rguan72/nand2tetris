from turtle import write
import typing

import parser

def codewrite(ifstream: typing.TextIO, ofstream: typing.TextIO) -> None:
    lines = ifstream.readlines()
    commands = parser.parse(lines)
    for i, command in enumerate(commands):
        writeCommand(command, ofstream, i)

def writeCommand(command: parser.Command, ofstream: typing.TextIO, index: int) -> None:
    if command.commandType == parser.CommandType.C_ARITHMETIC:
        writeArithmetic(command, ofstream, index)
    else:
        writePushPop(command, ofstream)

def writeArithmetic(command: parser.Command, ofstream: typing.TextIO, index: int) -> None:
    ofstream.writelines(arithmeticAssembly[command.arg1](index))

def writePushPop(command: parser.Command, ofstream: typing.TextIO) -> None:
    assemblyCode = pushPopAssembly[f"{command.commandType} {command.arg1}"](command.arg2)
    ofstream.writelines(assemblyCode)

arithmeticAssembly = {
    "add": lambda _: [
        "// add\n",
        "    @SP\n",
        "    M=M-1\n",
        "    A=M\n",
        "    D=M\n",
        "    @SP\n",
        "    A=M-1\n",
        "    M=M+D\n",      
    ],
    "sub": lambda _: [
        "// sub\n",
        "    @SP\n",
        "    M=M-1\n",
        "    A=M\n",
        "    D=M\n",
        "    @SP\n",
        "    A=M-1\n",
        "    M=M-D\n",
    ],
    "neg": lambda _: [
        "// neg\n",
        "    @SP\n",
        "    A=M-1\n",
        "    D=M\n",
        "    M=-D\n",
    ],
    "not": lambda _: [
        "// not\n",
        "    @SP\n",
        "    A=M-1\n",
        "    D=M\n",
        "    M=!D\n",
    ],
    "and": lambda _: [
        "// and\n",
        "    @SP\n",
        "    M=M-1\n",
        "    A=M\n",
        "    D=M\n",
        "    @SP\n",
        "    A=M-1\n",
        "    M=M&D\n",      
    ],
    "or": lambda _: [
        "// or\n",
        "    @SP\n",
        "    M=M-1\n",
        "    A=M\n",
        "    D=M\n",
        "    @SP\n",
        "    A=M-1\n",
        "    M=M|D\n",      
    ],
    "eq": lambda index: [
        "// eq\n",
        "    @SP\n",
        "    M=M-1\n",
        "    A=M\n",
        "    D=M\n",
        "    @SP\n",
        "    A=M-1\n",
        "    D=M-D\n",
        "    M=-1\n",
        f"    @EQUAL{index}\n",
        "    D;JEQ\n",
        "    @SP\n",
        "    A=M-1\n",
        "    M=0\n",
        f"(EQUAL{index})\n",
    ],
    "gt": lambda index: [
        "// gt\n",
        "    @SP\n",
        "    M=M-1\n",
        "    A=M\n",
        "    D=M\n",
        "    @SP\n",
        "    A=M-1\n",
        "    D=M-D\n",
        "    M=-1\n",
        f"    @GT{index}\n",
        "    D;JGT\n",
        "    @SP\n",
        "    A=M-1\n",
        "    M=0\n",
        f"(GT{index})\n",
    ],
    "lt": lambda index: [
        "// lt\n",
        "    @SP\n",
        "    M=M-1\n",
        "    A=M\n",
        "    D=M\n",
        "    @SP\n",
        "    A=M-1\n",
        "    D=M-D\n",
        "    M=-1\n",
        f"    @LT{index}\n",
        "    D;JLT\n",
        "    @SP\n",
        "    A=M-1\n",
        "    M=0\n",
        f"(LT{index})\n",
    ],
}

pushPopAssembly = {
    "CommandType.C_PUSH constant": lambda arg2: [
        f"// push constant {arg2}\n",
        f"    @{arg2}\n",
        "    D=A\n"
        "    @SP\n",
        "    A=M\n",
        f"    M=D\n",
        "    @SP\n",
        "    M=M+1\n",
    ],
}
