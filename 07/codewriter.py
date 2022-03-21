from turtle import write
import typing

import parser

def codewrite(ifstream: typing.TextIO, ofstream: typing.TextIO) -> None:
    lines = ifstream.readlines()
    commands = parser.parse(lines)
    for command in commands:
        writeCommand(command, ofstream)

def writeCommand(command: parser.Command, ofstream: typing.TextIO) -> None:
    if command.commandType == parser.CommandType.C_ARITHMETIC:
        writeArithmetic(command, ofstream)
    else:
        writePushPop(command, ofstream)

def writeArithmetic(command: parser.Command, ofstream: typing.TextIO) -> None:
    if command.arg1 == "add":
        ofstream.writelines([
            "// add\n",
            "@SP\n",
            "M=M-1\n",
            "A=M\n",
            "D=M\n",
            "@SP\n",
            "A=M-1\n",
            "M=M+D\n",      
        ])

def writePushPop(command: parser.Command, ofstream: typing.TextIO) -> None:
    if command.commandType == parser.CommandType.C_PUSH:
        if command.arg1 == "constant":
            ofstream.writelines([
                f"// push constant {command.arg2}\n",
                f"@{command.arg2}\n",
                "D=A\n"
                "@SP\n",
                "A=M\n",
                f"M=D\n",
                "@SP\n",
                "M=M+1\n",
            ])
