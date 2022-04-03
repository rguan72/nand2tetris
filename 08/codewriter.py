import os
import pathlib
import typing

import parser

class CodeWriter:
    def codewrite(self) -> None:
        self.writeBootstrap()
        if os.path.isfile(self.inputName):
            with open(self.inputName, "r") as ifstream:
                self.codewriteFile(ifstream)
        else:
            for filename in os.listdir(self.inputName):
                if pathlib.Path(filename).suffix == ".vm":
                    filenameName, _ = os.path.splitext(filename)
                    self.filename = filenameName
                    with open(os.path.join(self.inputName, filename), "r") as ifstream:
                        self.codewriteFile(ifstream)

    def codewriteFile(self, ifstream) -> None:
        lines = ifstream.readlines()
        commands = parser.parse(lines)
        outsideFunctionName = ""
        for i, command in enumerate(commands):
            if command.commandType == parser.CommandType.C_FUNCTION:
                outsideFunctionName = command.arg1
            self.writeCommand(command, i, outsideFunctionName)

    def writeCommand(self, command: parser.Command, index: int, outsideFunctionName: str) -> None:
        if command.commandType == parser.CommandType.C_ARITHMETIC:
            self.writeArithmetic(command, index)
        elif command.commandType in [parser.CommandType.C_PUSH, parser.CommandType.C_POP]:
            self.writePushPop(command)
        elif command.commandType == parser.CommandType.C_LABEL:
            self.writeLabel(command, outsideFunctionName)
        elif command.commandType == parser.CommandType.C_IF:
            self.writeIf(command, outsideFunctionName)
        elif command.commandType == parser.CommandType.C_GOTO:
            self.writeGoto(command, outsideFunctionName)
        elif command.commandType == parser.CommandType.C_FUNCTION:
            self.writeFunction(command)
        elif command.commandType == parser.CommandType.C_RETURN:
            self.writeReturn()
        elif command.commandType == parser.CommandType.C_CALL:
            self.writeCall(command, index)

    def writeArithmetic(self, command: parser.Command, index: int) -> None:
        self.ofstream.writelines(self.arithmeticAssembly[command.arg1](index))

    def writePushPop(self, command: parser.Command) -> None:
        assemblyCode = self.pushPopAssembly[f"{command.commandType} {command.arg1}"](command.arg2)
        self.ofstream.writelines(assemblyCode)

    def writeLabel(self, command: parser.Command, outsideFunctionName: str) -> None:
        assembyCode = [ 
            f"({self.makeLabel(command.arg1, outsideFunctionName)})\n",
        ]
        self.ofstream.writelines(assembyCode)

    def writeIf(self, command: parser.Command, outsideFunctionName: str) -> None:
        self.ofstream.writelines(self.ifAssembly(command.arg1, outsideFunctionName))

    def writeGoto(self, command: parser.Command, outsideFunctionName: str) -> None:
        assemblyCode = [
            f"// goto {command.arg1}\n",
            f"    @{self.makeLabel(command.arg1, outsideFunctionName)}\n",
            "    0;JMP\n",
        ]
        self.ofstream.writelines(assemblyCode)

    def writeFunction(self, command: parser.Command) -> None:
        assemblyCode = self.functionAssembly(command.arg1, command.arg2)
        self.ofstream.writelines(assemblyCode)

    def writeReturn(self) -> None:
        self.ofstream.writelines(self.returnAssembly)

    def writeCall(self, command: parser.Command, index: int) -> None:
        assemblyCode = self.callAssembly(command.arg1, command.arg2, index)
        self.ofstream.writelines(assemblyCode)

    def writeBootstrap(self) -> None:
        bootstrapAssembly = [
            "// bootstrap\n"
            "    @261\n",
            "    D=A\n",
            "    @SP\n",
            "    M=D\n",
            "    @Sys.init\n",
            "    0;JMP\n",
        ]
        self.ofstream.writelines(bootstrapAssembly)

    def makeLabel(self, labelName: str, outsideFunctionName: str) -> str:
        return f"{self.filename}.{outsideFunctionName}${labelName}"

    def __init__(self, ofstream: typing.TextIO, inputName: str) -> None:
        self.ofstream = ofstream
        self.inputName = inputName

        self.arithmeticAssembly = {
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

        self.pushPopAssembly = {
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
            "CommandType.C_PUSH local": lambda arg2: [
                f"// push local {arg2}\n",
                "    @LCL\n",
                "    D=M\n",
                f"    @{arg2}\n",
                "    A=D+A\n",
                "    D=M\n",
                "    @SP\n",
                "    A=M\n",
                "    M=D\n",
                "    @SP\n",
                "    M=M+1\n",
            ],
            "CommandType.C_PUSH argument": lambda arg2: [
                f"// push argument {arg2}\n",
                "    @ARG\n",
                "    D=M\n",
                f"    @{arg2}\n",
                "    A=D+A\n",
                "    D=M\n",
                "    @SP\n",
                "    A=M\n",
                "    M=D\n",
                "    @SP\n",
                "    M=M+1\n",
            ],
            "CommandType.C_PUSH this": lambda arg2: [
                f"// push this {arg2}\n",
                "    @THIS\n",
                "    D=M\n",
                f"    @{arg2}\n",
                "    A=D+A\n",
                "    D=M\n",
                "    @SP\n",
                "    A=M\n",
                "    M=D\n",
                "    @SP\n",
                "    M=M+1\n",
            ],
            "CommandType.C_PUSH that": lambda arg2: [
                f"// push that {arg2}\n",
                "    @THAT\n",
                "    D=M\n",
                f"    @{arg2}\n",
                "    A=D+A\n",
                "    D=M\n",
                "    @SP\n",
                "    A=M\n",
                "    M=D\n",
                "    @SP\n",
                "    M=M+1\n",
            ],
            "CommandType.C_PUSH temp": lambda arg2: [
                f"// push temp {arg2}\n",
                "    @5\n",
                "    D=A\n",
                f"    @{arg2}\n",
                "    A=D+A\n",
                "    D=M\n",
                "    @SP\n",
                "    A=M\n",
                "    M=D\n",
                "    @SP\n",
                "    M=M+1\n",
            ],
            "CommandType.C_POP local": lambda arg2: [
                f"// pop local {arg2}\n",
                f"    @{arg2}\n",
                "    D=A\n",
                "    @LCL\n",
                "    D=M+D\n",
                "    @R13\n",
                "    M=D\n",
                "    @SP\n",
                "    M=M-1\n",
                "    A=M\n",
                "    D=M\n",
                "    @R13\n",
                "    A=M\n",
                "    M=D\n",
            ],
            "CommandType.C_POP argument": lambda arg2: [
                f"// pop argument {arg2}\n",
                f"    @{arg2}\n",
                "    D=A\n",
                "    @ARG\n",
                "    D=M+D\n",
                "    @R13\n",
                "    M=D\n",
                "    @SP\n",
                "    M=M-1\n",
                "    A=M\n",
                "    D=M\n",
                "    @R13\n",
                "    A=M\n",
                "    M=D\n",
            ],
            "CommandType.C_POP this": lambda arg2: [
                f"// pop this {arg2}\n",
                f"    @{arg2}\n",
                "    D=A\n",
                "    @THIS\n",
                "    D=M+D\n",
                "    @R13\n",
                "    M=D\n",
                "    @SP\n",
                "    M=M-1\n",
                "    A=M\n",
                "    D=M\n",
                "    @R13\n",
                "    A=M\n",
                "    M=D\n",
            ],
            "CommandType.C_POP that": lambda arg2: [
                f"// pop that {arg2}\n",
                f"    @{arg2}\n",
                "    D=A\n",
                "    @THAT\n",
                "    D=M+D\n",
                "    @R13\n",
                "    M=D\n",
                "    @SP\n",
                "    M=M-1\n",
                "    A=M\n",
                "    D=M\n",
                "    @R13\n",
                "    A=M\n",
                "    M=D\n",
            ],
            "CommandType.C_POP temp": lambda arg2: [
                f"// pop temp {arg2}\n",
                f"    @{arg2}\n",
                "    D=A\n",
                "    @5\n",
                "    D=A+D\n",
                "    @R13\n",
                "    M=D\n",
                "    @SP\n",
                "    M=M-1\n",
                "    A=M\n",
                "    D=M\n",
                "    @R13\n",
                "    A=M\n",
                "    M=D\n",
            ],
            "CommandType.C_PUSH pointer": lambda arg2: [
                f"// push pointer {arg2}\n",
                "    @THIS\n",
                "    D=A\n",
                f"    @{arg2}\n",
                "    A=D+A\n",
                "    D=M\n",
                "    @SP\n",
                "    A=M\n",
                "    M=D\n",
                "    @SP\n",
                "    M=M+1\n",
            ],
            "CommandType.C_POP pointer": lambda arg2: [
                f"// pop pointer {arg2}\n",
                "    @THIS\n",
                "    D=A\n",
                f"    @{arg2}\n",
                "    D=D+A\n",
                "    @R13\n",
                "    M=D\n",
                "    @SP\n",
                "    M=M-1\n",
                "    A=M\n",
                "    D=M\n",
                "    @R13\n",
                "    A=M\n",
                "    M=D\n",
            ],
            "CommandType.C_PUSH static": lambda arg2: [
                f"// push static {arg2}\n",
                f"    @{self.inputFileName}.{arg2}\n",
                "    D=M\n",
                "    @SP\n",
                "    A=M\n",
                "    M=D\n",
                "    @SP\n",
                "    M=M+1\n",
            ],
            "CommandType.C_POP static": lambda arg2: [
                f"// pop static {arg2}\n",
                "    @SP\n",
                "    M=M-1\n",
                "    A=M\n",
                "    D=M\n",
                f"    @{self.inputFileName}.{arg2}\n",
                "     M=D\n",
            ],
        }

        self.ifAssembly = lambda arg1, outsideFunctionName: [
            f"// if-goto {arg1}\n",
            "    @SP\n",
            "    M=M-1\n",
            "    A=M\n",
            "    D=M\n",
            f"    @{self.makeLabel(arg1, outsideFunctionName)}\n",
            "    D;JNE\n",
        ]

        self.functionAssembly = lambda arg1, arg2: [
            f"// function {arg1} {arg2}\n",
            f"({arg1})\n",
            f"    @{arg2}\n",
            "    D=A\n",
            f"({arg1}$internalLabel$loop)\n",
            f"    @{arg1}$internalLabel$end\n",
            "    D;JEQ\n",
            "    @SP\n",
            "    A=M\n",
            "    M=0\n",
            "    @SP\n",
            "    M=M+1\n",
            "    D=D-1\n"
            f"    @{arg1}$internalLabel$loop\n",
            "    0;JMP\n",
            f"({arg1}$internalLabel$end)\n",
        ]

        self.returnAssembly = [
            "// return\n",
            "    @LCL\n",
            "    D=M\n",
            "    @R13\n",
            "    M=D\n",
            "    @SP\n",
            "    A=M-1\n",
            "    D=M\n",
            "    @ARG\n",
            "    A=M\n",
            "    M=D\n",
            "    @ARG\n",
            "    D=M+1\n",
            "    @SP\n",
            "    M=D\n",
            "    @LCL\n",
            "    A=M-1\n",
            "    D=M\n",
            "    @THAT\n",
            "    M=D\n",
            "    @LCL\n",
            "    D=M\n",
            "    @2\n",
            "    D=D-A\n",
            "    A=D\n",
            "    D=M\n",
            "    @THIS\n",
            "    M=D\n",
            "    @LCL\n",
            "    D=M\n",
            "    @3\n",
            "    D=D-A\n",
            "    A=D\n",
            "    D=M\n",
            "    @ARG\n",
            "    M=D\n",
            "    @LCL\n",
            "    D=M\n",
            "    @4\n",
            "    D=D-A\n",
            "    A=D\n",
            "    D=M\n",
            "    @LCL\n",
            "    M=D\n",
            "    @R13\n",
            "    D=M\n",
            "    @5\n",
            "    D=D-A\n",
            "    A=D\n",
            "    A=M\n",
            "    0;JMP\n",
        ]

        self.callAssembly = lambda arg1, arg2, index: [
            f"// call {arg1} {arg2}\n",
            f"    @{arg1}$ret.{index}\n",
            "    D=A\n",
            "    @SP\n",
            "    A=M\n",
            "    M=D\n",
            "    @SP\n",
            "    M=M+1\n",
            "    @LCL\n",
            "    D=M\n",
            "    @SP\n",
            "    A=M\n",
            "    M=D\n",
            "    @SP\n",
            "    M=M+1\n",
            "    @ARG\n",
            "    D=M\n",
            "    @SP\n",
            "    A=M\n",
            "    M=D\n",
            "    @SP\n",
            "    M=M+1\n",
            "    @THIS\n",
            "    D=M\n",
            "    @SP\n",
            "    A=M\n",
            "    M=D\n",
            "    @SP\n",
            "    M=M+1\n",
            "    @THAT\n",
            "    D=M\n",
            "    @SP\n",
            "    A=M\n",
            "    M=D\n",
            "    @SP\n",
            "    M=M+1\n",
            "    @SP\n",
            "    D=M\n",
            "    @5\n",
            "    D=D-A\n",
            f"    @{arg2}\n",
            "    D=D-A\n",
            "    @ARG\n",
            "    M=D\n",
            "    @SP\n",
            "    D=M\n",
            "    @LCL\n",
            "    M=D\n",
            f"    @{arg1}\n",
            "    0;JMP\n",
            f"({arg1}$ret.{index})\n",
        ]
