import os
import sys

def getfiles():
    # Instruction(s) to get the list of PDF files goes here (and/or below)...
    entries = os.listdir('C:\\Users\\ankit\\Downloads')
    filelist = []
    for entry in entries:
        if entry.endswith('.pdf'):
            filelist.append(entry)
    return filelist

print(getfiles())
