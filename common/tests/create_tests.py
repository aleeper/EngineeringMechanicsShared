#!/usr/bin/python

import sys
import os
import re

testTemplateText = \
'''\documentclass[10pt,letterpaper]{article}
\usepackage[letterpaper, landscape, margin=1in]{geometry}
\usepackage{%s}
\\begin{document}
\subsection*{Command tests for package \\texttt{%s}:}
%s
\end{document}
'''

def getBasename(filename):
    return os.path.splitext(os.path.basename(filename))[0]

def createTableString(testCases):

    tableStartText = ("\n\\begin{tabular}{l|l}\n" +
                      "  Command & Result\n" +
                      "  \\\\[0.45pc] \hline\n")
    tableEndText = "\end{tabular}\n"

    maxElementsPerTable = 20

    text = tableStartText
    count = 0

    for testCase in testCases:
        count += 1
        if count > maxElementsPerTable:
            count = 0
            text += tableEndText + "\clearpage" + tableStartText
        text += "    \\verb|%s| & %s\n" % (testCase, testCase)
        text += "  \\\\[0.45pc]\n"

    text += tableEndText
    return text

def createFileString(basename, testCases):
    bodyText = createTableString(testCases)
    return testTemplateText % (basename, basename, bodyText)


def main(filename):

    print("filename = %s" % filename)
    basename = getBasename(filename)
    print("basename = %s" % basename)

    testCases = []
    pattern = re.compile(r"% test: (\\[A-Za-z]*(?:\[.*?\])?(?:{[^%]*})*)\s*(?:%.*)?$")
    # pattern = re.compile(r"% test:\s*((?:(?:\s*or\s*)?\\[A-Za-z]*(?:\[.*?\])?(?:{[^%]*})*)*)\s*(?:%.*)?$")
    with open(filename, 'r') as f:
        for line in f:
            match = pattern.search(line)
            if match:
                testCase = match.group(1)
                print "Found test case: %s" % testCase
                testCases.append(testCase)
            else:
                pass

    testFileName = "test_%s.tex" % basename

    with open(testFileName, 'w') as f:
        f.write(createFileString(basename, testCases))

    return 0


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: %s input.tex" % sys.argv[0])
        sys.exit(1)

    resultCode = main(sys.argv[1])
    sys.exit(resultCode)
