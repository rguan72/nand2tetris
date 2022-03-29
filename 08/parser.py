import typing
import dataclasses
import enum

from setuptools import Command

def parse(lines: typing.List[str]) -> list:
    """
    Reads a file and returns a list of commands.
    """
    lines = filterCommentsAndBlankLines(lines)
    return [parseLine(line) for line in lines]

def filterCommentsAndBlankLines(lines: typing.List[str]) -> typing.List[str]:
    """
    Filters out comments and blank lines.
    """
    lines = [line.strip('\n') for line in lines]
    return list(filter(lambda line: not line.startswith("//") and not len(line) == 0, lines))

def parseLine(line: str) -> Command:
    """
    Parses a single line of code.
    """
    lineWords = line.split(" ")
    commandType = commandToType[lineWords[0]]
    if commandType == CommandType.C_ARITHMETIC:
        return Command(commandType, lineWords[0], None)
    args1 = lineWords[1] if commandType != CommandType.C_RETURN else None
    args2 = lineWords[2] if commandType in [CommandType.C_PUSH, CommandType.C_POP, CommandType.C_FUNCTION, CommandType.C_CALL] else None
    return Command(commandType, args1, args2)

class CommandType(enum.Enum):
    C_ARITHMETIC = 1
    C_PUSH = 2
    C_POP = 3
    C_LABEL = 4
    C_GOTO = 5
    C_IF = 6
    C_FUNCTION = 7
    C_RETURN = 8
    C_CALL = 9

@dataclasses.dataclass
class Command:
    commandType: CommandType
    arg1: str
    arg2: int

commandToType = {
    "add": CommandType.C_ARITHMETIC,
    "sub": CommandType.C_ARITHMETIC,
    "neg": CommandType.C_ARITHMETIC,
    "eq": CommandType.C_ARITHMETIC,
    "gt": CommandType.C_ARITHMETIC,
    "lt": CommandType.C_ARITHMETIC,
    "and": CommandType.C_ARITHMETIC,
    "or": CommandType.C_ARITHMETIC,
    "not": CommandType.C_ARITHMETIC,
    "push": CommandType.C_PUSH,
    "pop": CommandType.C_POP,
    "label": CommandType.C_LABEL,
    "goto": CommandType.C_GOTO,
    "if-goto": CommandType.C_IF,
    "function": CommandType.C_FUNCTION,
    "call": CommandType.C_CALL,
    "return": CommandType.C_RETURN,
}
