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