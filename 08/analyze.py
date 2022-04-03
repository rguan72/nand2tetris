import sys

file = sys.argv[1]
with open(file, "r") as ifstream, open(file + ".analyze", "w") as ofstream:
    lines = []
    numCommented = 0
    numLabels = 0
    for lineNum, line in enumerate(ifstream.readlines()):
        if line.startswith("("):
            numLabels += 1
        elif line.startswith("//"):
            lines.append(str(lineNum - numCommented - numLabels) + " " + line)
            numCommented += 1
    ofstream.writelines(lines)

