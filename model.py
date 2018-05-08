from hashlib import sha1, sha224, sha256, sha384, sha512

class Blockchain:
    def __init__(self):
        self.bl = []
        self.nu = 0
    def append(self, block):
        self.bl.append(block)
        self.nu += 1

class Block:
    def __init__(self):
        self.tr = []
        self.nu = 0
    def append(self, transaction):
        self.tr.append(transaction)
        self.nu += 1

class Transaction:
    def __init__(self, fr, to, am, fe):
        self.fr = fr
        self.to = to
        self.am = am
        self.fe = fe

class Users:
    def __init__(self):
        self.us = []
        self.nu = 0
    def append(self, user):
        self.us.append(user)
        self.nu += 1
        
class User:
    def __init__(self, us=Users):
        self.ID = sha256(us.nu.encode('utf-8')).hexdigest()

def binary(string):
    return "".join([format(ord(i), 'b') for i in string])

def hash(block, string):
    if block % 5 == 0: return binary(sha1(string.encode('utf-8')).hexdigest())
    elif block % 5 == 1: return binary(sha224(string.encode('utf-8')).hexdigest())
    elif block % 5 == 2: return binary(sha256(string.encode('utf-8')).hexdigest())
    elif block % 5 == 3: return binary(sha384(string.encode('utf-8')).hexdigest())
    else: return binary(sha512(string.encode('utf-8')).hexdigest())

def leadingOnes(string):
    i = 0
    while(string[i] != '0'):
        i += 1
        if i == len(string): return i
    return i
'''
tries = 0
max1 = -1
while(max1 != 4):
    max1 = max(max1, leadingOnes(hash(2, str(tries))))
    print(tries,leadingOnes(hash(2, str(tries))))
    tries += 1
print(tries, hash(2, str(tries)))
'''
