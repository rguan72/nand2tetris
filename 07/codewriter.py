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
    ofstream.writelines(arithmeticAssembly[command.arg1])

def writePushPop(command: parser.Command, ofstream: typing.TextIO) -> None:
    assemblyCode = pushPopAssembly[f"{command.commandType} {command.arg1}"](command.arg2)
    ofstream.writelines(assemblyCode)

arithmeticAssembly = {
    "add": [
            "// add\n",
            "@SP\n",
            "M=M-1\n",
            "A=M\n",
            "D=M\n",
            "@SP\n",
            "A=M-1\n",
            "M=M+D\n",      
        ],
}

pushPopAssembly = {
    "CommandType.C_PUSH constant": lambda arg2: [
        f"// push constant {arg2}\n",
        f"@{arg2}\n",
        "D=A\n"
        "@SP\n",
        "A=M\n",
        f"M=D\n",
        "@SP\n",
        "M=M+1\n",
    ],
}
