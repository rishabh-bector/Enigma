from tqdm import *
import time


nms = ['zero','one','two','three','four','five','six','seven','eight','nine']

def clean(text):
    ls = list(text.lower().replace(' ', ''))
    out = ''
    for i in ls:
        if i.isdigit():
            out += nms[int(i)]
        if i.isalpha():
            out += i
    return out

def tonumber(x):
    return ord(x) - 96

def toletter(x):
    return str(chr(int(x) + 96))

def frequency(text):
    out = {}
    for i in range(26):
        out[chr(i + 97)] = 0
    for i in text.lower():
        out[i] += 1
    return out

def cshift(text, amount):
    ls = list(clean(text))
    out = []
    for char in ls:
        out.append(chr(((ord(char) - 97 + amount) % 26) + 97))
    return ''.join(out)

def keyshift(text, key):   #BUGGY
    text = clean(text)
    lsk = list(key)
    lst = list(text)
    q = []
    for i in lsk:
        q.append(tonumber(i))
    out = []
    c = 0
    for i in range(len(lst)):
        s = q[i % (len(q) - 1)]
        x = (tonumber(lst[i]) + s) % 26
        out.append(toletter(x))
    return ''.join(out)

def gcf(a, b):
    lower = sorted([a, b])[0]
    for i in range(lower):
        x = lower - i
        if a % x == 0 and b % x == 0:
            return x

def phi(x):
    out = 0
    for i in range(x):
        if gcf(i, x) == 1:
            out += 1
    return out

def isprime(x):
    for i in range(2, x // 2):
        if x % i == 0:
            return False
    return True

def primefactor(x):
    factors = []
    c = x
    i = 2
    while i < x:
        if c == 1:
            return factors
        if c % i == 0:
            factors.append(i)
            c /= i
        else:
            i += 1
    return x
