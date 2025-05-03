import re
import argparse
parser = argparse.ArgumentParser(
                    prog='auiabsbhhhhhtlircpuimldoioeppppppp.py',
                    description='auiabsbhhhhhtlircpuimldoioeppppppp utils',
                    epilog='Text at the bottom of help')
parser.add_argument('file', nargs='?', help='file to process')
parser.add_argument('--compile', '-c', help='compiles to a python file', action='store_true')
parser.add_argument('--outfile', help='file to compile to with -c')
args = parser.parse_args()
commands = [
    '(?i)guys i can vouch [a-z_]+ is [0-9]+$',  # Sets variable [PLAYER] to integer [VALUE]
    '(?i)[a-z_]+ can vouch go and tell them come on$',  # Prints ascii character of the id of the variable [PLAYER]'s value.
    '(?i)[a-z_]+ is just like [a-z_]+$',  # Sets [PLAYER]'s value to that of [SUSSYPLAYER]
    '(?i)if its not [a-z_]+ then vote me$',  # If [PLAYER]'s value is not 0, execute the next line, otherwise, skip it.
    '(?i)idk what [a-z_]+ is but its between [0-9]+ and [0-9]+$',  # Set [PLAYER]'s value to a random integer between [MIN] and [MAX]
    '(?i)[a-z_]+ was the impostor$',  # If [PLAYER] is not 0, end the program at that line.
    '(?i)[a-z_]+ goes up$',  # Add 1 to [PLAYER]
    '(?i)[a-z_]+ goes down$',  # Subtract 1 from [PLAYER]
    '(?i)[a-z_]+ who are you$',  # Recieve a character as user input, and save its ascii value at [PLAYER]
]

def parseline(s):
    s =s.split('//', 1)[0].strip()
    slist = s.split(' ')
    for i in range(len(commands)):
        if re.match(commands[i], s):
            match i:
                case 0:
                    var = slist[4]
                    new = slist[6]
                    return f'{var} = {new}\n'
                case 1:
                    var = slist[0]
                    return f'print(chr({var}),  end="")\n'
                case 2:
                    var1 = slist[0]
                    var2 = slist[4]
                    return f'{var1} = {var2}\n'
                case 3:
                    var = slist[3]
                    return f'if {var} != 0:\n   '
                case 4:
                    var = slist[2]
                    minimum = slist[7]
                    maximum = slist[9]
                    return f'{var} = random.randint({minimum}, {maximum})\n'
                case 5:
                    var = slist[0]
                    return f'if {var} != 0:\n   exit()\n'
                case 6:
                    var = slist[0]
                    return f'{var} = {var} + 1\n'
                case 7:
                    var = slist[0]
                    return f'{var} = {var} - 1\n'
                case 8:
                    var = slist[0]
                    return f'{var} = ord(input("input a character: "))\n'
    return ''
def parsetext(s):
    text = 'import random\n'
    for i in s.splitlines():
        text = text + parseline(i)
    return text
def init():
    if args.compile:
        if args.file:
            if args.outfile:
                with open(args.file) as file:
                    out = parsetext(file.read())
                with open(args.outfile, 'w') as file:
                    file.write(out)
            else:
                with open(args.file) as file:
                    out = parsetext(file.read())
                with open(args.file+'-compiled.py', 'w') as file:
                    file.write(out)
        else:
            print('Error: no file to process')
    elif args.file:
        exec(parsetext(open(args.file, 'r').read()))
    else:
        print('Interactive auiabsbhhhhhtlircpuimldoioeppppppp')
        while True:
            exec(parsetext(input('>>> ')))
if __name__ == '__main__':
    init()