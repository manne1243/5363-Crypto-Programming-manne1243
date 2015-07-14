###############################################
# Name: SAMPATH KUMAR MANNE
# Class: CMPS 5363 Cryptography
# Date: 13 July 2015
# Program 1 - Playfair Cipher
###############################################
'''
Objective: Create a program that creates a Playfair matrix
	using the given key and either encrypts or decrypts a
	message using the generated matrix.
'''

import pprint
import re

class StringManip:
    """
    Helper class to speed up simple string manipulation
    """

    def generateAlphabet(self):
        #Create empty alphabet string
        alphabet = ""

        #Generate the alphabet
        for i in range(0,26):
            alphabet = alphabet + chr(i+65)

        return alphabet


    def cleanString(self,s,options = {'up':1,'reNonAlphaNum':1,'reSpaces':'','spLetters':'X'}):
        """
        Cleans message by doing the following:
        - up            - uppercase letters
        - spLetters     - split double letters with some char
        - reSpaces      - replace spaces with some char or '' for removing spaces
        - reNonAlphaNum - remove non alpha numeric
        - reDupes       - remove duplicate letters

        @param   string -- the message
        @returns string -- cleaned message
        """
        if 'up' in options:
            s = s.upper()

        if 'spLetters' in options:
            #replace 2 occurences of same letter with letter and 'X'
            s = re.sub(r'([ABCDEFGHIJKLMNOPQRSTUVWXYZ])\1', r'\1X\1', s)
        if 'renum' in options:
            s = re.sub(r'[\d]','',s)

        if 'reSpaces' in options:
            space = options['reSpaces']
            s = re.sub(r'[\s]', space, s)

        if 'reNonAlphaNum' in options:
            s = re.sub(r'[^\w]', '', s)

        if 'reDupes' in options:
            s= ''.join(sorted(set(s), key=s.index))

        return s


class PlayFair:
    """
    Class to encrypt via the PlayFair cipher method
    Methods:

    - generateSquare
    - transposeSquare
    -
    """

    def __init__(self,key,message):
        self.Key = key
        self.Message = message
        self.Square = []
        self.Transposed = []
        self.StrMan = StringManip()
        self.Alphabet = ""

        self.generateSquare()
        self.transposeSquare()

        self.Message = self.StrMan.cleanString(self.Message,{'up':1,'reSpaces':'','reNonAlphaNum':1,'spLetters':1})
        if (len(self.Message) % 2 == 1):
            self.Message += "X"
        #print(self.Message)

    def generateSquare(self):
        """
        Generates a play fair square with a given keyword.

        @param   string   -- the keyword
        @returns nxn list -- 5x5 matrix
        """
        row = 0     #row index for sqaure
        col = 0     #col index for square

        #Create empty 5x5 matrix
        self.Square = [[0 for i in range(5)] for i in range(5)]

        self.Alphabet = self.StrMan.generateAlphabet()

        #uppercase key (it meay be read from stdin, so we need to be sure)
        self.Key = self.StrMan.cleanString(self.Key,{'up':1,'reSpaces':'','reNonAlphaNum':1,'reDupes':1,'renum':1})

        #Load keyword into square
        for i in range(len(self.Key)):
            self.Square[row][col] = self.Key[i]
            self.Alphabet = self.Alphabet.replace(self.Key[i], "")
            col = col + 1
            if col >= 5:
                col = 0
                row = row + 1

        #Remove "J" from alphabet
        self.Alphabet = self.Alphabet.replace("J", "")

        #Load up remainder of playFair matrix with
        #remaining letters
        for i in range(len(self.Alphabet)):
            self.Square[row][col] = self.Alphabet[i]
            col = col + 1
            if col >= 5:
                col = 0
                row = row + 1

    def transposeSquare(self):
        """
        Turns columns into rows of a cipher square

        @param   list2D -- playFair square
        @returns list2D -- square thats transposed
        """
        #Create empty 5x5 matrix
        self.Transposed = [[0 for i in range(5)] for i in range(5)]

        for col in range(5):
            for row in range(5):
               self.Transposed[col][row] = self.Square[row][col]


    def getCodedDigraph(self,digraph):
        """
        Turns a given digraph into its encoded digraph whether its on
        the same row, col, or a square

        @param   list -- digraph
        @returns list -- encoded digraph
        """
        newDigraph = ['','']

        #Check to see if digraph is in same row
        for row in self.Square:
            if digraph[0] in row and digraph[1] in row:
                newDigraph[0] = row[((row.index(digraph[0])+1)%5)]
                newDigraph[1] = row[((row.index(digraph[1])+1)%5)]
                return newDigraph

        #Check to see if digraph is in same column
        for row in self.Transposed:
            if digraph[0] in row and digraph[1] in row:
                newDigraph[0] = row[((row.index(digraph[0])+1)%5)]
                newDigraph[1] = row[((row.index(digraph[1])+1)%5)]
                return newDigraph


        #Digraph is in neither row nor column, so it's a square
        location1 = self.getLocation(digraph[0])
        location2 = self.getLocation(digraph[1])
        
        return [self.Square[location1[0]][location2[1]],self.Square[location2[0]][location1[1]]]

    def getDeCodedDigraph(self,digraph):
        """
        Turns a given digraph into its decoded digraph whether its on
        the same row, col, or a square

        @param   list -- digraph
        @returns list -- decoded digraph
        """
        newDigraph = ['','']

        #Check to see if digraph is in same row
        for row in self.Square:
            if digraph[0] in row and digraph[1] in row:
                newDigraph[0] = row[((row.index(digraph[0])-1)%5)]
                newDigraph[1] = row[((row.index(digraph[1])-1)%5)]
                return newDigraph

        #Check to see if digraph is in same column
        for row in self.Transposed:
            if digraph[0] in row and digraph[1] in row:
                newDigraph[0] = row[((row.index(digraph[0])-1)%5)]
                newDigraph[1] = row[((row.index(digraph[1])-1)%5)]
                return newDigraph


        #Digraph is in neither row nor column, so it's a square
        location1 = self.getLocation(digraph[0])
        location2 = self.getLocation(digraph[1])
        
        return [self.Square[location1[0]][location2[1]],self.Square[location2[0]][location1[1]]]



    def getLocation(self,letter):
        row = 0
        col = 0

        count = 0
        for list in self.Square:
            if letter in list:
                row = count
            count += 1

        count = 0
        for list in self.Transposed:
            if letter in list:
                col = count
            count += 1
        return [row,col]
    

    i =0
    #############################################
    # Helper methods just to see whats going on
    #############################################
    def printNewKey(self):
        print(self.Key)

    def printNewMessage(self):
        #print(self.Message)
        return self.Message
        
    def printSquare(self):
        for list in self.Square:
            print(list)
        print('')

    def printTransposedSquare(self):
        for list in self.Transposed:
            print(list)
        print('')
        
#Declaring empty strings.
decision = ""
enc = ""
dec = ""
noX=""

#Loop to give user the options to make the decision.
#1 for encryption
#2 for decryption
#3 to Quit
while decision is not "1" and decision is not "2":

    print ("Playfair Encryption Tool (P.E.T)")
    print ("Written By: Sampath Kumar Manne") 
    print ("********************************************************")
    print ("Would you like to encrypt or decrypt a message?")
    print ("1 - Encrypt message")
    print ("2 - Decrypt Message")
    print ("3 - Quit")
    print ("=>")
    print ("********************************************************")
    decision = input("Enter Decision :\t")
    print("")
    
    if decision == "1":
        print ("Playfair Encryption Tool (P.E.T)")
        print ("Written By: Sampath Kumar Manne") 
        print ("********************************************************")
        key = input("\nPlease enter a keyword:\n")
        print ("********************************************************")
        enc_message = input("\nPlease enter the plain text :\n")
        print ("********************************************************")
    
        # Creating an instance of the class PlayFair
        myCipher = PlayFair(key, enc_message)
        changedText= myCipher.printNewMessage()
        index = 0
        #To convert the list assigned to en_value into strings.
        while(index<len(changedText)-1):
            en_value = myCipher.getCodedDigraph([changedText[index], changedText[index+1]])
            en_value = ''.join(en_value)
            index = index + 2
            enc = enc + en_value
            
        print("\nGiven key :",key)
        print("Plain text :",enc_message)
        print("\nYour Encrypted message is:")
        print(enc)
        print ("*******************The end******************************")
                 
    elif decision == "2":

        print ("Playfair Encryption Tool (P.E.T)")
        print ("Written By: Sampath Kumar Manne") 
        print ("********************************************************")
        
        key = input("\nPlease enter the keyword:\n")
        print ("********************************************************")
        dec_message = input("\nEnter the Encrypted message:\n")
        myCipher = PlayFair(key, dec_message)
        changedText = dec_message

        index = 0
        #To convert the list assigned to en_value into strings.
        while(index<len(changedText)-1):
            de_value = myCipher.getDeCodedDigraph([changedText[index], changedText[index+1]])
            de_value = ''.join(de_value)
            index = index + 2
            dec = dec + de_value

        '''
        # For removing the X from the cipher text when printing the plain text
        temp = dec
        #print(len(temp))
        
        for i in range(1,len(temp)-2):
            if temp[i] == 'X':
                if temp[i-1] == temp[i+1]:
                    temp = "%c%c" % (temp[i],"X")
                    temp = ''.join(temp)

        final_dec = temp
        '''    
        print("\nGiven key :",key)
        print("Cipher text :",dec_message)
        print ("********************************************************")
        print("\nYour Decrypted message is:")
        #To remove the char X from the decrypted message.
        x = re.sub(r'([ABCDEFGHIJKLMNOPQRSTUVWXYZ](X)[ABCDEFGHIJKLMNOPQRSTUVWXYZ])\1',"",dec)
        print(x)
        print ("*******************The end******************************")
    # To Quit from the P.E.T       
    else:
	    print ("You have selected to QUIT")
	    break
