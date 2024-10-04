"""
addrStrConv or Address String Conversion was made by @Argonisin in github.

This project aims for my understanding in classes and how they function,
This also aims for my practice in hex, octa, binary conversion of a decimal
value in python, Also it gives us a basic understanding on how packet addresses work (Not in this format)

:encoder(listOfString).encode(): Returns a literal string 
ex. 
[012010[0]:0x6e2] = 'hello world'

dev note: "No way i can make a decoder for this.. It's plain impossible for me i think,
This is made for fun anyways and to practice myself, so yeah i wont be making a decoder"

dev note(1): "If used in industrial places, this encoder poses a huge security risk."
"""

import string

# This class checks for the amount of digits used in the text 
class IntChck:
    
    def __init__(self, STRING:list[str]) -> None:
        self.str = STRING
        self.lenStr = len(self.str)
    
    def count(self) -> int:
        count=0
        for i in range(self.lenStr):
            if self.str[i] in list(string.digits):
                count+=1
        return count

# This class checks for the amount of special characters used in the text
class specialChck:
    
    def __init__(self, STRING:list[str]) -> None:
        self.str = STRING
        self.lenStr = len(self.str)
        
    def count(self) -> int:
        count=0
        for i in range(self.lenStr):
            if self.str[i] in list(string.punctuation):
                count+=1
        return count
    
# This class checks for the amount of lowercase or uppercase used in a text
class up_lowChck:
    
    def __init__(self, STRING:list[str]) -> None:
        self.str = STRING
        self.lenStr = len(self.str)
        
    def checkUpper(self) -> int:
        count=0
        for i in range(self.lenStr):
            if self.str[i] in list(string.ascii_uppercase):
                count+=1
        return count

    def checkLower(self) -> int:
        count=0
        for i in range(self.lenStr):
            if self.str[i] in list(string.ascii_lowercase):
                count+=1
        return count

# Encoder class
class encoder:
    
    # Initialization
    def __init__(self, STRING:list[str]) -> None:
        self.str = STRING
        self.lenStr = len(self.str)
        self.lower = up_lowChck(self.str).checkLower()
        self.upper = up_lowChck(self.str).checkUpper()
        self.special = specialChck(self.str).count()
        self.int = IntChck(self.str).count()
    
    # Encode Method
    def encode(self):
        """For the value of the hex__ variable:
           First we translate the decimal into binary, and then that binary to octadecimal,
           and then finally that octadecimal to hexidecimal.  
        """
        hex__ = (hex(int(oct(int(bin(self.lenStr)[2:]))[2:])))
        
        # A octadecimal conversion of the amount of lowercased and uppercased in the text
        lAddr, uAddr = oct(self.lower)[2:], oct(self.upper)[2:] 
        # Amount of special characters and decimal in the text
        special, Int = self.special, self.int 
        # Amount of characters in the text
        aAddr = self.lower + self.upper 
        
        literal_string = [special,lAddr,uAddr,aAddr,f'[{Int}]',':',hex__]
        return ''.join(map(str, literal_string))


# <<User-Input Encoding>>

while True:
    print("STRING TO ADDRESS conversion")
    user = input("Type anything: ")
    
    if user:
        textListed = [i for i in user if i != ' '] # Removes the spaces on the string the user provided
        addrString = encoder(textListed).encode()
        
        print(f"STRING ADDRESS : {addrString}\n")
    else:
        print("\nActually type something, not just a space.\n")
