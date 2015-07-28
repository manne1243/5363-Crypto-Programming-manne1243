###############################################
# Name: SAMPATH KUMAR MANNE
# Class: CMPS 5363 Cryptography
# Date: 28 July 2015
# Program 2 - Vigenere Cipher
###############################################

import random
import string
from pprint import pprint
import argparse
import sys

##Declaring Symbols Globally.
symbols = """!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"""

## Function to generate a keyword from the seed
## For encrypting or decrypting the message.

def keywordFromSeed(seed):
    Letters = []
    seed = int(seed)
    #random.seed(seed)

    while seed > 0:
        Letters.insert(0,chr((seed % 100) % 26 + 65))
        seed = seed // 100
    return ''.join(Letters)

## Function to print the Vigenere in matrix form.
def printMatrix(v):
    i=0
    j=0
    k=0
    line = ""
    length = len(symbols)

    for i in range(length*length):
        line = line + v[j][k]
        j = j + 1
        if j >= 95:
            print(line)
            line = ""
            j = 0
            k = k + 1

## Building a Vigenere matrix by populating random values at random positions using given symbols.

def buildVigenere(seed):

    n = len(symbols)

    vig = [[0 for i in range(n)] for i in range(n)]
    temp = symbols

    for char in temp:
        random.seed(seed)
        exists = []
        for j in range(n):
            r = random.randrange(len(temp))
    
            if r not in exists:
                exists.append(r)
            
            else:
                while(r in exists):
                    r = random.randrange(len(temp))
                exists.append(r)
            while(vig[j][r] != 0):
                r = (r + 1) % n

            vig[j][r] = char
    return vig

## Function to encrypt and decrypt the given message based on the given mode.
            
def encrypt(m,mode,seed):
    v = buildVigenere(seed)
    #printMatrix(v)
    k = keywordFromSeed(seed)
    #print(k)

    mode = mode.lower()

    # Mode = 'Encode' will encrypt the message.
    if mode == 'encode':
        
        text = ""
        for i in range(len(m)):
            mi = i
            ki = i % len(k)

            # For loop for getting the coloumn index of the plaintext.
            temp1 = m[mi]
            col = 0
            for a in range(1):
                for b in range(len(symbols)):
                    if (temp1 == v[a][b]):
                        col = b

            # For loop to find the key letter in the vigenere matrix.
            # And get its coloumn index to map it to the cipher text in the same Coloumn

            temp2 = k[ki]
            row = 0
            for p in range(len(symbols)):
                for q in range(1):
                    if (temp2 == v[p][q]):
                        row = p

            text = text + v[row][col]
        return text

    # Mode = 'Decode' will decrypt the cipherText.
##    else:
def decrypt(m,mode,seed):

    v = buildVigenere(seed)
    k = keywordFromSeed(seed)
    if mode == 'decode':
        text2 = ""
        
        for i in range(len(m)):
            emi = i
            eki = i % len(k)

            # For loop for getting the row index of the keyword.
            row = 0
            temp = k[eki]
            for a in range(1):
                for b in range(len(symbols)):
                    if (temp == v[b][a]):
                         row = b
            # For loop to find the single cipher letter in the vigenere matrix.
            # And get its coloumn index to map it to the plain text in the same coloumn.
            col = 0
            temp2 = m[emi]
            for c in range(len(symbols)):
                if (temp2 == v[row][c]):
                    col = c

            text2 = text2 + v[0][col]     
        return text2

def main():

    cipherText = encrypt(message,'encode',seed)
    #print(cipherText)
    plainText = decrypt(cipherText,'decode',seed)
    #print(plainText)

        
if __name__ == '__main__':
    main()


