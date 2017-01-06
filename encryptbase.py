from random import *
import subprocess
from tqdm import *

def tonumber(ls):
    output = []
    print('Enumerating...')
    for character in tqdm(ls):
        output.append(ord(character) - 96)
    return output

def toletter(ls):
    output = []
    print('Lettering...')
    for number in tqdm(ls):
        output.append(str(chr(int(number) + 96)))
    return output

def splice(sentence):
    output = list(sentence)
    return output

def unsplice(ls):
    output = ''.join(ls)
    return output

def shiftls(ls, amount):
    output = []
    print('Shifting...')
    for item in tqdm(ls):
        output.append((item + amount) % 26)

def codegen(ls):
    output = []
    print('Generating Code...')
    for item in tqdm(ls):
        output.append(randint(0, 10))
    return output

def shiftbycode(ls, code):
    output = []
    print('Shifting...')
    lslen = len(ls)
    code = list(code)
    codelen = len(code)
    count = 0
    while count < lslen:
        char = (ls[count] + code[count]) % 26
        output.append(char)
        count += 1
    return output

def returnbycode(ls, code):
    output = []
    print('Decoding...')
    lslen = len(ls)
    codelen = len(code)
    count = 0
    while count < lslen:
        char = (ls[count] - code[count]) % 26
        output.append(char)
        count += 1
    return output

#-------------------- FULL CONVERSIONS --------------------#

def fullencode(message):
    message = tonumber(splice(message))
    code = codegen(message)
    print('CODE: ' + str(code))
    message = shiftbycode(message, code)
    return [message, code]

def fulldecode(message, code):
    output = returnbycode(message, code)
    output = toletter(output)
    output = unsplice(output)
    return output
