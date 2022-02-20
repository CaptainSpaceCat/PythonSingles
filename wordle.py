'''
wordle.py
author - Connor Settle

example usage: python wordle.py bbbgb yybgb gbggg ggggg
g - green square
y - yellow square
b - black square

the program will output a string that can be pasted into Slack 
to make a fancy visual of your performance in a game of wordle

supports any word length and any number of guesses
'''


import sys

def expand(s):
    if s == 'g':
        return ":large_green_square:"
    if s == 'y':
        return ":large_yellow_square:"
    if s == 'b':
        return ":black_large_square:"

def convert(msg):
    out = ""
    for char in msg:
        print(char)
        out += expand(char)
    out += "\n"
    return out

def main(args):
    first = True
    total = ""
    for msg in args:
        if first:
            first = False
            continue
        print(msg)
        total += convert(msg)
    return total


print(main(sys.argv))
