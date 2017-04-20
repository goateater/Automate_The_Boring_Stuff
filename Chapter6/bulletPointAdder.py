#/usr/bin/python3
# Author: CrazyWhiteMonkey
# Date: April 20, 2017
# What is this? = Adds Wikipedia bullet points to the start
# Script Name =  bulletPointAdder.py
#Usage = Run this after using pw.py, and it will paste whatever is in your clipboard

import pyperclip
text = pyperclip.paste()

# Seperate lines and add star

lines = text.split('\n')

for i in range(len(lines)): # loop throughall indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list
print(lines[i])
text = '\n'.join(lines)

pyperclip.copy(text)
print(text)
