import random
import encryptbase as eb
from ngram_score import ngram_score
from tqdm import *
import ciphers as c
import hilllclimb
import time

TEXT = raw_input('> ')


MUTATION_PROBABILITY = 10


TEXT = c.clean(TEXT)
letters = []
for i in range(26):
    letters.append(chr(i + 97).upper())

fitness = ngram_score('english_quadgrams.txt')


def randkey():
    out = []
    for i in range(26):
        out.append(chr(i + 97).upper())
    random.shuffle(out)
    return out[:]


def decrypt(text, key):
    out = ''
    for i in text:
        out += str(key[letters.index(i.upper())])
    return out


def createpop():
    out = []
    for i in range(100):
        out.append(randkey())
    return out


def intercourse(x, y):
    xlen = random.randint(0, 26)
    out = x[:xlen] + y[xlen:]
    if len(out) > 26:
        print('ERR')
    notin = []
    inkey = []
    double = []
    for i in letters:
        if i not in out:
            notin.append(i)
    for i in out:
        if i not in inkey:
            inkey.append(i)
        else:
            double.append(i)
    # print(notin)
    # print(double)
    for i in double:
        # print(double.index(i))
        out[out.index(i)] = notin[double.index(i)]
    return out


def purge(pop, text):
    fits = []
    newpopulation = []
    for i in pop:
        fit = fitness.score(decrypt(text, i))
        fits.append(fit)
    fitscopy = fits[:]
    fits = sorted(fits)
    highest = fits[len(fits) - 1]
    fits = fits[33:]
    for i in fits:
        newpopulation.append(pop[fitscopy.index(i)])
    return [newpopulation, highest]


def breed(pop):  # EXPECTS POPULATION SIZE 66 AFTER THE PURGE
    final = []
    for i in range(33):
        tofinal = intercourse(pop[i], pop[i + 32])
        final.append(tofinal)
    out = mutate(final)
    out += pop
    return out


def swap(key):
    nkey = key[:]
    a = random.randint(0, 25)
    b = random.randint(0, 25)
    x = nkey[a]
    y = nkey[b]
    nkey[a] = y
    nkey[b] = x
    return nkey


def mutate(popl):
    x = popl[:]
    #print('LEN ' + str(len(x)))
    for i in range(len(x)):
        chance = random.randint(0, 100)
        if chance <= MUTATION_PROBABILITY:
            g = x[i]
            x.remove(g)
            x.insert(i, swap(g))
            if len(x[i]) != 26:
                print('Oh crap')
    return x


def bigbang(text):
    start = time.clock()
    high = -10000
    p = createpop()
    iters = 0
    noimproves = 0
    while True:
        purged = purge(p, text)[0]
        nhigh = purge(p, text)[1]
        if nhigh > high:
            high = nhigh
            print('Highest: ' + str(high) + '  Iter: ' +
                  str(iters) + '  Time: ' + str(time.clock()))
            print(decrypt(text, sorted(p)[len(p) - 1]))
            noimproves = 0
        else:
            noimproves += 1
        p = breed(purged)
        iters += 1
        if noimproves > 20:
            hilllclimb.go(decrypt(text, sorted(
                p)[len(p) - 1]), sorted(p)[len(p) - 1])


bigbang(TEXT)
