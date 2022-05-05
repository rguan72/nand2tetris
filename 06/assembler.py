import os
import sys 

class SymbolTable:
    def __init__(self):
        self.table = {}
        self.numVars = 0

def assemble(filename):
    inputAssembly = getInputAssembly(filename)
    machineCode = translateAssembly(inputAssembly)
    writeOutput(machineCode, filename)

def getInputAssembly(filename: str) -> list[str]:
    with open(filename, "r") as ifstream:
        return ifstream.readlines()

def translateAssembly(inputAssembly: list[str]) -> list[str]:
    symbolTable = initializeSymbolTable()
    symbolTable = addLabels(symbolTable, inputAssembly)
    outputMachineCode = []
    for line in inputAssembly:
        if isRealCode(line):
            outputMachineCode.append(translateLine(line, symbolTable))
    return outputMachineCode

def writeOutput(machineCode: list[str], filename: str) -> None:
    filenameBase, _ = os.path.splitext(filename)
    with open(f"{filenameBase}.hack", "w") as ofstream:
        ofstream.writelines([f"{line}\n" for line in machineCode])

def initializeSymbolTable() -> SymbolTable:
    symbolTable = SymbolTable()
    table = {
        "SCREEN": 16384,
        "KBD": 24576,
        "SP": 0,
        "LCL": 1,
        "ARG": 2,
        "THIS": 3,
        "THAT": 4,        
    }
    for i in range(16):
        table[f"R{i}"] = i
    symbolTable.table = table
    return symbolTable

def addLabels(symbolTable: SymbolTable, inputAssembly):
    linesOfRealCode = 0
    for line in inputAssembly:
        if isRealCode(line):
            linesOfRealCode += 1
        elif isLabel(line):
            symbolTable.table[getLabel(line)] = linesOfRealCode
    return symbolTable

def isRealCode(line: str):
    return len(line.strip()) > 0 and line.strip()[0:2] != "//" and line.strip()[0] != "("

def translateLine(line: str, symbolTable: SymbolTable) -> str:
    proccessed = cleanupLine(line)
    if isAInstruction(proccessed):
        instructionValueOrSymbol = proccessed[1:]
        if not instructionValueOrSymbol.isnumeric():
            if instructionValueOrSymbol in symbolTable.table:
                instructionValue = symbolTable.table[instructionValueOrSymbol]
            else:
                variableBaseAddress = 16
                instructionValue = variableBaseAddress + symbolTable.numVars
                symbolTable.numVars += 1
                symbolTable.table[instructionValueOrSymbol] = instructionValue
        else:
            instructionValue = instructionValueOrSymbol
        return f"0{padZeros(toBinary(instructionValue))}"
    elif isCInstruction(proccessed):
        dest, comp, jump = parseCInstruction(proccessed)
        return translateCInstruction(dest, comp, jump)

def cleanupLine(line: str) -> str:
    if "//" in line:
        line, _ = line.split("//")
    return line.strip()

def isLabel(line: str) -> bool:
    return len(line.strip()) > 0 and line.strip()[0] == "("

def getLabel(line: str) -> bool:
    return line.strip()[1:-1]

def isAInstruction(line: str) -> bool:
    return line[0] == "@"

def isCInstruction(line: str) -> bool:
    return len(line) > 0 and not isLabel(line) and not isAInstruction(line)

def padZeros(binary: int) -> str:
    return "0" * (15 - len(str(binary))) + str(binary)

def toBinary(line: str) -> int:
    currValue = int(line)
    output = 0
    iterCount = 0
    while currValue > 0:
        output += (currValue % 2) * 10 ** iterCount
        currValue //= 2
        iterCount += 1
    return output

def parseCInstruction(instr: str):
    if "=" in instr:
        dest, rest = instr.split("=")
    else:
        dest = None
        rest = instr
    if ";" in rest:
        comp, jump = rest.split(";")
    else:
        comp = rest
        jump = None
    dest = "".join(sorted(dest)) if dest is not None else dest
    return (dest, comp, jump)

def translateCInstruction(dest: str, comp: str, jump: str) -> str:
    return f"111{translateComp[comp]}{translateDest[dest]}{translateJump[jump]}"


translateComp = {
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",
    "!D": "0001101",
    "!A": "0110001",
    "-D": "0001111",
    "-A": "0110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "D+A": "0000010",
    "A+D": "0000010",
    "D-A": "0010011",
    "A-D": "0000111",
    "D&A": "0000000",
    "A&D": "0000000",
    "D|A": "0010101",
    "A|D": "0010101",
    "M": "1110000",
    "!M": "1110001",
    "-M": "1110011",
    "M+1": "1110111",
    "M-1": "1110010",
    "D+M": "1000010",
    "M+D": "1000010",
    "D-M": "1010011",
    "M-D": "1000111",
    "D&M": "1000000",
    "M&D": "1000000",
    "D|M": "1010101",
    "M|D": "1010101",
}

translateDest = {
    None: "000",
    "M": "001",
    "D": "010",
    "DM": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "ADM": "111",
}

translateJump = {
    None: "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111",
}


if __name__ == "__main__":
    assemble(sys.argv[1])
