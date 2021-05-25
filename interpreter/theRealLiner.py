"""

*`prin` Prints the results of all the following function, and the numeric value
of any namespace.
*`let` converts an integer into its Unicode character.
*`if` returns the highest number of two different namespaces/function
*`set` override the numeric value of a namespace, and replaces the original in duplicate cases.
*`run` Run the function at the given numeric property, if no function is there, crashes.
*`add` add two numeric properties
*`sub` subtracts two numeric properties
*`split` run two functions
"""
class Liner:

    def __init__(self):
        self.namespaces = dict()
        self.reverseLookup = dict()
        self.functionLookup = dict()
        self.entranceLine = ""

    def addNamespace(self, namespace, numeric, function):
        self.namespaces.update({namespace : numeric})
        self.reverseLookup.update({numeric : namespace})
        self.functionLookup.update({namespace : function})

    def setEntranceLine(self, function):
        self.entranceLine = function

    def prin(self, function):
        functs = function.split(" ")
        output = ""
        for func in functs:
            output += str(self.runLine(func))
        print(output)

    def ifStatement(self, numericOne, numericTwo):
        return numericOne if (numericOne > numericTwo) else numericTwo

    def setNamespace(self, namespace, numeric):
        if not numeric.isdigit():
            numeric = self.evalLine(numeric)
        self.namespaces.update({namespace : numeric})
        self.reverseLookup.update({numeric : namespace})

    def runFunction(self, numeric):
        if not numeric.isdigit():
            numeric = self.evalLine(numeric)
        return self.runLine(self.functionLookup[self.reverseLookup[numeric]])

    def splitOperation(self, namespaceOne, namespaceTwo):
        self.runLine(self.functionLookup[namespaceOne[:-2]])
        self.runLine(self.functionLookup[namespaceTwo[:-2]])

    def inStatement(self):
        return int(input("Number: "))

    def evalLine(self, line):
        if line.endswith("()"):
            namespace = line.split("()")[0].strip()
            return self.runLine(self.functionLookup[namespace])
        elif len(line) == 0:
            exit(0)
        else:
            return self.namespaces[line.strip()]

    def start(self):
        self.runLine(self.entranceLine)

    def runLine(self, line):
        if 'prin' in line:
            self.prin(line.split("prin ")[1])

        elif 'let' in line:
            return chr(self.namespaces[line.split("let ")[1]])

        elif 'if' in line:
            args = line.split(" if ")
            return self.ifStatement(args[0], args[1])

        elif 'set' in line:
            args = line.split("set ")[1].split(" ")
            self.setNamespace(args[0], args[1])

        elif 'run' in line:
            return self.runFunction(line.split("run ")[1])

        elif 'add' in line:
            args = line.split(" add ")
            first = int(self.namespaces[args[0].strip()])
            second = int(self.namespaces[args[1].strip()])
            return first + second

        elif 'sub' in line:
            args = line.split(" sub ")
            first = int(self.namespaces[args[0].strip()])
            second = int(self.namespaces[args[1].strip()])
            return first - second

        elif 'split' in line:
            args = line.split(" split ")
            return self.splitOperation(args[0], args[1])

        elif line.strip() == 'in':
            return self.inStatement()

        else:
            return self.evalLine(line)
