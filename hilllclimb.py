from math import *
from ngram_score import ngram_score
import random
import numpy as np
import time
import ciphers

THING='hellotherethisisamessagetestingifthingsworkornot'

def Scramble(String):
    start=list(range(26))
    new=[]
    for i in range(26):
        r=random.choice(start)
        new.append(r)
        start.remove(r)
    print(new)
    newString=""
    midString=""
    String=String.lower()
    for i in String:
        if i.isalpha():
            midString+=i

    for i in midString:
        newString+=chr(new[ord(i)-97]+97)
    return newString

MESSAGE = Scramble(THING)

fitness = ngram_score('english_quadgrams.txt')

letters = []
for i in range(26):
    letters.append(chr(i + 97).upper())

def randkey():
    out = []
    for i in range(26):
        out.append(chr(i + 97).upper())
    random.shuffle(out)
    return out[:]

def decrypt(text, key):
    out = ''
    for i in text:
        out += key[letters.index(i.upper())]
    return out

def changekey(key):
    nkey = key[:]
    a = random.randint(0, 25)
    b = random.randint(0, 25)
    x = nkey[a]
    y = nkey[b]
    nkey[a] = y
    nkey[b] = x
    return nkey

def go(txt, startkey):
    MESSAGE = ciphers.clean(txt)
    cont = 0
    itercounter = 0
    besttext = None
    bestfitness = -1000000
    bestkey = None

    start = time.clock()


    while True:
        if startkey == None:
            key = randkey()
        else:
            key = startkey
        badcounter = 0
        while badcounter < 1000:
            cfitness = fitness.score(decrypt(MESSAGE, key))
            #print(cfitness)
            nkey = changekey(key[:])
            if key == nkey:
                #print('error')
                badcounter += 1
            nfitness = fitness.score(decrypt(MESSAGE, nkey))
            if nfitness > cfitness:
                key = nkey[:]
                if nfitness > bestfitness:
                    bestfitness = nfitness
                    besttext = decrypt(MESSAGE, nkey)
                    bestkey = nkey
                    print('current best: iteration ' + str(itercounter))
                    print(besttext)
                    print(letters)
                    print(bestkey)
                    print('fitness:' + str(bestfitness))
                    print('time elapsed: ' + str(time.clock()))


            elif cfitness > nfitness:
                badcounter += 1
            itercounter += 1
        cont += 1
