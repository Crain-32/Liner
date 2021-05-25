import sys
from theRealLiner import Liner

if len(sys.argv) == 0:
    print("No File provided!")
    exit(1)

foo = Liner()
with open(sys.argv[1],'r') as linerProgram:
    lineNumber = 1
    for line in linerProgram:
        if line.startswith("C"):
            lineNumber += 1
            continue
        elif len(line.strip()) == 0:
            lineNumber += 1
            continue
        elif ';' in line:
            args = line.split(";")
            foo.addNamespace(args[0].strip(), lineNumber, args[1].strip())
            lineNumber += 1
            continue
        else:
            foo.setEntranceLine(line.strip())
            lineNumber += 1
    foo.start()
