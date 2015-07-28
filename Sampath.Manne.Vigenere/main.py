###############################################
# Name: SAMPATH KUMAR MANNE
# Class: CMPS 5363 Cryptography
# Date: 28 July 2015
# Program 2 - Vigenere Cipher
###############################################

import argparse
import sys
import math
import randomized_vigenere as rv

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode", dest="mode", default = "encode", help="Encode or Decode")
    parser.add_argument("-i", "--inputfile", dest="plainText", help="Input Name")
    parser.add_argument("-o", "--outputfile", dest="outputFile", help="Output Name")
    parser.add_argument("-s", "--seed", type=int,help="Integer seed")
    #parser.add_argument("-t", "--type", dest="type",help="Encoding / Decoding mode [encode,decode]")
    
    args = parser.parse_args()
    
    f1 = open(args.plainText,'r')
    message = f1.read()

    # IF given mode is encode encrypt function is called else decrypt function is called.

    if(args.mode == 'encode'):
        data = rv.encrypt(message,args.mode,args.seed)
    else:
        data = rv.decrypt(message,args.mode,args.seed)
    #To write the encoded or plain text into a file
    o = open(args.outputFile,'w')
    o.write(str(data))        

if __name__ == '__main__':
    main()
